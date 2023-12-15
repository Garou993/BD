/*!40101 SET NAMES utf8 */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET SQL_NOTES=0 */;
DROP TABLE IF EXISTS auth_group;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb3_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS auth_group_permissions;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=265 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS auth_permission;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb3_bin NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb3_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=169 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS auth_user;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb3_bin NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb3_bin NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb3_bin NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb3_bin NOT NULL,
  `email` varchar(254) COLLATE utf8mb3_bin NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS auth_user_groups;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS auth_user_user_permissions;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS builder_status;
CREATE TABLE `builder_status` (
  `master_id` int NOT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `time` date DEFAULT NULL,
  PRIMARY KEY (`master_id`),
  CONSTRAINT `builder_status_ibfk_1` FOREIGN KEY (`master_id`) REFERENCES `pc_builder` (`master_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS cars;
CREATE TABLE `cars` (
  `car_id` int NOT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `courier_id` int DEFAULT NULL,
  PRIMARY KEY (`car_id`),
  KEY `R_89` (`courier_id`),
  CONSTRAINT `cars_ibfk_1` FOREIGN KEY (`courier_id`) REFERENCES `couriers` (`courier_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS cleaner_status;
CREATE TABLE `cleaner_status` (
  `status` tinyint(1) DEFAULT NULL,
  `time` date DEFAULT NULL,
  `master_id` int NOT NULL,
  PRIMARY KEY (`master_id`),
  CONSTRAINT `cleaner_status_ibfk_1` FOREIGN KEY (`master_id`) REFERENCES `pc_cleaner` (`master_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS client;
CREATE TABLE `client` (
  `client_id` int NOT NULL,
  `full_name` varchar(100) COLLATE utf8mb3_bin DEFAULT NULL,
  `phone_number` varchar(32) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL,
  `client_email` varchar(50) COLLATE utf8mb3_bin DEFAULT NULL,
  `address` varchar(128) COLLATE utf8mb3_bin NOT NULL,
  PRIMARY KEY (`client_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS client_comment_courier;
CREATE TABLE `client_comment_courier` (
  `comment_id` int NOT NULL,
  `comment` varchar(128) COLLATE utf8mb3_bin DEFAULT NULL,
  `service_rating` float DEFAULT NULL,
  `datetime_comment` datetime DEFAULT NULL,
  `id_order` int NOT NULL,
  PRIMARY KEY (`comment_id`,`id_order`),
  KEY `R_63` (`id_order`),
  CONSTRAINT `client_comment_courier_ibfk_1` FOREIGN KEY (`id_order`) REFERENCES `orders` (`id_order`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS client_comment_devices;
CREATE TABLE `client_comment_devices` (
  `id_order` int NOT NULL,
  `comment_id` int NOT NULL,
  `comment_text` varchar(128) COLLATE utf8mb3_bin DEFAULT NULL,
  `item_rating` float NOT NULL,
  `datetime_comment` date DEFAULT NULL,
  PRIMARY KEY (`comment_id`,`id_order`),
  KEY `id_order` (`id_order`),
  CONSTRAINT `client_comment_devices_ibfk_1` FOREIGN KEY (`id_order`) REFERENCES `orders` (`id_order`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS client_comment_master;
CREATE TABLE `client_comment_master` (
  `client_comment_id` tinyint(1) NOT NULL,
  `comment` varchar(128) COLLATE utf8mb3_bin DEFAULT NULL,
  `rating` float DEFAULT NULL,
  `id_order` int NOT NULL,
  PRIMARY KEY (`client_comment_id`,`id_order`),
  KEY `R_88` (`id_order`),
  CONSTRAINT `client_comment_master_ibfk_1` FOREIGN KEY (`id_order`) REFERENCES `orders` (`id_order`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS couriers;
CREATE TABLE `couriers` (
  `courier_id` int NOT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `rating` float DEFAULT NULL,
  `time_to_deliver` datetime NOT NULL DEFAULT '2023-12-12 00:00:00',
  `id_order` int DEFAULT NULL,
  `delivery_price` float DEFAULT NULL,
  PRIMARY KEY (`courier_id`),
  KEY `R_43` (`id_order`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS django_admin_log;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb3_bin,
  `object_repr` varchar(200) COLLATE utf8mb3_bin NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb3_bin NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS django_content_type;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb3_bin NOT NULL,
  `model` varchar(100) COLLATE utf8mb3_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS django_migrations;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb3_bin NOT NULL,
  `name` varchar(255) COLLATE utf8mb3_bin NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS django_session;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb3_bin NOT NULL,
  `session_data` longtext COLLATE utf8mb3_bin NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS flash;
CREATE TABLE `flash` (
  `item_id` int NOT NULL AUTO_INCREMENT,
  `params` varchar(20) COLLATE utf8mb3_bin DEFAULT NULL,
  `price` float NOT NULL,
  `rating` float DEFAULT NULL,
  `amount` int DEFAULT NULL,
  `name` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin DEFAULT NULL,
  `type` varchar(20) COLLATE utf8mb3_bin DEFAULT 'Flash',
  PRIMARY KEY (`item_id`),
  CONSTRAINT `flash_ibfk_1` FOREIGN KEY (`item_id`) REFERENCES `items` (`item_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS hdd;
CREATE TABLE `hdd` (
  `item_id` int NOT NULL AUTO_INCREMENT,
  `params` varchar(20) COLLATE utf8mb3_bin DEFAULT NULL,
  `price` float NOT NULL,
  `rating` float DEFAULT NULL,
  `amount` int DEFAULT NULL,
  `name` varchar(20) COLLATE utf8mb3_bin DEFAULT NULL,
  `type` varchar(20) COLLATE utf8mb3_bin DEFAULT 'HDD',
  PRIMARY KEY (`item_id`),
  CONSTRAINT `hdd_ibfk_1` FOREIGN KEY (`item_id`) REFERENCES `items` (`item_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS indtracks;
CREATE TABLE `indtracks` (
  `ind_track_id` int NOT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `time_to_deliver` date DEFAULT NULL,
  PRIMARY KEY (`ind_track_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS indtracks_status;
CREATE TABLE `indtracks_status` (
  `status` tinyint(1) DEFAULT NULL,
  `time` date DEFAULT NULL,
  `ind_track_id` int NOT NULL,
  PRIMARY KEY (`ind_track_id`),
  CONSTRAINT `indtracks_status_ibfk_1` FOREIGN KEY (`ind_track_id`) REFERENCES `indtracks` (`ind_track_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS industries;
CREATE TABLE `industries` (
  `industry_id` int NOT NULL,
  `industry_address` varchar(20) COLLATE utf8mb3_bin NOT NULL,
  `industry_name` varchar(20) COLLATE utf8mb3_bin NOT NULL,
  PRIMARY KEY (`industry_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS invoice_items;
CREATE TABLE `invoice_items` (
  `item_id` int NOT NULL AUTO_INCREMENT COMMENT 'Primary Key',
  `item_name` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
  `params` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
  `type` varchar(20) COLLATE utf8mb3_bin DEFAULT NULL,
  `amount` int NOT NULL,
  `invoice_id` int DEFAULT NULL,
  `price` float NOT NULL DEFAULT '0',
  PRIMARY KEY (`item_id`),
  KEY `invoice_id` (`invoice_id`),
  CONSTRAINT `invoice_id` FOREIGN KEY (`invoice_id`) REFERENCES `invoices` (`invoice_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS invoices;
CREATE TABLE `invoices` (
  `invoice_id` int NOT NULL,
  `storage_id` int DEFAULT NULL,
  `ind_track_id` int DEFAULT NULL,
  `price` float DEFAULT NULL,
  `industry_id` int DEFAULT NULL,
  `invoices_date` datetime DEFAULT NULL,
  PRIMARY KEY (`invoice_id`),
  KEY `R_99` (`storage_id`),
  KEY `R_102` (`ind_track_id`),
  KEY `R_107` (`industry_id`),
  CONSTRAINT `invoices_ibfk_1` FOREIGN KEY (`storage_id`) REFERENCES `storage` (`storage_id`),
  CONSTRAINT `invoices_ibfk_2` FOREIGN KEY (`ind_track_id`) REFERENCES `indtracks` (`ind_track_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS items;
CREATE TABLE `items` (
  `item_id` int NOT NULL AUTO_INCREMENT,
  `item_name` varchar(32) COLLATE utf8mb3_bin NOT NULL,
  `storage_id` int NOT NULL,
  `type` varchar(20) COLLATE utf8mb3_bin DEFAULT NULL,
  PRIMARY KEY (`item_id`),
  KEY `R_95` (`storage_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS items_for_order;
CREATE TABLE `items_for_order` (
  `id` int NOT NULL AUTO_INCREMENT,
  `item_name` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
  `id_order` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `if_order` (`id_order`),
  CONSTRAINT `if_order` FOREIGN KEY (`id_order`) REFERENCES `orders` (`id_order`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS keyboards;
CREATE TABLE `keyboards` (
  `item_id` int NOT NULL AUTO_INCREMENT,
  `params` varchar(20) COLLATE utf8mb3_bin DEFAULT NULL,
  `price` float NOT NULL,
  `rating` float DEFAULT NULL,
  `amount` int DEFAULT NULL,
  `name` varchar(20) COLLATE utf8mb3_bin DEFAULT NULL,
  PRIMARY KEY (`item_id`),
  CONSTRAINT `keyboards_ibfk_1` FOREIGN KEY (`item_id`) REFERENCES `items` (`item_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS login;
CREATE TABLE `login` (
  `client_login` varchar(32) COLLATE utf8mb3_bin NOT NULL,
  `client_password` varchar(32) COLLATE utf8mb3_bin NOT NULL,
  `client_id` int NOT NULL,
  PRIMARY KEY (`client_id`,`client_login`),
  CONSTRAINT `login_ibfk_1` FOREIGN KEY (`client_id`) REFERENCES `client` (`client_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS master_status;
CREATE TABLE `master_status` (
  `status` tinyint(1) DEFAULT NULL,
  `time` datetime NOT NULL DEFAULT '2023-12-12 00:00:00',
  `master_id` char(128) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL,
  PRIMARY KEY (`master_id`),
  CONSTRAINT `master_status_ibfk_1` FOREIGN KEY (`master_id`) REFERENCES `pc_master` (`master_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS mice;
CREATE TABLE `mice` (
  `item_id` int NOT NULL AUTO_INCREMENT,
  `params` varchar(20) COLLATE utf8mb3_bin DEFAULT NULL,
  `price` float NOT NULL,
  `rating` float DEFAULT NULL,
  `amount` int DEFAULT NULL,
  `name` varchar(20) COLLATE utf8mb3_bin DEFAULT NULL,
  PRIMARY KEY (`item_id`),
  CONSTRAINT `mice_ibfk_1` FOREIGN KEY (`item_id`) REFERENCES `items` (`item_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS microphones;
CREATE TABLE `microphones` (
  `item_id` int NOT NULL AUTO_INCREMENT,
  `params` varchar(20) COLLATE utf8mb3_bin DEFAULT NULL,
  `price` float NOT NULL,
  `rating` float DEFAULT NULL,
  `amount` int DEFAULT NULL,
  `name` char(128) COLLATE utf8mb3_bin DEFAULT NULL,
  PRIMARY KEY (`item_id`),
  CONSTRAINT `microphones_ibfk_1` FOREIGN KEY (`item_id`) REFERENCES `items` (`item_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS orders;
CREATE TABLE `orders` (
  `order_datetime` datetime NOT NULL DEFAULT '2023-12-12 00:00:00',
  `id_order` int NOT NULL,
  `order_sum` float NOT NULL,
  `order_status` int NOT NULL,
  `client_id` int NOT NULL,
  `services_type` int DEFAULT NULL,
  `client_address` varchar(128) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL,
  `delivery_type` int DEFAULT NULL,
  `master_id` int DEFAULT NULL,
  `pick_up_point_id` int DEFAULT NULL,
  `courier_id` int DEFAULT NULL,
  PRIMARY KEY (`id_order`),
  KEY `R_37` (`client_id`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`client_id`) REFERENCES `client` (`client_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS pc_builder;
CREATE TABLE `pc_builder` (
  `master_id` int NOT NULL,
  `rating` float DEFAULT NULL,
  `service_id` int DEFAULT NULL,
  `name` varchar(255) COLLATE utf8mb3_bin NOT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`master_id`),
  KEY `R_94` (`service_id`),
  CONSTRAINT `pc_builder_ibfk_1` FOREIGN KEY (`service_id`) REFERENCES `services` (`services_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS pc_cleaner;
CREATE TABLE `pc_cleaner` (
  `master_id` int NOT NULL,
  `rating` tinyint(1) DEFAULT NULL,
  `service_id` int DEFAULT NULL,
  `name` varchar(255) COLLATE utf8mb3_bin NOT NULL,
  `time` datetime NOT NULL,
  PRIMARY KEY (`master_id`),
  KEY `R_93` (`service_id`),
  CONSTRAINT `pc_cleaner_ibfk_1` FOREIGN KEY (`service_id`) REFERENCES `services` (`services_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS pc_master;
CREATE TABLE `pc_master` (
  `master_id` char(128) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL,
  `rating` float DEFAULT NULL,
  `service_id` int DEFAULT NULL,
  `name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL,
  `time` datetime NOT NULL DEFAULT '2023-12-12 00:00:00',
  PRIMARY KEY (`master_id`),
  KEY `R_92` (`service_id`),
  CONSTRAINT `pc_master_ibfk_1` FOREIGN KEY (`service_id`) REFERENCES `services` (`services_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS pick_up_point;
CREATE TABLE `pick_up_point` (
  `id_point` int NOT NULL AUTO_INCREMENT,
  `open_hours` datetime NOT NULL DEFAULT '2023-12-12 00:00:00',
  `address_point` varchar(100) COLLATE utf8mb3_bin DEFAULT NULL,
  `id_order` int DEFAULT NULL,
  PRIMARY KEY (`id_point`),
  KEY `R_44` (`id_order`),
  CONSTRAINT `pick_up_point_ibfk_1` FOREIGN KEY (`id_order`) REFERENCES `orders` (`id_order`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS services;
CREATE TABLE `services` (
  `services_type` int NOT NULL,
  `price` float DEFAULT NULL,
  PRIMARY KEY (`services_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS ssd;
CREATE TABLE `ssd` (
  `item_id` int NOT NULL AUTO_INCREMENT,
  `params` varchar(20) COLLATE utf8mb3_bin DEFAULT NULL,
  `price` float NOT NULL,
  `rating` float DEFAULT NULL,
  `amount` int DEFAULT NULL,
  `name` varchar(20) COLLATE utf8mb3_bin DEFAULT NULL,
  PRIMARY KEY (`item_id`),
  CONSTRAINT `ssd_ibfk_1` FOREIGN KEY (`item_id`) REFERENCES `items` (`item_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS storage;
CREATE TABLE `storage` (
  `storage_id` int NOT NULL,
  `address` varchar(20) COLLATE utf8mb3_bin DEFAULT NULL,
  PRIMARY KEY (`storage_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS techsupp;
CREATE TABLE `techsupp` (
  `support_id` int NOT NULL,
  `datetime_tech_supp` datetime NOT NULL DEFAULT '2023-12-12 00:00:00',
  `client_id` int DEFAULT NULL,
  `question` text COLLATE utf8mb3_bin,
  PRIMARY KEY (`support_id`),
  KEY `R_66` (`client_id`),
  CONSTRAINT `techsupp_ibfk_1` FOREIGN KEY (`client_id`) REFERENCES `client` (`client_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

DROP TABLE IF EXISTS tracks;
CREATE TABLE `tracks` (
  `track_id` int NOT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `time_to_deliver` datetime NOT NULL DEFAULT '2023-12-12 00:00:00',
  `id_point` int DEFAULT NULL,
  PRIMARY KEY (`track_id`),
  KEY `R_86` (`id_point`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

INSERT INTO auth_group(id,name) VALUES('4','\'Gosha_admin\''),('3','\'Sanya_admin\''),('2','\'Vlad_admin\'');

INSERT INTO auth_group_permissions(id,group_id,permission_id) VALUES('193','2','61'),('194','2','62'),('195','2','63'),('196','2','64'),('161','2','129'),('162','2','130'),('163','2','131'),('164','2','132'),('165','2','133'),('166','2','134'),('167','2','135'),('168','2','136'),('169','2','137'),('170','2','138'),('171','2','139'),('172','2','140'),('173','2','141'),('174','2','142'),('175','2','143'),('176','2','144'),('177','2','145'),('178','2','146'),('179','2','147'),('180','2','148'),('181','2','149'),('182','2','150'),('183','2','151'),('184','2','152'),('185','2','153'),('186','2','154'),('187','2','155'),('188','2','156'),('189','2','157'),('190','2','158'),('191','2','159'),('192','2','160'),('198','3','25'),('199','3','26'),('200','3','27'),('201','3','28'),('202','3','45'),('203','3','46'),('204','3','47'),('205','3','48'),('206','3','65'),('207','3','66'),('208','3','67'),('209','3','68'),('210','3','73'),('211','3','74'),('212','3','75'),('213','3','76'),('214','3','89'),('215','3','90'),('216','3','91'),('217','3','92'),('218','3','93'),('219','3','94'),('220','3','95'),('221','3','96'),('222','3','97'),('223','3','98'),('224','3','99'),('225','3','100'),('226','3','101'),('227','3','102'),('228','3','103'),('229','3','104'),('230','3','121'),('231','3','122'),('232','3','123'),('233','3','124'),('234','3','125'),('235','3','126'),('236','3','127'),('197','3','128'),('245','4','49'),('246','4','50'),('247','4','51'),('248','4','52'),('249','4','53'),('250','4','54'),('251','4','55'),('252','4','56'),('253','4','77'),('254','4','78'),('255','4','79'),('256','4','80'),('257','4','105'),('258','4','106'),('259','4','107'),('260','4','108'),('261','4','109'),('262','4','110'),('263','4','111'),('264','4','112'),('237','4','161'),('238','4','162'),('239','4','163'),('240','4','164'),('241','4','165'),('242','4','166'),('243','4','167'),('244','4','168');

INSERT INTO auth_permission(id,name,content_type_id,codename) VALUES('1','\'Can add log entry\'','1','\'add_logentry\''),('2','\'Can change log entry\'','1','\'change_logentry\''),('3','\'Can delete log entry\'','1','\'delete_logentry\''),('4','\'Can view log entry\'','1','\'view_logentry\''),('5','\'Can add permission\'','2','\'add_permission\''),('6','\'Can change permission\'','2','\'change_permission\''),('7','\'Can delete permission\'','2','\'delete_permission\''),('8','\'Can view permission\'','2','\'view_permission\''),('9','\'Can add group\'','3','\'add_group\''),('10','\'Can change group\'','3','\'change_group\''),('11','\'Can delete group\'','3','\'delete_group\''),('12','\'Can view group\'','3','\'view_group\''),('13','\'Can add user\'','4','\'add_user\''),('14','\'Can change user\'','4','\'change_user\''),('15','\'Can delete user\'','4','\'delete_user\''),('16','\'Can view user\'','4','\'view_user\''),('17','\'Can add content type\'','5','\'add_contenttype\''),('18','\'Can change content type\'','5','\'change_contenttype\''),('19','\'Can delete content type\'','5','\'delete_contenttype\''),('20','\'Can view content type\'','5','\'view_contenttype\''),('21','\'Can add session\'','6','\'add_session\''),('22','\'Can change session\'','6','\'change_session\''),('23','\'Can delete session\'','6','\'delete_session\''),('24','\'Can view session\'','6','\'view_session\''),('25','\'Can add cars\'','7','\'add_cars\''),('26','\'Can change cars\'','7','\'change_cars\''),('27','\'Can delete cars\'','7','\'delete_cars\''),('28','\'Can view cars\'','7','\'view_cars\''),('29','\'Can add client comment courier\'','8','\'add_clientcommentcourier\''),('30','\'Can change client comment courier\'','8','\'change_clientcommentcourier\''),('31','\'Can delete client comment courier\'','8','\'delete_clientcommentcourier\''),('32','\'Can view client comment courier\'','8','\'view_clientcommentcourier\''),('33','\'Can add client comment devices\'','9','\'add_clientcommentdevices\''),('34','\'Can change client comment devices\'','9','\'change_clientcommentdevices\''),('35','\'Can delete client comment devices\'','9','\'delete_clientcommentdevices\''),('36','\'Can view client comment devices\'','9','\'view_clientcommentdevices\''),('37','\'Can add client comment master\'','10','\'add_clientcommentmaster\''),('38','\'Can change client comment master\'','10','\'change_clientcommentmaster\''),('39','\'Can delete client comment master\'','10','\'delete_clientcommentmaster\''),('40','\'Can view client comment master\'','10','\'view_clientcommentmaster\''),('41','\'Can add client comments operator\'','11','\'add_clientcommentsoperator\''),('42','\'Can change client comments operator\'','11','\'change_clientcommentsoperator\''),('43','\'Can delete client comments operator\'','11','\'delete_clientcommentsoperator\''),('44','\'Can view client comments operator\'','11','\'view_clientcommentsoperator\''),('45','\'Can add couriers\'','12','\'add_couriers\''),('46','\'Can change couriers\'','12','\'change_couriers\''),('47','\'Can delete couriers\'','12','\'delete_couriers\''),('48','\'Can view couriers\'','12','\'view_couriers\''),('49','\'Can add industries\'','13','\'add_industries\''),('50','\'Can change industries\'','13','\'change_industries\''),('51','\'Can delete industries\'','13','\'delete_industries\''),('52','\'Can view industries\'','13','\'view_industries\''),('53','\'Can add invoices\'','14','\'add_invoices\''),('54','\'Can change invoices\'','14','\'change_invoices\''),('55','\'Can delete invoices\'','14','\'delete_invoices\''),('56','\'Can view invoices\'','14','\'view_invoices\''),('57','\'Can add operators\'','15','\'add_operators\''),('58','\'Can change operators\'','15','\'change_operators\''),('59','\'Can delete operators\'','15','\'delete_operators\''),('60','\'Can view operators\'','15','\'view_operators\''),('61','\'Can add orders\'','16','\'add_orders\''),('62','\'Can change orders\'','16','\'change_orders\''),('63','\'Can delete orders\'','16','\'delete_orders\''),('64','\'Can view orders\'','16','\'view_orders\''),('65','\'Can add pick up point\'','17','\'add_pickuppoint\''),('66','\'Can change pick up point\'','17','\'change_pickuppoint\''),('67','\'Can delete pick up point\'','17','\'delete_pickuppoint\''),('68','\'Can view pick up point\'','17','\'view_pickuppoint\''),('69','\'Can add providers\'','18','\'add_providers\''),('70','\'Can change providers\'','18','\'change_providers\''),('71','\'Can delete providers\'','18','\'delete_providers\''),('72','\'Can view providers\'','18','\'view_providers\''),('73','\'Can add services\'','19','\'add_services\''),('74','\'Can change services\'','19','\'change_services\''),('75','\'Can delete services\'','19','\'delete_services\''),('76','\'Can view services\'','19','\'view_services\''),('77','\'Can add storage\'','20','\'add_storage\''),('78','\'Can change storage\'','20','\'change_storage\''),('79','\'Can delete storage\'','20','\'delete_storage\''),('80','\'Can view storage\'','20','\'view_storage\''),('81','\'Can add techsupp\'','21','\'add_techsupp\''),('82','\'Can change techsupp\'','21','\'change_techsupp\''),('83','\'Can delete techsupp\'','21','\'delete_techsupp\''),('84','\'Can view techsupp\'','21','\'view_techsupp\''),('85','\'Can add tracks\'','22','\'add_tracks\''),('86','\'Can change tracks\'','22','\'change_tracks\''),('87','\'Can delete tracks\'','22','\'delete_tracks\''),('88','\'Can view tracks\'','22','\'view_tracks\''),('89','\'Can add builder status\'','23','\'add_builderstatus\''),('90','\'Can change builder status\'','23','\'change_builderstatus\''),('91','\'Can delete builder status\'','23','\'delete_builderstatus\''),('92','\'Can view builder status\'','23','\'view_builderstatus\''),('93','\'Can add pc builder\'','24','\'add_pcbuilder\''),('94','\'Can change pc builder\'','24','\'change_pcbuilder\''),('95','\'Can delete pc builder\'','24','\'delete_pcbuilder\''),('96','\'Can view pc builder\'','24','\'view_pcbuilder\''),('97','\'Can add pc cleaner\'','25','\'add_pccleaner\''),('98','\'Can change pc cleaner\'','25','\'change_pccleaner\''),('99','\'Can delete pc cleaner\'','25','\'delete_pccleaner\''),('100','\'Can view pc cleaner\'','25','\'view_pccleaner\''),('101','\'Can add cleaner status\'','26','\'add_cleanerstatus\''),('102','\'Can change cleaner status\'','26','\'change_cleanerstatus\''),('103','\'Can delete cleaner status\'','26','\'delete_cleanerstatus\''),('104','\'Can view cleaner status\'','26','\'view_cleanerstatus\''),('105','\'Can add indtracks status\'','27','\'add_indtracksstatus\''),('106','\'Can change indtracks status\'','27','\'change_indtracksstatus\''),('107','\'Can delete indtracks status\'','27','\'delete_indtracksstatus\''),('108','\'Can view indtracks status\'','27','\'view_indtracksstatus\''),('109','\'Can add indtracks\'','28','\'add_indtracks\''),('110','\'Can change indtracks\'','28','\'change_indtracks\''),('111','\'Can delete indtracks\'','28','\'delete_indtracks\''),('112','\'Can view indtracks\'','28','\'view_indtracks\''),('113','\'Can add client\'','29','\'add_client\''),('114','\'Can change client\'','29','\'change_client\''),('115','\'Can delete client\'','29','\'delete_client\''),('116','\'Can view client\'','29','\'view_client\''),('117','\'Can add login\'','30','\'add_login\''),('118','\'Can change login\'','30','\'change_login\''),('119','\'Can delete login\'','30','\'delete_login\''),('120','\'Can view login\'','30','\'view_login\''),('121','\'Can add master status\'','31','\'add_masterstatus\''),('122','\'Can change master status\'','31','\'change_masterstatus\''),('123','\'Can delete master status\'','31','\'delete_masterstatus\''),('124','\'Can view master status\'','31','\'view_masterstatus\''),('125','\'Can add pc master\'','32','\'add_pcmaster\''),('126','\'Can change pc master\'','32','\'change_pcmaster\''),('127','\'Can delete pc master\'','32','\'delete_pcmaster\''),('128','\'Can view pc master\'','32','\'view_pcmaster\''),('129','\'Can add microphones\'','33','\'add_microphones\''),('130','\'Can change microphones\'','33','\'change_microphones\''),('131','\'Can delete microphones\'','33','\'delete_microphones\''),('132','\'Can view microphones\'','33','\'view_microphones\''),('133','\'Can add items\'','34','\'add_items\''),('134','\'Can change items\'','34','\'change_items\''),('135','\'Can delete items\'','34','\'delete_items\''),('136','\'Can view items\'','34','\'view_items\''),('137','\'Can add ssd\'','35','\'add_ssd\''),('138','\'Can change ssd\'','35','\'change_ssd\''),('139','\'Can delete ssd\'','35','\'delete_ssd\''),('140','\'Can view ssd\'','35','\'view_ssd\''),('141','\'Can add flash\'','36','\'add_flash\''),('142','\'Can change flash\'','36','\'change_flash\''),('143','\'Can delete flash\'','36','\'delete_flash\''),('144','\'Can view flash\'','36','\'view_flash\''),('145','\'Can add keyboards\'','37','\'add_keyboards\''),('146','\'Can change keyboards\'','37','\'change_keyboards\''),('147','\'Can delete keyboards\'','37','\'delete_keyboards\''),('148','\'Can view keyboards\'','37','\'view_keyboards\''),('149','\'Can add mice\'','38','\'add_mice\''),('150','\'Can change mice\'','38','\'change_mice\''),('151','\'Can delete mice\'','38','\'delete_mice\''),('152','\'Can view mice\'','38','\'view_mice\''),('153','\'Can add hdd\'','39','\'add_hdd\''),('154','\'Can change hdd\'','39','\'change_hdd\''),('155','\'Can delete hdd\'','39','\'delete_hdd\''),('156','\'Can view hdd\'','39','\'view_hdd\''),('157','\'Can add items for order\'','40','\'add_itemsfororder\''),('158','\'Can change items for order\'','40','\'change_itemsfororder\''),('159','\'Can delete items for order\'','40','\'delete_itemsfororder\''),('160','\'Can view items for order\'','40','\'view_itemsfororder\''),('161','\'Can add invoice items\'','41','\'add_invoiceitems\''),('162','\'Can change invoice items\'','41','\'change_invoiceitems\''),('163','\'Can delete invoice items\'','41','\'delete_invoiceitems\''),('164','\'Can view invoice items\'','41','\'view_invoiceitems\''),('165','\'Can add industry items\'','42','\'add_industryitems\''),('166','\'Can change industry items\'','42','\'change_industryitems\''),('167','\'Can delete industry items\'','42','\'delete_industryitems\''),('168','\'Can view industry items\'','42','\'view_industryitems\'');

INSERT INTO auth_user(id,password,last_login,is_superuser,username,first_name,last_name,email,is_staff,is_active,date_joined) VALUES('1','\'pbkdf2_sha256$600000$lXKf1WLmqbYefLDY0l1Q9D$K06NvNHlFTL0NiunSg8oqyCSbBvsYgJSHq76fy3382A=\'','\'2023-12-15 05:46:11.742090\'','1','\'admin\'','\'\'','\'\'','\'vlunku@gmail.com\'','1','1','\'2023-11-21 01:06:28.388386\''),('5','\'pbkdf2_sha256$600000$FooqSeDJiJPc2MaCuFlT95$s7R/Z+jbWmm5UvJDDlHOPMd2Ktam3ei0rtxW9gJYuR4=\'','\'2023-12-15 05:41:24.923341\'','0','\'Gosha\'','\'\'','\'\'','\'\'','1','1','\'2023-12-15 05:40:49.000000\''),('6','\'pbkdf2_sha256$600000$v8IgCjctwSS9rEqtcNGiXx$oNhaX+RsXeOA/8XgBkmijdnNv0rrWeqKkOVaGjWhFvk=\'','\'2023-12-15 05:43:19.235800\'','0','\'Vladik\'','\'\'','\'\'','\'\'','1','1','\'2023-12-15 05:42:07.000000\''),('7','\'pbkdf2_sha256$600000$VQEsIGSvpA3exlfaHe71mE$g9MaGxneJes2+lWRwqV1S9ddlocENdJikdv9+iWiXjU=\'','\'2023-12-15 05:42:53.676951\'','0','\'Sanya\'','\'\'','\'\'','\'\'','1','1','\'2023-12-15 05:42:31.000000\'');

INSERT INTO auth_user_groups(id,user_id,group_id) VALUES('3','5','4'),('4','6','2'),('5','7','3');


INSERT INTO builder_status(master_id,status,time) VALUES('1','1','\'2023-12-14\''),('2','1','\'2023-12-15\''),('3','1','\'2023-12-15\'');

INSERT INTO cars(car_id,status,courier_id) VALUES('1','0','NULL');

INSERT INTO cleaner_status(status,time,master_id) VALUES('1','\'2023-12-15\'','1');

INSERT INTO client(client_id,full_name,phone_number,client_email,address) VALUES('1','\'Korneev Alexandr\'','\'01\'','\'james.howlett.work10@gmail.com\'','\'ул.Пушкина д.Колотушкина\''),('2','\'Lundyshev Vladislav\'','\'02\'','\'aaa@mail.ru\'','\'aaa\''),('3','\'Konkin George\'','\'03\'','\'bbb@yandex.com\'','\'bbb\''),('4','\'Vlad\'','\'14124124123\'','\'eqweqw@ss.com\'','\'11111aaaa\''),('5','\'Vlad\'','\'asdasdasdas\'','\'jameshowlett993@yandex.ru\'','\'GTA for USA\''),('6','\'Vlada\'','\'+79771295752\'','\'jameshowlett993@yandex.ru\'','\'GTA for USA\''),('7','\'HUYLAN\'','\'+79867453513\'','\'bio-apparation@mail.ru\'','\'zzzxxxccc\''),('8','\'GAVNO\'','\'+73011234567\'','\'jameshowlett993@yandex.ru\'','\'GTA for USA\''),('9','\'GAVNO\'','\'+73011234567\'','\'jameshowlett993@yandex.ru\'','\'GTA for USA\''),('10','\'Vladik\'','\'+79867453513\'','\'jameshowlett993@yandex.ru\'','\'GTA for USA\'');





INSERT INTO django_admin_log(id,action_time,object_id,object_repr,action_flag,change_message,content_type_id,user_id) VALUES('1','\'2023-11-21 01:18:37.064904\'','X\'31\'','\'Client object (1)\'','1','X\'5b7b226164646564223a207b7d7d5d\'','29','1'),('2','\'2023-11-21 01:18:55.240180\'','X\'31\'','\'Client object (1)\'','3','X\'\'','29','1'),('3','\'2023-11-21 01:23:10.042548\'','X\'31\'','\'Client object (1)\'','1','X\'5b7b226164646564223a207b7d7d5d\'','29','1'),('4','\'2023-11-21 10:07:29.615915\'','X\'32\'','\'Client object (2)\'','1','X\'5b7b226164646564223a207b7d7d5d\'','29','1'),('5','\'2023-11-21 11:29:36.791434\'','X\'32\'','\'James\'','1','X\'5b7b226164646564223a207b7d7d5d\'','4','1'),('6','\'2023-11-21 11:30:31.210989\'','X\'32\'','\'James\'','2','X\'5b7b226368616e676564223a207b226669656c6473223a205b224669727374206e616d65222c20224c617374206e616d65222c2022456d61696c2061646472657373225d7d7d5d\'','4','1'),('7','\'2023-11-21 22:29:32.850614\'','X\'31\'','\'Services object (1)\'','1','X\'5b7b226164646564223a207b7d7d5d\'','19','1'),('8','\'2023-11-21 22:29:43.063427\'','X\'31\'','\'Services object (1)\'','2','X\'5b5d\'','19','1'),('9','\'2023-11-21 22:29:47.686467\'','X\'32\'','\'Services object (2)\'','1','X\'5b7b226164646564223a207b7d7d5d\'','19','1'),('10','\'2023-11-21 22:29:51.336841\'','X\'33\'','\'Services object (3)\'','1','X\'5b7b226164646564223a207b7d7d5d\'','19','1'),('11','\'2023-11-21 22:31:10.355442\'','X\'31\'','\'PcBuilder object (1)\'','1','X\'5b7b226164646564223a207b7d7d5d\'','24','1'),('12','\'2023-12-12 17:30:33.206693\'','X\'31\'','\'Group_1\'','1','X\'5b7b226164646564223a207b7d7d5d\'','3','1'),('13','\'2023-12-12 17:33:51.035549\'','X\'33\'','\'Vlad\'','1','X\'5b7b226164646564223a207b7d7d5d\'','4','1'),('14','\'2023-12-12 17:34:21.107337\'','X\'33\'','\'Vlad\'','2','X\'5b7b226368616e676564223a207b226669656c6473223a205b2247726f757073225d7d7d5d\'','4','1'),('15','\'2023-12-12 17:38:56.126118\'','X\'34\'','\'Vlad1\'','1','X\'5b7b226164646564223a207b7d7d5d\'','4','1'),('16','\'2023-12-12 17:39:13.977220\'','X\'34\'','\'Vlad1\'','2','X\'5b7b226368616e676564223a207b226669656c6473223a205b224669727374206e616d65222c20224c617374206e616d65222c2022456d61696c2061646472657373222c202247726f757073225d7d7d5d\'','4','1'),('17','\'2023-12-12 17:40:59.767328\'','X\'34\'','\'Vlad1\'','2','X\'5b7b226368616e676564223a207b226669656c6473223a205b22537461666620737461747573225d7d7d5d\'','4','1'),('18','\'2023-12-12 17:55:59.272215\'','X\'31\'','\'Group_1\'','2','X\'5b7b226368616e676564223a207b226669656c6473223a205b225065726d697373696f6e73225d7d7d5d\'','3','1'),('19','\'2023-12-12 17:59:34.457335\'','X\'31\'','\'Invoices object (1)\'','1','X\'5b7b226164646564223a207b7d7d5d\'','14','1'),('20','\'2023-12-12 18:00:50.315268\'','X\'31\'','\'Indtracks object (1)\'','1','X\'5b7b226164646564223a207b7d7d5d\'','28','1'),('21','\'2023-12-12 18:01:04.057164\'','X\'31\'','\'Invoices object (1)\'','2','X\'5b7b226368616e676564223a207b226669656c6473223a205b22496e6420747261636b222c2022496e647573747279225d7d7d5d\'','14','1'),('22','\'2023-12-12 18:01:17.691190\'','X\'31\'','\'Invoices object (1)\'','2','X\'5b5d\'','14','1'),('23','\'2023-12-15 03:26:34.232108\'','X\'32\'','\'Invoices object (2)\'','1','X\'5b7b226164646564223a207b7d7d5d\'','14','1'),('24','\'2023-12-15 03:27:06.839089\'','X\'31\'','\'HDD_4\'','1','X\'5b7b226164646564223a207b7d7d5d\'','41','1'),('25','\'2023-12-15 03:55:09.118810\'','X\'31\'','\'Заказ номер 1\'','2','X\'5b7b226368616e676564223a207b226669656c6473223a205b224f7264657220737461747573222c202253657276696365732074797065222c20224d6173746572206964222c20225069636b20757020706f696e74206964225d7d7d5d\'','16','1'),('26','\'2023-12-15 03:57:40.643970\'','X\'31\'','\'Заказ номер 1\'','2','X\'5b7b226368616e676564223a207b226669656c6473223a205b2253657276696365732074797065225d7d7d5d\'','16','1'),('27','\'2023-12-15 03:57:45.879392\'','X\'31\'','\'Заказ номер 1\'','2','X\'5b5d\'','16','1'),('28','\'2023-12-15 03:57:49.978605\'','X\'31\'','\'Заказ номер 1\'','2','X\'5b7b226368616e676564223a207b226669656c6473223a205b2253657276696365732074797065225d7d7d5d\'','16','1'),('29','\'2023-12-15 03:59:19.420674\'','X\'33\'','\'Накладная номер 3\'','1','X\'5b7b226164646564223a207b7d7d5d\'','14','1'),('30','\'2023-12-15 04:03:22.865651\'','X\'34\'','\'Microphone RTX50080 количеством 500 из Накладная номер 3\'','1','X\'5b7b226164646564223a207b7d7d5d\'','41','1'),('31','\'2023-12-15 04:05:18.944299\'','X\'34\'','\'Microphone RTX50080 количеством 500 из Накладная номер 3\'','2','X\'5b7b226368616e676564223a207b226669656c6473223a205b225072696365225d7d7d5d\'','41','1'),('32','\'2023-12-15 04:18:15.523884\'','X\'32\'','\'Склад номер 2\'','1','X\'5b7b226164646564223a207b7d7d5d\'','20','1'),('33','\'2023-12-15 04:18:19.793041\'','X\'33\'','\'Предмет Microphone номер 3\'','1','X\'5b7b226164646564223a207b7d7d5d\'','34','1'),('34','\'2023-12-15 04:18:40.760527\'','X\'33\'','\'MIC_1 Стоимость: 123.0 Рейтинг: 5.0 Количество: 20\'','1','X\'5b7b226164646564223a207b7d7d5d\'','33','1'),('35','\'2023-12-15 04:21:55.622733\'','X\'32\'','\'Мастер номер 2\'','1','X\'5b7b226164646564223a207b7d7d5d\'','32','1'),('36','\'2023-12-15 04:31:25.412613\'','X\'34\'','\'Предмет Keyboard номер 4\'','1','X\'5b7b226164646564223a207b7d7d5d\'','34','1'),('37','\'2023-12-15 04:31:53.513168\'','X\'34\'','\'Keyboard Стоимость: 123.0 Рейтинг: 2.0 Количество: 3\'','1','X\'5b7b226164646564223a207b7d7d5d\'','37','1'),('38','\'2023-12-15 04:35:23.277204\'','X\'33\'','\'Склад номер 3\'','1','X\'5b7b226164646564223a207b7d7d5d\'','20','1'),('39','\'2023-12-15 04:35:28.101679\'','X\'35\'','\'Предмет Keyboard номер 5\'','1','X\'5b7b226164646564223a207b7d7d5d\'','34','1'),('40','\'2023-12-15 04:36:04.957088\'','X\'35\'','\'Key1 Стоимость: 123.0 Рейтинг: 5.0 Количество: 1231\'','1','X\'5b7b226164646564223a207b7d7d5d\'','37','1'),('41','\'2023-12-15 04:45:17.948890\'','X\'33\'','\'Мастер номер 3\'','1','X\'5b7b226164646564223a207b7d7d5d\'','32','1'),('42','\'2023-12-15 04:45:38.596250\'','X\'32\'','\'Мастер номер 2\'','3','X\'\'','32','1'),('43','\'2023-12-15 04:46:04.110788\'','X\'32\'','\'Мастер номер 2\'','1','X\'5b7b226164646564223a207b7d7d5d\'','32','1'),('44','\'2023-12-15 05:36:40.534433\'','X\'31\'','\'Group_1\'','3','X\'\'','3','1'),('45','\'2023-12-15 05:37:57.176436\'','X\'32\'','\'Vlad_admin\'','1','X\'5b7b226164646564223a207b7d7d5d\'','3','1'),('46','\'2023-12-15 05:39:23.724110\'','X\'33\'','\'Sanya_admin\'','1','X\'5b7b226164646564223a207b7d7d5d\'','3','1'),('47','\'2023-12-15 05:40:04.518718\'','X\'34\'','\'Gosha_admin\'','1','X\'5b7b226164646564223a207b7d7d5d\'','3','1'),('48','\'2023-12-15 05:40:17.255770\'','X\'32\'','\'James\'','3','X\'\'','4','1'),('49','\'2023-12-15 05:40:17.260768\'','X\'33\'','\'Vlad\'','3','X\'\'','4','1'),('50','\'2023-12-15 05:40:17.264767\'','X\'34\'','\'Vlad1\'','3','X\'\'','4','1'),('51','\'2023-12-15 05:40:50.753896\'','X\'35\'','\'Gosha\'','1','X\'5b7b226164646564223a207b7d7d5d\'','4','1'),('52','\'2023-12-15 05:41:04.016894\'','X\'35\'','\'Gosha\'','2','X\'5b7b226368616e676564223a207b226669656c6473223a205b22537461666620737461747573222c202247726f757073222c20224c617374206c6f67696e225d7d7d5d\'','4','1'),('53','\'2023-12-15 05:42:08.590014\'','X\'36\'','\'Vladik\'','1','X\'5b7b226164646564223a207b7d7d5d\'','4','1'),('54','\'2023-12-15 05:42:13.754421\'','X\'36\'','\'Vladik\'','2','X\'5b7b226368616e676564223a207b226669656c6473223a205b2247726f757073222c20224c617374206c6f67696e225d7d7d5d\'','4','1'),('55','\'2023-12-15 05:42:22.253752\'','X\'36\'','\'Vladik\'','2','X\'5b7b226368616e676564223a207b226669656c6473223a205b22537461666620737461747573225d7d7d5d\'','4','1'),('56','\'2023-12-15 05:42:32.681484\'','X\'37\'','\'Sanya\'','1','X\'5b7b226164646564223a207b7d7d5d\'','4','1'),('57','\'2023-12-15 05:42:38.255242\'','X\'37\'','\'Sanya\'','2','X\'5b7b226368616e676564223a207b226669656c6473223a205b22537461666620737461747573222c202247726f757073222c20224c617374206c6f67696e225d7d7d5d\'','4','1');

INSERT INTO django_content_type(id,app_label,model) VALUES('1','\'admin\'','\'logentry\''),('3','\'auth\'','\'group\''),('2','\'auth\'','\'permission\''),('4','\'auth\'','\'user\''),('5','\'contenttypes\'','\'contenttype\''),('23','\'polls\'','\'builderstatus\''),('7','\'polls\'','\'cars\''),('26','\'polls\'','\'cleanerstatus\''),('29','\'polls\'','\'client\''),('8','\'polls\'','\'clientcommentcourier\''),('9','\'polls\'','\'clientcommentdevices\''),('10','\'polls\'','\'clientcommentmaster\''),('11','\'polls\'','\'clientcommentsoperator\''),('12','\'polls\'','\'couriers\''),('36','\'polls\'','\'flash\''),('39','\'polls\'','\'hdd\''),('28','\'polls\'','\'indtracks\''),('27','\'polls\'','\'indtracksstatus\''),('13','\'polls\'','\'industries\''),('42','\'polls\'','\'industryitems\''),('41','\'polls\'','\'invoiceitems\''),('14','\'polls\'','\'invoices\''),('34','\'polls\'','\'items\''),('40','\'polls\'','\'itemsfororder\''),('37','\'polls\'','\'keyboards\''),('30','\'polls\'','\'login\''),('31','\'polls\'','\'masterstatus\''),('38','\'polls\'','\'mice\''),('33','\'polls\'','\'microphones\''),('15','\'polls\'','\'operators\''),('16','\'polls\'','\'orders\''),('24','\'polls\'','\'pcbuilder\''),('25','\'polls\'','\'pccleaner\''),('32','\'polls\'','\'pcmaster\''),('17','\'polls\'','\'pickuppoint\''),('18','\'polls\'','\'providers\''),('19','\'polls\'','\'services\''),('35','\'polls\'','\'ssd\''),('20','\'polls\'','\'storage\''),('21','\'polls\'','\'techsupp\''),('22','\'polls\'','\'tracks\''),('6','\'sessions\'','\'session\'');

INSERT INTO django_migrations(id,app,name,applied) VALUES('1','\'contenttypes\'','\'0001_initial\'','\'2023-11-21 00:33:45.991582\''),('2','\'auth\'','\'0001_initial\'','\'2023-11-21 00:33:47.566585\''),('3','\'admin\'','\'0001_initial\'','\'2023-11-21 00:33:47.865489\''),('4','\'admin\'','\'0002_logentry_remove_auto_add\'','\'2023-11-21 00:33:47.880485\''),('5','\'admin\'','\'0003_logentry_add_action_flag_choices\'','\'2023-11-21 00:33:47.897479\''),('6','\'contenttypes\'','\'0002_remove_content_type_name\'','\'2023-11-21 00:33:48.082420\''),('7','\'auth\'','\'0002_alter_permission_name_max_length\'','\'2023-11-21 00:33:48.225375\''),('8','\'auth\'','\'0003_alter_user_email_max_length\'','\'2023-11-21 00:33:48.365836\''),('9','\'auth\'','\'0004_alter_user_username_opts\'','\'2023-11-21 00:33:48.381831\''),('10','\'auth\'','\'0005_alter_user_last_login_null\'','\'2023-11-21 00:33:48.487797\''),('11','\'auth\'','\'0006_require_contenttypes_0002\'','\'2023-11-21 00:33:48.496794\''),('12','\'auth\'','\'0007_alter_validators_add_error_messages\'','\'2023-11-21 00:33:48.515788\''),('13','\'auth\'','\'0008_alter_user_username_max_length\'','\'2023-11-21 00:33:48.645747\''),('14','\'auth\'','\'0009_alter_user_last_name_max_length\'','\'2023-11-21 00:33:48.780704\''),('15','\'auth\'','\'0010_alter_group_name_max_length\'','\'2023-11-21 00:33:48.910662\''),('16','\'auth\'','\'0011_update_proxy_permissions\'','\'2023-11-21 00:33:48.929656\''),('17','\'auth\'','\'0012_alter_user_first_name_max_length\'','\'2023-11-21 00:33:49.062614\''),('18','\'sessions\'','\'0001_initial\'','\'2023-11-21 00:33:49.142589\''),('19','\'polls\'','\'0001_initial\'','\'2023-11-21 01:03:43.606792\'');

INSERT INTO django_session(session_key,session_data,expire_date) VALUES('\'0lii8g7h177lbms1nybigzv1ykp9zxqs\'','X\'2e654a78566a45454f7769415152655f4332684267706852637576634d5a494242716f596d7056305a3736354e75744474662d5f396c776930725456736e5a63775a5845575770782d74306a70775730482d5537744e7373307433575a6f747756656441757233506d352d56775f77347139667174585237596a533470786459434a4552446746794b3575494141627a504a526b624c61477a6d516d55527139484132684244537a65483956304e78773a31724479444c3a7455674c4567326642783646694566656d4a514d4f69694a366770506f6132414642305244673958364338\'','\'2023-12-29 05:46:11.746089\'');

INSERT INTO flash(item_id,params,price,rating,amount,name,type) VALUES('1','\'asdasd\'','123','3.5','76','\'Flash1\'','\'Flash\'');

INSERT INTO hdd(item_id,params,price,rating,amount,name,type) VALUES('1','\'aaaa\'','12','3','30','\'HDD_1\'','\'HDD\'');

INSERT INTO indtracks(ind_track_id,status,time_to_deliver) VALUES('1','0','\'2023-12-12\'');


INSERT INTO industries(industry_id,industry_address,industry_name) VALUES('1','\'qwerty\'','\'qwerty\'');

INSERT INTO invoice_items(item_id,item_name,params,type,amount,invoice_id,price) VALUES('1','\'HDD_4\'','\'oidfguheu\'','\'Hdd\'','123','2','0'),('4','\'Microphone RTX50080\'','\'krutoi\'','\'Microphone\'','500','3','500000');

INSERT INTO invoices(invoice_id,storage_id,ind_track_id,price,industry_id,invoices_date) VALUES('1','1','1','11','1','\'2023-12-12 00:00:00\''),('2','1','1','NULL','1','\'2023-12-15 00:26:33\''),('3','1','1','NULL','1','\'2023-12-15 00:58:59\'');

INSERT INTO items(item_id,item_name,storage_id,type) VALUES('1','\'HDD_1\'','1','\'HDD\''),('2','\'Flash1\'','1','\'Flash\''),('3','\'MIC_1\'','2','\'Microphones\''),('4','\'Keyboard_1\'','1','\'Keyboard\''),('5','\'Key1\'','3','\'Keyboard\'');

INSERT INTO items_for_order(id,item_name,id_order) VALUES('1','\'HDD_1\'','32');

INSERT INTO keyboards(item_id,params,price,rating,amount,name) VALUES('4','\'oidfguheu\'','123','2','1','\'Keyboard_1\''),('5','\'oidfguheu\'','123','5','1228','\'Key1\'');

INSERT INTO login(client_login,client_password,client_id) VALUES('\'Vlada228\'','\'123123\'','6'),('\'GAVNO\'','\'123123penis\'','7'),('\'GAVNO2\'','\'123qwe\'','8'),('\'GAVNO3\'','\'qwe123\'','9'),('\'GAVNO25\'','\'qweqwe\'','10');

INSERT INTO master_status(status,time,master_id) VALUES('0','\'2023-12-15 02:24:32\'','\'1\''),('0','\'2023-12-15 02:16:10\'','\'2\''),('0','\'2023-12-15 02:11:50\'','\'3\''),('0','\'2023-12-12 00:00:00\'','\'4\''),('1','\'2023-12-15 02:25:36\'','\'5\'');


INSERT INTO microphones(item_id,params,price,rating,amount,name) VALUES('3','\'oidfguheu\'','123','5','19','\'MIC_1\'');

INSERT INTO orders(order_datetime,id_order,order_sum,order_status,client_id,services_type,client_address,delivery_type,master_id,pick_up_point_id,courier_id) VALUES('\'2023-12-15 02:24:32\'','30','150','0','8','2','\'GTA for USA\'','NULL','1','NULL','NULL'),('\'2023-12-15 02:25:36\'','31','150','0','8','2','\'GTA for USA\'','NULL','5','NULL','NULL'),('\'2023-12-15 02:29:55\'','32','12','0','8','NULL','\'GTA for USA\'','1','NULL','NULL','NULL');

INSERT INTO pc_builder(master_id,rating,service_id,name,time) VALUES('1','2.5','1','\'james_gay\'','\'2023-11-21 22:31:07\''),('2','2','1','\'zxc\'','\'2023-11-21 22:31:07\''),('3','1.875','1','\'asd\'','\'2023-11-21 22:31:07\'');

INSERT INTO pc_cleaner(master_id,rating,service_id,name,time) VALUES('1','1','3','\'asdasdasdas\'','\'2023-12-12 00:00:00\'');

INSERT INTO pc_master(master_id,rating,service_id,name,time) VALUES('\'1\'','1','2','\'qwqweqw\'','\'2023-12-12 00:00:00\''),('\'2\'','5','2','\'James Howlett\'','\'2023-12-15 01:46:03\''),('\'3\'','3','2','\'Garou993\'','\'2023-12-15 01:45:13\''),('\'4\'','2','2','\'ASDAD\'','\'2023-12-12 00:00:00\''),('\'5\'','2','2','\'James Howlett\'','\'2023-12-12 00:00:00\'');

INSERT INTO pick_up_point(id_point,open_hours,address_point,id_order) VALUES('1','\'2023-12-12 00:00:00\'','\'qqqqq\'','NULL');

INSERT INTO services(services_type,price) VALUES('1','100'),('2','150'),('3','200');


INSERT INTO storage(storage_id,address) VALUES('1','\'asdasdas\''),('2','\'GTA for USA\''),('3','\'GTA for USA\'');

INSERT INTO techsupp(support_id,datetime_tech_supp,client_id,question) VALUES('1','\'2023-12-15 02:31:33\'','8','X\'617364617364\''),('2','\'2023-12-15 02:31:53\'','8','X\'617364617364617364617364617364\''),('3','\'2023-12-15 02:31:57\'','8','X\'737373737373\''),('4','\'2023-12-15 02:31:58\'','8','X\'737373737373\'');
INSERT INTO tracks(track_id,status,time_to_deliver,id_point) VALUES('1','0','\'2023-12-12 00:00:00\'','NULL');DROP PROCEDURE IF EXISTS proc_name;
CREATE PROCEDURE `proc_name`()
BEGIN
        SELECT * FROM orders;
END;

DROP Function IF EXISTS news;
DELIMITER ;;
CREATE FUNCTION `news`() RETURNS int
    READS SQL DATA
BEGIN
    return 0;
END;;
DELIMITER ;