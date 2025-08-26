<?php

//class Database

class Database{
    private $host= 'sql210.infinityfree.com';
    private $db_name= 'f0_39461062_task_manager';
    private $username= 'if0_39461062';
    private $password= 'vd9bmTSeVMa';  
    private $conn;

    public function connect() {
        try {
            $this->conn = new PDO(
                "mysql:host=$this->host;dbname=$this->db_name;charset=utf8mb4",
                $this->username,
                $this->password
            );

            // Set error mode to exception
            $this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            return $this->conn;
        } catch (PDOException $e) {
            die("Database connection failed: " . $e->getMessage());
        }
    }

}


?>