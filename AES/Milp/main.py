#!/usr/bin/env python3
"""
Main script to automate running figure plotting scripts (fig2.py to fig12.py, and logic.py)
"""

import os
import sys
import subprocess
import argparse
import time
from pathlib import Path

def run_script(script_name):
    """Run a single Python script and handle errors."""
    try:
        print(f"Running {script_name}...")
        start_time = time.time()
        
        # Run the script and capture output
        result = subprocess.run([sys.executable, script_name], 
                              capture_output=True, 
                              text=True, 
                              check=True)
        
        end_time = time.time()
        print(f"✓ {script_name} completed successfully in {end_time - start_time:.2f}s")
        
        # Print any output from the script
        if result.stdout:
            print(f"  Output: {result.stdout.strip()}")
            
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"✗ Error running {script_name}:")
        print(f"  Exit code: {e.returncode}")
        if e.stdout:
            print(f"  Stdout: {e.stdout}")
        if e.stderr:
            print(f"  Stderr: {e.stderr}")
        return False
    
    except FileNotFoundError:
        print(f"✗ Script {script_name} not found!")
        return False

def get_available_scripts():
    """Get list of available fig*.py scripts in current directory."""
    scripts = []
    for i in range(2, 13):  # fig2.py to fig12.py
        script_name = f"fig{i}.py"
        if Path(script_name).exists():
            scripts.append(script_name)
    return scripts

def main():
    parser = argparse.ArgumentParser(description="Run figure plotting scripts")
    parser.add_argument("--figures", "-f", nargs="+", type=int, 
                       help="Specific figure numbers to run (e.g., -f 2 5 8)")
    parser.add_argument("--all", "-a", action="store_true", 
                       help="Run all available figure scripts")
    parser.add_argument("--list", "-l", action="store_true", 
                       help="List available figure scripts")
    parser.add_argument("--continue-on-error", "-c", action="store_true", 
                       help="Continue running scripts even if one fails")
    
    args = parser.parse_args()
    
    # Get available scripts
    available_scripts = get_available_scripts()
    
    if args.list:
        print("Available figure scripts:")
        for script in available_scripts:
            print(f"  {script}")
        return
    
    if not available_scripts:
        print("No figure scripts (fig2.py to fig12.py) found in current directory!")
        return
    
    # Determine which scripts to run
    scripts_to_run = []
    
    if args.all:
        scripts_to_run = available_scripts
    elif args.figures:
        for fig_num in args.figures:
            script_name = f"fig{fig_num}.py"
            if script_name in available_scripts:
                scripts_to_run.append(script_name)
            else:
                print(f"Warning: {script_name} not found!")
    else:
        # Interactive mode - ask user which scripts to run
        print("Available figure scripts:")
        # Extract figure numbers from script names for display
        fig_numbers = []
        for script in available_scripts:
            fig_num = int(script.replace('fig', '').replace('.py', ''))
            fig_numbers.append(fig_num)
            print(f"  {fig_num}. {script}")
        print("  all. Run all scripts")
        
        try:
            choice = input("\nEnter your choice (figure number or 'all'): ").strip().lower()
            
            if choice == 'all':
                scripts_to_run = available_scripts
            else:
                choice_num = int(choice)
                if choice_num in fig_numbers:
                    script_name = f"fig{choice_num}.py"
                    scripts_to_run = [script_name]
                else:
                    print("Invalid choice!")
                    return
        except (ValueError, KeyboardInterrupt):
            print("\nOperation cancelled.")
            return
    
    if not scripts_to_run:
        print("No scripts selected to run.")
        return
    
    # Run selected scripts
    print(f"\nRunning {len(scripts_to_run)} script(s)...")
    print("=" * 50)
    
    total_start_time = time.time()
    successful = 0
    failed = 0
    
    for script in scripts_to_run:
        success = run_script(script)
        if success:
            successful += 1
        else:
            failed += 1
            if not args.continue_on_error:
                print(f"\nStopping execution due to error in {script}")
                print("Use --continue-on-error to continue despite failures")
                break
        print("-" * 30)
    
    total_end_time = time.time()
    
    # Summary
    print("\nSUMMARY:")
    print(f"Total time: {total_end_time - total_start_time:.2f}s")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Total scripts: {successful + failed}")

if __name__ == "__main__":
    main()