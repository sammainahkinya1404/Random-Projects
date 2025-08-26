<?php
session_start();
if (!isset($_SESSION['user_id']) || $_SESSION['role'] !== 'admin') {
    header("Location: index.php");
    exit();
}

require_once 'classes/User.php';
require_once 'classes/Task.php';

$userClass = new User();
$taskClass = new Task();

$users = $userClass->getAllUsers();
$tasks = $taskClass->getAllTasks();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Admin Panel - Task Manager</title>
    <link rel="stylesheet" href="assets/admin.css">
</head>
<body>

<div class="page-wrapper">
    <div>
        <h2>Welcome, Admin <?= htmlspecialchars($_SESSION['name']) ?>!</h2>
        <ul>
            <li><a href="users.php">Manage Users</a></li>
            <li><a href="admin_panel.php">Assign Tasks</a></li>
            <li><a href="dashboard.php">Back to Dashboard</a></li>
            <li><a href="logout.php">Logout</a></li>
        </ul>
    </div>

    <div class="form-wrapper">
        <h3>Assign a New Task</h3>
        <form method="POST" action="assign_task.php">
            <label>Title:</label>
            <input type="text" name="title" required>

            <label>Description:</label>
            <textarea name="description"></textarea>

            <label>Assign To:</label>
            <select name="assigned_to" required>
                <?php foreach ($users as $user): ?>
                    <option value="<?= $user['id'] ?>">
                        <?= htmlspecialchars($user['name']) ?> (<?= $user['role'] ?>)
                    </option>
                <?php endforeach; ?>
            </select>

            <label>Deadline:</label>
            <input type="date" name="deadline" required>

            <button type="submit">Assign Task</button>
        </form>
    </div>
</div>

<hr>

<h3>All Tasks</h3>
<table>
    <tr>
        <th>Title</th>
        <th>Assigned To</th>
        <th>Status</th>
        <th>Deadline</th>
        <th>Last Updated</th>
    </tr>
    <?php foreach ($tasks as $task): ?>
        <tr>
            <td><?= htmlspecialchars($task['title']) ?></td>
            <td><?= htmlspecialchars($task['assigned_user']) ?></td>
            <td><?= htmlspecialchars($task['status']) ?></td>
            <td><?= htmlspecialchars($task['deadline']) ?></td>
            <td><?= htmlspecialchars($task['status_updated_at']) ?></td>
        </tr>
    <?php endforeach; ?>
</table>

<script src="assets/app.js"></script>
</body>
</html>
