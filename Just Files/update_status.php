<link rel="stylesheet" href="assets/style.css">
<?php
session_start();
if (!isset($_SESSION['user_id']) || $_SESSION['role'] !== 'user') {
    header("Location: index.php");
    exit();
}

require_once 'classes/Task.php';
$task = new Task();

// Handle updates
foreach ($_POST['status'] as $taskId => $newStatus) {
    if (!empty($newStatus)) {
        $task->updateTaskStatus($taskId, $newStatus);
    }
}

header("Location: my_tasks.php");
exit();
