-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 25, 2023 at 06:15 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ransom`
--
CREATE DATABASE IF NOT EXISTS `ransom` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `ransom`;

-- --------------------------------------------------------

--
-- Table structure for table `ransom_info`
--

CREATE TABLE `ransom_info` (
  `time` varchar(255) DEFAULT NULL,
  `sys_name` varchar(255) DEFAULT NULL,
  `dec_key` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ransom_info`
--

INSERT INTO `ransom_info` (`time`, `sys_name`, `dec_key`) VALUES
('[2023-02-25 22:58:24.790959]', 'LAPTOP-B879B2CK', '/IfuP.HIc4mcQMo,GEyC/]gFEy9TTujffLNKs5S?kn.xyaNIWzsiL9VrJ1X7[pX1');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
