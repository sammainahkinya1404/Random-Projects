-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 13, 2025 at 01:36 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `task_manager`
--

-- --------------------------------------------------------

--
-- Table structure for table `tasks`
--

CREATE TABLE `tasks` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` text DEFAULT NULL,
  `assigned_to` int(11) DEFAULT NULL,
  `deadline` date DEFAULT NULL,
  `status` enum('Pending','In Progress','Completed') DEFAULT 'Pending',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `status_updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tasks`
--

INSERT INTO `tasks` (`id`, `title`, `description`, `assigned_to`, `deadline`, `status`, `created_at`, `status_updated_at`) VALUES
(1, 'Finish report', 'Write the end-of-month financial report', 1, '2025-07-15', 'Completed', '2025-07-12 09:34:01', '2025-07-12 09:34:01'),
(4, 'Finish report', 'Write the end-of-month financial report', 1, '2025-07-15', 'Pending', '2025-07-12 11:52:26', '2025-07-12 11:52:26'),
(5, 'test2', 'hello', 3, '2025-07-14', 'Completed', '2025-07-12 12:07:59', '2025-07-12 12:17:23'),
(6, 'task4', 'we need you to update the databases', 3, '2025-07-14', 'Completed', '2025-07-12 12:16:28', '2025-07-13 10:45:59'),
(7, 'Coding', 'Develop  and Train an ML Classifier for spam detection', 3, '2025-07-14', 'Completed', '2025-07-13 06:28:36', '2025-07-13 10:45:59'),
(8, 'Coding Challenge', 'Develop a web app for selling Dorper sheep in Nakuru County', 3, '2025-07-25', 'Completed', '2025-07-13 07:03:13', '2025-07-13 09:01:06'),
(9, 'Task 5', 'Testing PHPMailer', 3, '2025-07-23', 'Completed', '2025-07-13 07:20:10', '2025-07-13 10:45:59'),
(10, 'Test v1', 'hello', 3, '2025-07-15', 'Completed', '2025-07-13 08:56:57', '2025-07-13 09:01:06'),
(11, 'Test v1', 'hello', 3, '2025-07-15', 'Completed', '2025-07-13 08:59:56', '2025-07-13 10:45:59'),
(12, 'Micro services ', 'We need to finish ', 4, '2025-07-15', 'In Progress', '2025-07-13 09:04:47', '2025-07-13 09:20:50');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` enum('admin','user') DEFAULT 'user',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `password`, `role`, `created_at`) VALUES
(1, 'Jane Doe', 'jane@example.com', '$2y$10$IiEaEi4BxQGjDw9guCm6se6eGo6r9GNacltF.HH0XAIlrH9a5VVXW', 'admin', '2025-07-12 09:28:08'),
(3, 'Kinyanjui Mainah', 'kinyanjuisamson1404@gmail.com', '$2y$10$DcNgpqZuiXtJ8HMbMJgPr.RBDXIfgu8xYOgw8LjZSHaxC/ODRantG', 'user', '2025-07-12 12:05:20'),
(4, 'Twizard', 'twizard720@gmail.com', '$2y$10$Ok2.IsuO7N8/Zlsi27iXLexQkikKyndt4oxjSvk6UfCs52J8x1fXO', 'user', '2025-07-13 09:03:20');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tasks`
--
ALTER TABLE `tasks`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tasks_ibfk_1` (`assigned_to`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tasks`
--
ALTER TABLE `tasks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tasks`
--
ALTER TABLE `tasks`
  ADD CONSTRAINT `tasks_ibfk_1` FOREIGN KEY (`assigned_to`) REFERENCES `users` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
