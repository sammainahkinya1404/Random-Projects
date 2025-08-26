<link rel="stylesheet" href="assets/style.css">
<?php
require_once 'classes/User.php';
$userClass = new User();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $userClass->addUser($_POST['name'], $_POST['email'], $_POST['password'], $_POST['role']);
    header("Location: users.php");
    exit();
}
?>
<div class="form-wrapper">
<h2>Add New User</h2>
<form method="POST">
    Name: <input type="text" name="name" required><br><br>
    Email: <input type="email" name="email" required><br><br>
    Password: <input type="password" name="password" required><br><br>
    Role:
    <select name="role">
        <option value="user">User</option>
        <option value="admin">Admin</option>
    </select><br><br>

    <button type="submit">Add User</button>
</form>
<a href="users.php">← Cancel</a>

</div>

<script src="assets/app.js"></script>


<link rel="stylesheet" href="assets/style.css">
<?php
require_once 'classes/User.php';
$userClass = new User();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $userClass->addUser($_POST['name'], $_POST['email'], $_POST['password'], $_POST['role']);
    header("Location: users.php");
    exit();
}
?>
<div class="form-wrapper">
<h2>Add New User</h2>
<form method="POST">
    Name: <input type="text" name="name" required><br><br>
    Email: <input type="email" name="email" required><br><br>
    Password: <input type="password" name="password" required><br><br>
    Role:
    <select name="role">
        <option value="user">User</option>
        <option value="admin">Admin</option>
    </select><br><br>

    <button type="submit">Add User</button>
</form>
<a href="users.php">← Cancel</a>

</div>

<script src="assets/app.js"></script>


<link rel="stylesheet" href="assets/style.css">
<?php
require_once 'classes/User.php';
$userClass = new User();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $userClass->addUser($_POST['name'], $_POST['email'], $_POST['password'], $_POST['role']);
    header("Location: users.php");
    exit();
}
?>
<div class="form-wrapper">
<h2>Add New User</h2>
<form method="POST">
    Name: <input type="text" name="name" required><br><br>
    Email: <input type="email" name="email" required><br><br>
    Password: <input type="password" name="password" required><br><br>
    Role:
    <select name="role">
        <option value="user">User</option>
        <option value="admin">Admin</option>
    </select><br><br>

    <button type="submit">Add User</button>
</form>
<a href="users.php">← Cancel</a>

</div>

<script src="assets/app.js"></script>


<link rel="stylesheet" href="assets/style.css">
<?php
require_once 'classes/User.php';
$userClass = new User();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $userClass->addUser($_POST['name'], $_POST['email'], $_POST['password'], $_POST['role']);
    header("Location: users.php");
    exit();
}
?>
<div class="form-wrapper">
<h2>Add New User</h2>
<form method="POST">
    Name: <input type="text" name="name" required><br><br>
    Email: <input type="email" name="email" required><br><br>
    Password: <input type="password" name="password" required><br><br>
    Role:
    <select name="role">
        <option value="user">User</option>
        <option value="admin">Admin</option>
    </select><br><br>

    <button type="submit">Add User</button>
</form>
<a href="users.php">← Cancel</a>

</div>

<script src="assets/app.js"></script>


