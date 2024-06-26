CREATE DATABASE `UniBar`;

CREATE TABLE `UniBar`.`Users` (
    `user_id` CHAR(36) NOT NULL,
    `password` VARCHAR(32) NOT NULL,
    `auth_token` CHAR(32),
    `name` VARCHAR(32) NOT NULL,
    `email` VARCHAR(32) NOT NULL,
    `registered_time` DATETIME NOT NULL,
    `delivery_tokens` INT NOT NULL,
    `phone_number` VARCHAR(24) NOT NULL,
    `etransfer_email` VARCHAR(32),

    PRIMARY KEY (`user_id`),
    UNIQUE (`auth_token`),
    UNIQUE (`email`)
);

CREATE TABLE `UniBar`.`Admins` (
    `admin_id` CHAR(36) NOT NULL,
    `name` VARCHAR(32) NOT NULL,
    `auth_token` VARCHAR(32) NOT NULL,
    `registered_time` DATETIME NOT NULL,

    PRIMARY KEY (`admin_id`),
    UNIQUE (`auth_token`)
);

CREATE TABLE `UniBar`.`Orders` (
    `order_id` CHAR(36) NOT NULL,
    `orderer_id` CHAR(36) NOT NULL,
    `deliverer_id` CHAR(36),

    `creation_time` DATETIME NOT NULL,
    `deadline_time` DATETIME NOT NULL,
    `claimed_time` DATETIME,
    `delivered_time` DATETIME,
    `cancelled_time` DATETIME,

    `order` varchar(250) NOT NULL,
    `source` varchar(250) NOT NULL,
    `destination` varchar(250) NOT NULL,
    `payment_method` ENUM('cash', 'etransfer') NOT NULL,

    PRIMARY KEY (`order_id`),
    FOREIGN KEY (`orderer_id`) REFERENCES `UniBar`.`Users`(`user_id`),
    FOREIGN KEY (`deliverer_id`) REFERENCES `UniBar`.`Users`(`user_id`)
);

CREATE TABLE `UniBar`.`Reports` (
    `report_id` CHAR(36) NOT NULL,
    `reporter_user_id` CHAR(36) NOT NULL,
    `reported_user_id` CHAR(36) NOT NULL,
    `order_id` CHAR(36) NOT NULL,

    `time` DATETIME NOT NULL,
    `message` varchar(250) NOT NULL,
    `conclusion` VARCHAR(250),

    PRIMARY KEY (`report_id`),
    FOREIGN KEY (`reporter_user_id`) REFERENCES `UniBar`.`Users`(`user_id`),
    FOREIGN KEY (`reported_user_id`) REFERENCES `UniBar`.`Users`(`user_id`),
    FOREIGN KEY (`order_id`) REFERENCES `UniBar`.`Orders`(`order_id`)
);

CREATE TABLE `UniBar`.`Messages` (
    `message_id` CHAR(36) NOT NULL,
    `user_id` CHAR(36),
    `email` VARCHAR(32),
    `message` VARCHAR(500) NOT NULL,
    `time` DATETIME NOT NULL,

    PRIMARY KEY (`message_id`),
    FOREIGN KEY (`user_id`) REFERENCES `UniBar`.`Users`(`user_id`)
);

