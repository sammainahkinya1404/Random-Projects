import numpy as np
import pandas as pd
from scipy.optimize import minimize, linprog
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import List, Tuple, Dict
import cvxpy as cp

@dataclass
class AESParameters:
    """Parameters for All-Electric Ship"""
    vessel_id: int
    P_DSG_max: float  # Maximum DSG power (kW)
    P_DSG_min: float  # Minimum DSG power (kW)
    P_ramp: float     # Ramp rate limit (kW/h)
    E_ESS: float      # ESS capacity (kWh)
    P_dis_max: float  # Maximum discharge power (kW)
    P_dis_min: float  # Minimum discharge power (kW)
    P_sv1: float      # Service load during cruising (kW)
    P_sv2: float      # Service load during berthing (kW)
    c0: float
    c1: float
    c2: float # Fuel cost coefficients
    TC_ESS: float     # ESS investment cost ($/kW)
    T_low: int        # Earliest arrival time (hour)
    T_up: int         # Latest arrival time (hour)
    beta_k: float     # Satisfaction threshold
    
@dataclass  
class SeaportParameters:
    """Parameters for Seaport Microgrid"""
    n_buses: int      # Number of buses
    n_berths: int     # Number of berths
    V_min: float      # Minimum voltage (p.u.)
    V_max: float      # Maximum voltage (p.u.)
    tap_max: int      # Maximum daily OLTC switching
    berth_times: Dict[int, List[float]]  # Berthing times for each berth-vessel combination

class RouteOptimizer:
    """Optimal route planning with minimum sea resistance"""
    
    def __init__(self, grid_size: Tuple[int, int] = (10, 10)):
        self.grid_size = grid_size
        
    def generate_resistance_map(self, wind_conditions: np.ndarray) -> np.ndarray:
        """Generate resistance map based on Beaufort scale"""
        # Beaufort scale mapping (from Table I in paper)
        beaufort_scale = {
            0: 0.00, 1: 0.06, 2: 0.13, 3: 0.20,
            4: 0.26, 5: 0.33, 6: 0.40
        }
        
        resistance_map = np.zeros(self.grid_size)
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                wind_level = min(int(wind_conditions[i, j]), 6)
                resistance_map[i, j] = beaufort_scale[wind_level]
                
        return resistance_map
    
    def dijkstra_route_planning(self, resistance_map: np.ndarray, 
                              start: Tuple[int, int], end: Tuple[int, int]) -> Tuple[List, float]:
        """Find optimal route using Dijkstra algorithm"""
        import heapq
        
        rows, cols = resistance_map.shape
        distances = np.full((rows, cols), np.inf)
        distances[start] = 0
        previous = {}
        pq = [(0, start)]
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), 
                     (1, 1), (1, -1), (-1, 1), (-1, -1)]  # 8-directional
        
        while pq:
            current_dist, current = heapq.heappop(pq)
            
            if current == end:
                break
                
            if current_dist > distances[current]:
                continue
                
            for dx, dy in directions:
                nx, ny = current[0] + dx, current[1] + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    neighbor = (nx, ny)
                    new_dist = current_dist + resistance_map[nx, ny]
                    
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        previous[neighbor] = current
                        heapq.heappush(pq, (new_dist, neighbor))
        
        # Reconstruct path
        path = []
        current = end
        while current in previous:
            path.append(current)
            current = previous[current]
        path.append(start)
        path.reverse()
        
        return path, distances[end]

