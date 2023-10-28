-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-10-2023 a las 06:40:57
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `agua`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add cliente', 6, 'add_cliente'),
(22, 'Can change cliente', 6, 'change_cliente'),
(23, 'Can delete cliente', 6, 'delete_cliente'),
(24, 'Can view cliente', 6, 'view_cliente'),
(25, 'Can add cuenta', 7, 'add_cuenta'),
(26, 'Can change cuenta', 7, 'change_cuenta'),
(27, 'Can delete cuenta', 7, 'delete_cuenta'),
(28, 'Can view cuenta', 7, 'view_cuenta'),
(29, 'Can add user', 8, 'add_user'),
(30, 'Can change user', 8, 'change_user'),
(31, 'Can delete user', 8, 'delete_user'),
(32, 'Can view user', 8, 'view_user'),
(33, 'Can add lectura', 9, 'add_lectura'),
(34, 'Can change lectura', 9, 'change_lectura'),
(35, 'Can delete lectura', 9, 'delete_lectura'),
(36, 'Can view lectura', 9, 'view_lectura');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente_cliente`
--

CREATE TABLE `cliente_cliente` (
  `id_cliente` bigint(20) NOT NULL,
  `dpi` bigint(20) NOT NULL,
  `nombre` varchar(250) NOT NULL,
  `apellido` varchar(350) NOT NULL,
  `direccion` varchar(750) NOT NULL,
  `telefono` varchar(8) NOT NULL,
  `correo` varchar(250) DEFAULT NULL,
  `fecha` datetime(6) NOT NULL,
  `estado` int(11) NOT NULL,
  `usuario_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `cliente_cliente`
--

