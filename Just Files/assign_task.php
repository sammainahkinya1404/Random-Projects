<?php
session_start();
header('Content-Type: application/json'); // Set JSON response early

if (!isset($_SESSION['user_id']) || $_SESSION['role'] !== 'admin') {
    echo json_encode(['status' => 'error', 'message' => 'Unauthorized']);
    exit();
}

require_once 'classes/Task.php';
require_once 'classes/User.php';
require_once 'mailer.php';  // uses PHPMailer

// Collect form inputs
$title = $_POST['title'] ?? null;
$description = $_POST['description'] ?? null;
$assignedTo = $_POST['assigned_to'] ?? null;
$deadline = $_POST['deadline'] ?? null;

if (!$title || !$description || !$assignedTo || !$deadline) {
    echo json_encode(['status' => 'error', 'message' => 'Missing required fields']);
    exit();
}

$task = new Task();
$user = new User();

// Assign the task in DB
$success = $task->assignTask($title, $description, $assignedTo, $deadline);

if ($success) {
    $userInfo = $user->getUserById($assignedTo);
    $email = $userInfo['email'] ?? null;
    $name = $userInfo['name'] ?? 'User';

    if ($email && sendTaskEmail($email, $name, $title, $description, $deadline)) {
        echo json_encode(['status' => 'success', 'message' => 'Task assigned and email sent']);
    } else {
        echo json_encode(['status' => 'partial', 'message' => 'Task assigned but email failed']);
    }
} else {
    echo json_encode(['status' => 'error', 'message' => 'Task assignment failed']);
}

exit();