class VoyageScheduler:
    """Optimal voyage scheduling for AES"""
    
    def __init__(self, aes_params: AESParameters, d_route: float = 30.0):
        self.params = aes_params
        self.d_route = d_route  # Route distance in nautical miles
        self.rho1, self.rho2 = 0.0355, 3.165  # Propulsion power coefficients
        
    def propulsion_power(self, velocity: float, resistance: float) -> float:
        """Calculate propulsion power P_pl = rho1 * v^rho2 * (1 + f_t)"""
        return self.rho1 * (velocity ** self.rho2) * (1 + resistance)
    
    def dsg_cost(self, P_DSG: float) -> float:
        """DSG fuel cost: c2*P^2 + c1*P + c0"""
        return (self.params.c2 * P_DSG**2 + 
                self.params.c1 * P_DSG + 
                self.params.c0)
    
    def ess_degradation_cost(self, P_dis: float, DOD: float) -> float:
        """ESS degradation cost based on DOD"""
        # Simplified battery lifetime model
        alpha0, alpha1, alpha2 = 1.69e4, -0.24, -2.57
        L_ESS = alpha0 * np.exp(alpha1 * DOD + alpha2)
        return self.params.TC_ESS * P_dis / (L_ESS * self.params.E_ESS)
    
    def optimize_voyage(self, T_a: int, resistance_profile: List[float]) -> Dict:
        """Solve voyage scheduling optimization for given arrival time"""
        
        # Calculate cruise duration
        T_s = 8  # Start time (8:00)
        cruise_hours = T_a - T_s
        
        if cruise_hours <= 0:
            return None
            
        # Decision variables: velocity, P_DSG, P_dis for each hour
        n_vars = 3 * cruise_hours  # v, P_DSG, P_dis for each time step
        
        # Objective: minimize total operation cost
        def objective(x):
            total_cost = 0
            for t in range(cruise_hours):
                v_t = x[t]
                P_DSG_t = x[cruise_hours + t]
                P_dis_t = x[2 * cruise_hours + t]
                
                # DSG cost
                total_cost += self.dsg_cost(P_DSG_t)
                
                # ESS degradation cost (simplified)
                DOD_t = P_dis_t / self.params.E_ESS
                total_cost += self.ess_degradation_cost(P_dis_t, DOD_t)
                
            return total_cost
        
        # Constraints
        constraints = []
        
        # Power balance constraint for each time step
        for t in range(cruise_hours):
            def power_balance(x, t=t):
                v_t = x[t]
                P_DSG_t = x[cruise_hours + t]
                P_dis_t = x[2 * cruise_hours + t]
                f_t = resistance_profile[t] if t < len(resistance_profile) else 0.2
                
                P_pl_t = self.propulsion_power(v_t, f_t)
                return P_DSG_t + P_dis_t - P_pl_t - self.params.P_sv1
                
            constraints.append({'type': 'eq', 'fun': lambda x, t=t: power_balance(x, t)})
        
        # Distance constraint: sum(v_t) = d_route
        constraints.append({
            'type': 'eq', 
            'fun': lambda x: np.sum(x[:cruise_hours]) - self.d_route
        })
        
        # Bounds
        bounds = []
        # Velocity bounds
        for t in range(cruise_hours):
            bounds.append((5, 20))  # v_min, v_max in knots
        # P_DSG bounds  
        for t in range(cruise_hours):
            bounds.append((self.params.P_DSG_min, self.params.P_DSG_max))
        # P_dis bounds
        for t in range(cruise_hours):
            bounds.append((self.params.P_dis_min, self.params.P_dis_max))
            
        # Initial guess
        x0 = np.concatenate([
            np.full(cruise_hours, self.d_route / cruise_hours),  # velocity
            np.full(cruise_hours, self.params.P_DSG_min),       # P_DSG
            np.full(cruise_hours, 0)                            # P_dis
        ])
        
        # Solve optimization
        try:
            result = minimize(objective, x0, method='SLSQP', 
                            bounds=bounds, constraints=constraints)
            
            if result.success:
                # Calculate final SOC
                total_discharge = np.sum(result.x[2*cruise_hours:])
                SOC_initial = 0.9  # Assume full charge at start
                eta_dis = 0.95
                SOC_final = SOC_initial - (total_discharge * cruise_hours) / (self.params.E_ESS * eta_dis)
                
                return {
                    'success': True,
                    'T_a': T_a,
                    'SOC_a': max(0.1, SOC_final),  # Ensure minimum SOC
                    'cost': result.fun,
                    'velocity_profile': result.x[:cruise_hours],
                    'P_DSG_profile': result.x[cruise_hours:2*cruise_hours],
                    'P_dis_profile': result.x[2*cruise_hours:]
                }
            else:
                return None
                
        except Exception as e:
            print(f"Optimization failed for T_a={T_a}: {e}")
            return None

