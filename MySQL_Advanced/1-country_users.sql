-- Create a table
-- with only some possible countries
DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `email` VARCHAR(255) NOT NULL,
    `name` VARCHAR(255),
    `country` ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
    PRIMARY KEY (`id`),
    UNIQUE (`email`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;
