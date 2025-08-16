-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 24, 2024 at 05:35 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `new`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(20) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `username`, `password`) VALUES
(1, 'admin', '1234'),
(2, 'mushu', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `bgmi`
--

CREATE TABLE `bgmi` (
  `id` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `role` varchar(100) NOT NULL,
  `image` varchar(200) NOT NULL,
  `youtube` varchar(200) NOT NULL,
  `instagram` varchar(200) NOT NULL,
  `twitter` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bgmi`
--

INSERT INTO `bgmi` (`id`, `name`, `role`, `image`, `youtube`, `instagram`, `twitter`) VALUES
(1, 'Ronny', 'Filter', 'static/rony.jpg', '', '', ''),
(3, 'Nakul', 'Assulter', 'static/nakul.jpg', 'https://www.youtube.com/@8bitMafia', 'https://www.instagram.com/', 'https://www.instagram.com/'),
(4, 'Manya', 'Igl', 'static/manya.jpg', '', '', ''),
(5, 'Saumay', 'Support', 'static/saumay.jpg', '', '', ''),
(8, 'Mayavi', 'Coach', 'static/mayavi.jpeg', 'https://www.youtube.com/@GAMERxMaYaVi', 'https://www.instagram.com/soul_mayavi28/?hl=en', 'https://twitter.com/soul_mayavi'),
(9, 'Ayogi', 'Analyst', 'static/ayogi.jpeg', 'https://www.youtube.com/@ayogi', 'https://www.instagram.com/soul_ayogi27/?hl=en', 'https://twitter.com/soul_ayogi?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor'),
(10, 'Skipz', 'Assulter', 'static/skipz.webp', '', '', ''),
(11, 'Sid', 'Manager', 'static/sid.avif', 'https://www.youtube.com/c/sidjosh1/videos', 'https://www.instagram.com/s8ul.sid/?hl=en', 'https://twitter.com/s8ulsidbhai');

-- --------------------------------------------------------

--
-- Table structure for table `suggestion`
--

CREATE TABLE `suggestion` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `twitter_username` varchar(100) NOT NULL,
  `suggestion` text NOT NULL,
  `timestamp` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `suggestion`
--

INSERT INTO `suggestion` (`id`, `name`, `twitter_username`, `suggestion`, `timestamp`) VALUES
(1, 'mushu', 'mushu0729', 'very good', '2024-12-04 14:23:57'),
(2, 'nayaz', 'nayaz221', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.', '2024-12-04 15:43:38');

-- --------------------------------------------------------

--
-- Table structure for table `valorant`
--

CREATE TABLE `valorant` (
  `id` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `role` varchar(100) NOT NULL,
  `image_url` varchar(200) NOT NULL,
  `youtube_url` varchar(200) NOT NULL,
  `instagram_url` varchar(200) NOT NULL,
  `twitter_url` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `valorant`
--

INSERT INTO `valorant` (`id`, `name`, `role`, `image_url`, `youtube_url`, `instagram_url`, `twitter_url`) VALUES
(2, 'Binks', 'Igl', 'static/binks.jpeg', 'https://www.youtube.com/c/sidjosh1/videos', '', ''),
(3, 'EdiT999', 'Entry Fragger', 'static/edit999.jpeg', '', '', ''),
(4, 'Ezzy', 'Support', 'static/ezzy.jpeg', '', '', ''),
(5, 'NotFoxx', 'Secondary Entry Fragger', 'static/fox.jpeg', '', '', ''),
(6, 'Strixx', 'Lurker', 'static/strixx.jpeg', '', '', ''),
(7, 'Sid', 'Manager', 'static/sid.avif', '', '', ''),
(8, 'Kuzurii', 'Anchor', 'static/kuzuri.jpeg', '', '', ''),
(9, 'Zeref', 'Mentor', 'static/zeref.jpeg', 'https://www.youtube.com/@ayogi', '', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `bgmi`
--
ALTER TABLE `bgmi`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `suggestion`
--
ALTER TABLE `suggestion`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `valorant`
--
ALTER TABLE `valorant`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `bgmi`
--
ALTER TABLE `bgmi`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `suggestion`
--
ALTER TABLE `suggestion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `valorant`
--
ALTER TABLE `valorant`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