class SatisfactoryIndex:
    """Calculate and manage satisfactory index for AES"""
    
    @staticmethod
    def calculate_SI(costs: List[float]) -> List[float]:
        """Calculate satisfactory index for each cost"""
        C_max = max(costs)
        C_min = min(costs)
        
        if C_max == C_min:
            return [1.0] * len(costs)
            
        SI_values = []
        for C_k in costs:
            SI_k = (C_max - C_k) / (C_max - C_min)
            SI_values.append(SI_k)
            
        return SI_values
    
    @staticmethod
    def filter_by_threshold(Ta_SOCa_pairs: List[Dict], beta_k: float) -> List[Dict]:
        """Filter T_a-SOC_a pairs based on satisfaction threshold"""
        if not Ta_SOCa_pairs:
            return []
            
        costs = [pair['cost'] for pair in Ta_SOCa_pairs]
        SI_values = SatisfactoryIndex.calculate_SI(costs)
        
        filtered_pairs = []
        for i, (pair, SI) in enumerate(zip(Ta_SOCa_pairs, SI_values)):
            pair['SI'] = SI
            if SI >= beta_k:
                filtered_pairs.append(pair)
                
        return filtered_pairs

class VoltageRegulator:
    """Voltage regulation in seaport microgrids with berth allocation"""
    
    def __init__(self, seaport_params: SeaportParameters):
        self.params = seaport_params
        
    def optimize_voltage_regulation(self, Ta_SOCa_pairs_all: Dict[int, List[Dict]], 
                                  pv_forecast: np.ndarray, load_forecast: np.ndarray) -> Dict:
        """Solve extended OPF with berth allocation"""
        
        n_vessels = len(Ta_SOCa_pairs_all)
        n_hours = len(pv_forecast)
        n_berths = self.params.n_berths
        
        # Decision variables using CVXPY for MILP
        # Binary variables for berth allocation
        omega = cp.Variable((n_berths, n_vessels, n_hours), boolean=True)  # berth allocation
        mu = cp.Variable((n_berths, n_vessels, n_hours), boolean=True)     # start service
        
        # Continuous variables
        tap = cp.Variable(n_hours, integer=True)  # OLTC tap position
        Q_PV = cp.Variable((4, n_hours))          # PV reactive power (4 PVs)
        P_ch = cp.Variable((n_berths, n_vessels, n_hours))  # Charging power
        
        # Vessel selection variables (which Ta-SOCa pair to choose)
        vessel_selection = {}
        for vessel_id in Ta_SOCa_pairs_all:
            n_pairs = len(Ta_SOCa_pairs_all[vessel_id])
            vessel_selection[vessel_id] = cp.Variable(n_pairs, boolean=True)
        
        # Objective: minimize power losses (simplified as total charging power deviation)
        objective = cp.Minimize(cp.sum(cp.square(P_ch)))
        
        constraints = []
        
        # Berth allocation constraints
        for t in range(n_hours):
            for m in range(n_berths):
                # Each berth serves at most one vessel
                constraints.append(cp.sum([omega[m, k, t] for k in range(n_vessels)]) <= 1)
            
            for k in range(n_vessels):
                # Each vessel at most one berth
                constraints.append(cp.sum([omega[m, k, t] for m in range(n_berths)]) <= 1)
        
        # Vessel selection constraints
        for vessel_id in vessel_selection:
            constraints.append(cp.sum(vessel_selection[vessel_id]) == 1)
        
        # Power flow constraints (simplified)
        for t in range(n_hours):
            total_charging = cp.sum([P_ch[m, k, t] * omega[m, k, t] 
                                   for m in range(n_berths) for k in range(n_vessels)])
            
            # Power balance (simplified - assuming radial network)
            constraints.append(total_charging <= 1000)  # Maximum port capacity
        
        # OLTC constraints
        constraints.append(tap >= -10)
        constraints.append(tap <= 10)
        
        # PV reactive power constraints
        for i in range(4):
            for t in range(n_hours):
                constraints.append(Q_PV[i, t] >= -50)  # -50 kVar
                constraints.append(Q_PV[i, t] <= 50)   # +50 kVar
        
        # Charging power constraints
        constraints.append(P_ch >= 0)
        constraints.append(P_ch <= 200)  # Maximum charging power
        
        # Create and solve problem
        problem = cp.Problem(objective, constraints)
        
        try:
            problem.solve(solver=cp.CBC, verbose=False)  # Using open-source CBC solver
            
            if problem.status == cp.OPTIMAL:
                return {
                    'success': True,
                    'omega': omega.value,
                    'tap': tap.value,
                    'Q_PV': Q_PV.value,
                    'P_ch': P_ch.value,
                    'objective_value': problem.value,
                    'vessel_selection': {k: v.value for k, v in vessel_selection.items()}
                }
            else:
                return {'success': False, 'status': problem.status}
                
        except Exception as e:
            print(f"Voltage regulation optimization failed: {e}")
            return {'success': False, 'error': str(e)}