INSERT INTO `cliente_cliente` (`id_cliente`, `dpi`, `nombre`, `apellido`, `direccion`, `telefono`, `correo`, `fecha`, `estado`, `usuario_id`) VALUES
(2, 1978265471901, 'Erick', 'Sagastume', 'aldea santa rosalia', '51810896', '', '2023-08-20 22:18:07.914351', 1, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente_cuenta`
--

CREATE TABLE `cliente_cuenta` (
  `id_cuenta` varchar(150) NOT NULL,
  `direccion` varchar(750) NOT NULL,
  `limite` int(11) NOT NULL,
  `mensual` decimal(12,2) NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `dpi_id` bigint(20) NOT NULL,
  `usuario_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `cliente_cuenta`
--

INSERT INTO `cliente_cuenta` (`id_cuenta`, `direccion`, `limite`, `mensual`, `fecha`, `dpi_id`, `usuario_id`) VALUES
('1', 'aldea santa rosalia', 50, 50.00, '2023-08-20 22:18:38.897950', 2, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(6, 'Cliente', 'cliente'),
(7, 'Cliente', 'cuenta'),
(4, 'contenttypes', 'contenttype'),
(9, 'Lectura', 'lectura'),
(5, 'sessions', 'session'),
(8, 'user', 'user');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-08-03 20:19:24.201655'),
(2, 'contenttypes', '0002_remove_content_type_name', '2023-08-03 20:19:24.299379'),
(3, 'auth', '0001_initial', '2023-08-03 20:19:24.587672'),
(4, 'auth', '0002_alter_permission_name_max_length', '2023-08-03 20:19:24.643389'),
(5, 'auth', '0003_alter_user_email_max_length', '2023-08-03 20:19:24.651366'),
(6, 'auth', '0004_alter_user_username_opts', '2023-08-03 20:19:24.658325'),
(7, 'auth', '0005_alter_user_last_login_null', '2023-08-03 20:19:24.667301'),
(8, 'auth', '0006_require_contenttypes_0002', '2023-08-03 20:19:24.670295'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2023-08-03 20:19:24.678271'),
(10, 'auth', '0008_alter_user_username_max_length', '2023-08-03 20:19:24.686250'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2023-08-03 20:19:24.694229'),
(12, 'auth', '0010_alter_group_name_max_length', '2023-08-03 20:19:24.747106'),
(13, 'auth', '0011_update_proxy_permissions', '2023-08-03 20:19:24.755084'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2023-08-03 20:19:24.762065'),
(15, 'user', '0001_initial', '2023-08-03 20:19:25.044687'),
(16, 'Cliente', '0001_initial', '2023-08-03 20:19:25.260157'),
(17, 'admin', '0001_initial', '2023-08-03 20:19:25.400701'),
(18, 'admin', '0002_logentry_remove_auto_add', '2023-08-03 20:19:25.471158'),
(19, 'admin', '0003_logentry_add_action_flag_choices', '2023-08-03 20:19:25.500080'),
(20, 'sessions', '0001_initial', '2023-08-03 20:19:25.566628'),
(21, 'user', '0002_alter_user_groups_alter_user_user_permissions', '2023-08-03 20:19:25.587613'),
(22, 'user', '0003_user_estado', '2023-08-03 20:19:25.633519'),
(23, 'user', '0004_user_lugar', '2023-08-03 20:19:25.661481'),
(24, 'user', '0005_remove_user_lugar_user_aportado_user_dpi_and_more', '2023-08-03 20:19:25.780396'),
(25, 'user', '0006_remove_user_aportado_remove_user_prestado', '2023-08-03 20:19:25.828971'),
(26, 'Lectura', '0001_initial', '2023-08-19 18:59:25.272347'),
(27, 'Lectura', '0002_alter_lectura_mes', '2023-08-19 18:59:25.342960');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('ppgek9umjezzyrvor537w841ty4dcbrx', '.eJxVjjsOwjAQRO_iGlnxxpY3lPScwVp71zhAEimfKuLuJJILaOfNPM2uAm1rCdsic-hZXRWoy28WKb1kPAE_aXxMOk3jOvdRnxVd6aLvE8v7Vrt_gkJLOdbWUERBm8A5zJ6zz51pMaEXEEsgLguwz4BtbMA6TgYtGs9NQ9QZe0gHGWJ9CZ8vE7o8Lg:1qXvWi:WVz_TRfRMbrqfljvMSg2LhD5Bw5dZfQ74w4f3ouwWWU', '2023-09-04 03:24:24.497747'),
('urch38fvbzeoom5n5gjm9pm0tlet2b3z', '.eJxVjkEOwiAQRe_C2hCmJTB16d4zkIEZbNVCUtqV8e7apAvd_vfy8l8q0LaOYWuyhInVWYE6_W6R0kPKDvhO5VZ1qmVdpqh3RR-06WtleV4O9y8wUhv3LEaxuXdsMHUIEYW9dZiHgTrJWSI4od4jOmeHZCQBWwdIaBjBM36js8zxeAnvDx2XPHQ:1qRenr:eJw3cFadytjk_pn0c1DQ7qZTlQ_aybg_ZD575G0jkDA', '2023-08-17 20:20:11.545851'),
('x9ys46i2g9m4o89t15eetfuv25z9fvjz', '.eJxVjssOwiAQRf-FtSHNUMrg0r3f0MzAIFVLkz5Wxn9XEha6vefk5L7USMeex2OTdZyiOitQp9-NKTykVBDvVG6LDkvZ14l1VXSjm74uUZ6X5v4FMm25ZgdAAOcxGe8SGLZiyIlFtIkiu4ENEHHPCBEds-88hkhsQUznpP9GZ5m5vYT3BwB3PGU:1qXRDY:z6oQ59f5NCt5JpehWH0o-_iuskowGugK7Ih6OSp6IWg', '2023-09-02 19:02:36.754469');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `lectura_lectura`
--

CREATE TABLE `lectura_lectura` (
  `id` bigint(20) NOT NULL,
  `anterior` decimal(12,2) NOT NULL,
  `actual` decimal(12,2) NOT NULL,
  `consumo` decimal(12,2) NOT NULL,
  `exceso` decimal(12,2) NOT NULL,
  `cargo_mes` decimal(12,2) NOT NULL,
  `cargo_exceso` decimal(12,2) NOT NULL,
  `cargo_total` decimal(12,2) NOT NULL,
  `mes` varchar(250) NOT NULL,
  `ciclo` int(11) NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `id_cuenta_id` varchar(150) NOT NULL,
  `usuario_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_user`
--

CREATE TABLE `user_user` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `rol` varchar(250) DEFAULT NULL,
  `estado` int(11) NOT NULL,
  `dpi` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `user_user`
--

INSERT INTO `user_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `rol`, `estado`, `dpi`) VALUES
(2, 'pbkdf2_sha256$260000$CCA5StM8TLKhZ0q10yXjsB$PcF5nTxZ1zhdy6Uyra64JXcptQiAfAXXqxk2YRJ7eYA=', '2023-08-21 03:24:24.494747', 1, 'erick', 'erick', 'sagastume', '', 1, 1, '2023-08-19 19:00:48.978053', 'admin', 0, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_user_groups`
--

CREATE TABLE `user_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_user_user_permissions`
--

CREATE TABLE `user_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `cliente_cliente`
--
ALTER TABLE `cliente_cliente`
  ADD PRIMARY KEY (`id_cliente`),
  ADD KEY `Cliente_cliente_usuario_id_31b4c364_fk_user_user_id` (`usuario_id`);

--
-- Indices de la tabla `cliente_cuenta`
--
ALTER TABLE `cliente_cuenta`
  ADD PRIMARY KEY (`id_cuenta`),
  ADD KEY `Cliente_cuenta_dpi_id_28b94723_fk_Cliente_cliente_id_cliente` (`dpi_id`),
  ADD KEY `Cliente_cuenta_usuario_id_49ac75ec_fk_user_user_id` (`usuario_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_user_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `lectura_lectura`
--
ALTER TABLE `lectura_lectura`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Lectura_lectura_id_cuenta_id_a671e222_fk_Cliente_c` (`id_cuenta_id`),
  ADD KEY `Lectura_lectura_usuario_id_91853465_fk_user_user_id` (`usuario_id`);

--
-- Indices de la tabla `user_user`
--
ALTER TABLE `user_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `user_user_groups`
--
ALTER TABLE `user_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_user_groups_user_id_group_id_bb60391f_uniq` (`user_id`,`group_id`),
  ADD KEY `user_user_groups_group_id_c57f13c0_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `user_user_user_permissions`
--
ALTER TABLE `user_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_user_user_permissions_user_id_permission_id_64f4d5b8_uniq` (`user_id`,`permission_id`),
  ADD KEY `user_user_user_permi_permission_id_ce49d4de_fk_auth_perm` (`permission_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT de la tabla `cliente_cliente`
--
ALTER TABLE `cliente_cliente`
  MODIFY `id_cliente` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT de la tabla `lectura_lectura`
--
ALTER TABLE `lectura_lectura`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `user_user`
--
ALTER TABLE `user_user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `user_user_groups`
--
ALTER TABLE `user_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `user_user_user_permissions`
--
ALTER TABLE `user_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `cliente_cliente`
--
ALTER TABLE `cliente_cliente`
  ADD CONSTRAINT `Cliente_cliente_usuario_id_31b4c364_fk_user_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `cliente_cuenta`
--
ALTER TABLE `cliente_cuenta`
  ADD CONSTRAINT `Cliente_cuenta_dpi_id_28b94723_fk_Cliente_cliente_id_cliente` FOREIGN KEY (`dpi_id`) REFERENCES `cliente_cliente` (`id_cliente`),
  ADD CONSTRAINT `Cliente_cuenta_usuario_id_49ac75ec_fk_user_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `lectura_lectura`
--
ALTER TABLE `lectura_lectura`
  ADD CONSTRAINT `Lectura_lectura_id_cuenta_id_a671e222_fk_Cliente_c` FOREIGN KEY (`id_cuenta_id`) REFERENCES `cliente_cuenta` (`id_cuenta`),
  ADD CONSTRAINT `Lectura_lectura_usuario_id_91853465_fk_user_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `user_user_groups`
--
ALTER TABLE `user_user_groups`
  ADD CONSTRAINT `user_user_groups_group_id_c57f13c0_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `user_user_groups_user_id_13f9a20d_fk_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `user_user_user_permissions`
--
ALTER TABLE `user_user_user_permissions`
  ADD CONSTRAINT `user_user_user_permi_permission_id_ce49d4de_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `user_user_user_permissions_user_id_31782f58_fk_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