class CoordinatedOptimizer:
    """Main coordinated optimization procedure (Algorithm 1)"""
    
    def __init__(self, aes_fleet: List[AESParameters], seaport_params: SeaportParameters):
        self.aes_fleet = aes_fleet
        self.seaport_params = seaport_params
        self.route_optimizer = RouteOptimizer()
        self.voltage_regulator = VoltageRegulator(seaport_params)
        
    def run_coordinated_optimization(self, wind_conditions: np.ndarray, 
                                   pv_forecast: np.ndarray, 
                                   load_forecast: np.ndarray) -> Dict:
        """Execute Algorithm 1: Customized Coordinated Optimization Procedure"""
        
        print("Step 1: Initialization completed")
        
        # Step 2: Solve optimal route planning
        print("Step 2: Solving route planning...")
        resistance_map = self.route_optimizer.generate_resistance_map(wind_conditions)
        optimal_route, total_resistance = self.route_optimizer.dijkstra_route_planning(
            resistance_map, (0, 0), (9, 9)
        )
        print(f"Optimal route found with total resistance: {total_resistance:.3f}")
        
        # Step 3: Solve voyage scheduling for all AES
        print("Step 3: Solving voyage scheduling...")
        all_Ta_SOCa_pairs = {}
        
        for aes in self.aes_fleet:
            voyage_scheduler = VoyageScheduler(aes)
            pairs = []
            
            # Generate resistance profile (simplified)
            resistance_profile = [0.15, 0.20, 0.18, 0.22]
            
            for T_a in range(aes.T_low, aes.T_up + 1):
                result = voyage_scheduler.optimize_voyage(T_a, resistance_profile)
                if result and result['success']:
                    pairs.append(result)
            
            all_Ta_SOCa_pairs[aes.vessel_id] = pairs
            print(f"AES {aes.vessel_id}: Generated {len(pairs)} T_a-SOC_a pairs")
        
        # Step 4: Selection based on satisfactory index
        print("Step 4: Filtering T_a-SOC_a pairs based on SI...")
        filtered_pairs = {}
        
        for vessel_id, pairs in all_Ta_SOCa_pairs.items():
            aes_params = next(aes for aes in self.aes_fleet if aes.vessel_id == vessel_id)
            filtered = SatisfactoryIndex.filter_by_threshold(pairs, aes_params.beta_k)
            filtered_pairs[vessel_id] = filtered
            print(f"AES {vessel_id}: {len(filtered)} pairs after SI filtering (β_k={aes_params.beta_k})")
        
        # Step 5: Solve voltage regulation with berth allocation
        print("Step 5: Solving voltage regulation...")
        voltage_result = self.voltage_regulator.optimize_voltage_regulation(
            filtered_pairs, pv_forecast, load_forecast
        )
        
        # Step 6: Determine final voyage scheduling strategy
        print("Step 6: Finalizing strategies...")
        final_strategies = {}
        
        if voltage_result['success']:
            for vessel_id, pairs in filtered_pairs.items():
                if pairs:  # If there are valid pairs
                    # Select the pair with best SI (simplified selection)
                    best_pair = max(pairs, key=lambda x: x['SI'])
                    final_strategies[vessel_id] = best_pair
                    
            print("Coordinated optimization completed successfully!")
            
            return {
                'success': True,
                'route': optimal_route,
                'vessel_strategies': final_strategies,
                'voltage_control': voltage_result,
                'summary': self._generate_summary(final_strategies, voltage_result)
            }
        else:
            print("Voltage regulation failed!")
            return {'success': False, 'error': 'Voltage regulation optimization failed'}
    
    def _generate_summary(self, strategies: Dict, voltage_result: Dict) -> Dict:
        """Generate optimization summary"""
        total_cost = sum(strategy['cost'] for strategy in strategies.values())
        avg_SI = np.mean([strategy['SI'] for strategy in strategies.values()])
        
        return {
            'total_operation_cost': total_cost,
            'average_SI': avg_SI,
            'power_losses': voltage_result.get('objective_value', 0),
            'n_vessels_optimized': len(strategies)
        }

# Example usage and testing
def run_example():
    """Run example optimization"""
    
    # Define AES fleet
    aes_fleet = [
        AESParameters(
            vessel_id=1, P_DSG_max=300, P_DSG_min=80, P_ramp=200,
            E_ESS=120, P_dis_max=60, P_dis_min=10, P_sv1=10, P_sv2=10,
            c0=3.02e-5, c1=0.37, c2=0.01, TC_ESS=600,
            T_low=10, T_up=12, beta_k=0.5
        ),
        AESParameters(
            vessel_id=2, P_DSG_max=400, P_DSG_min=120, P_ramp=200,
            E_ESS=180, P_dis_max=90, P_dis_min=10, P_sv1=20, P_sv2=20,
            c0=3.02e-5, c1=0.37, c2=0.01, TC_ESS=600,
            T_low=10, T_up=12, beta_k=0.5
        )
    ]
    
    # Seaport parameters
    seaport_params = SeaportParameters(
        n_buses=16, n_berths=3, V_min=0.95, V_max=1.05, tap_max=10,
        berth_times={0: [2, 4, 6], 1: [2, 4, 6], 2: [1, 2, 3]}
    )
    
    # Initialize optimizer
    optimizer = CoordinatedOptimizer(aes_fleet, seaport_params)
    
    # Generate sample data
    wind_conditions = np.random.randint(0, 4, size=(10, 10))
    pv_forecast = np.array([0, 0, 0.2, 0.6, 0.8, 1.0, 0.9, 0.6, 0.3, 0.1] + [0]*15)
    load_forecast = np.array([0.7, 0.6, 0.7, 0.8, 0.9, 0.85, 0.8, 0.9, 1.0, 0.8] + [0.7]*15)
    
    # Run optimization
    result = optimizer.run_coordinated_optimization(wind_conditions, pv_forecast, load_forecast)
    
    if result['success']:
        print("\n=== OPTIMIZATION RESULTS ===")
        print(f"Total Operation Cost: ${result['summary']['total_operation_cost']:.2f}")
        print(f"Average Satisfaction Index: {result['summary']['average_SI']:.3f}")
        print(f"Power Losses: {result['summary']['power_losses']:.2f} kWh")
        print(f"Vessels Optimized: {result['summary']['n_vessels_optimized']}")
        
        print("\nVessel Strategies:")
        for vessel_id, strategy in result['vessel_strategies'].items():
            print(f"  AES {vessel_id}: Arrive at {strategy['T_a']}:00, "
                  f"SOC_a={strategy['SOC_a']:.3f}, SI={strategy['SI']:.3f}")
    else:
        print("Optimization failed!")

# if __name__ == "__main__":
#     run_example()