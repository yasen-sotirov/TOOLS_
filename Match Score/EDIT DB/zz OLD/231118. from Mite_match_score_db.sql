-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema match_score_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema match_score_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `match_score_db` DEFAULT CHARACTER SET latin1 ;
USE `match_score_db` ;

-- -----------------------------------------------------
-- Table `match_score_db`.`tournaments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `match_score_db`.`tournaments` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NOT NULL,
  `format` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  `prize` INT(11) NOT NULL,
  `creator` VARCHAR(45) NULL DEFAULT NULL,
  `users_creator_id` INT(11) NOT NULL,
  `statistics_matches_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_tournaments_statistics1_idx` (`statistics_matches_id` ASC) VISIBLE,
  INDEX `fk_tournaments_users1_idx` (`users_creator_id` ASC) VISIBLE,
  CONSTRAINT `fk_tournaments_statistics1`
    FOREIGN KEY (`statistics_matches_id`)
    REFERENCES `match_score_db`.`statistics` (`matches_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_tournaments_users1`
    FOREIGN KEY (`users_creator_id`)
    REFERENCES `match_score_db`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `match_score_db`.`matches`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `match_score_db`.`matches` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `format` VARCHAR(45) NOT NULL,
  `players_id_1` INT(11) NOT NULL,
  `players_id_2` INT(11) NOT NULL,
  `date` DATE NOT NULL,
  `tournament_name` VARCHAR(100) NULL DEFAULT NULL,
  `played` TINYINT(4) NOT NULL DEFAULT 0,
  `winner` VARCHAR(45) NULL DEFAULT NULL,
  `tournaments_id` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_match_tournament_idx` (`tournaments_id` ASC) VISIBLE,
  CONSTRAINT `fk_match_tournament`
    FOREIGN KEY (`tournaments_id`)
    REFERENCES `match_score_db`.`tournaments` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `match_score_db`.`statistics`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `match_score_db`.`statistics` (
  `matches_id` INT(11) NOT NULL,
  `round` INT(11) NULL DEFAULT NULL,
  `points_p1` INT(11) NULL DEFAULT NULL,
  `points_p2` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`matches_id`),
  INDEX `fk_statistics_matches1_idx` (`matches_id` ASC) VISIBLE,
  CONSTRAINT `fk_statistics_matches1`
    FOREIGN KEY (`matches_id`)
    REFERENCES `match_score_db`.`matches` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `match_score_db`.`players`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `match_score_db`.`players` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `full_name` VARCHAR(45) NOT NULL,
  `country` VARCHAR(45) NOT NULL,
  `sports_club` VARCHAR(45) NOT NULL,
  `is_active` TINYINT(4) NULL DEFAULT 0,
  `is_connected` TINYINT(4) NULL DEFAULT 0,
  `statistics_matches_id` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_players_statistics1_idx` (`statistics_matches_id` ASC) VISIBLE,
  CONSTRAINT `fk_players_statistics1`
    FOREIGN KEY (`statistics_matches_id`)
    REFERENCES `match_score_db`.`statistics` (`matches_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = latin1;

-- Insert the provided player information only if the table is empty

INSERT INTO `match_score_db`.`players` 
    (`full_name`, `country`, `sports_club`, `is_active`, `is_connected`, `statistics_matches_id`) 
VALUES 
    ('Michael Scott', 'Jamaica', 'Dunder Mufflin sports club', '0', '1', null)
ON DUPLICATE KEY UPDATE `id` = `id`;

INSERT INTO `match_score_db`.`players` 
    (`full_name`, `country`, `sports_club`, `is_active`, `is_connected`, `statistics_matches_id`) 
VALUES 
    ('Pam Beasly', 'France', 'La Boxeur Club', '0', '1', null)
ON DUPLICATE KEY UPDATE `id` = `id`;

INSERT INTO `match_score_db`.`players` 
    (`full_name`, `country`, `sports_club`, `is_active`, `is_connected`, `statistics_matches_id`) 
VALUES 
    ('Jim Halpert', 'USA', 'TheOfficeFans', '0', '1', null)
ON DUPLICATE KEY UPDATE `id` = `id`;

INSERT INTO `match_score_db`.`players` 
    (`full_name`, `country`, `sports_club`, `is_active`, `is_connected`, `statistics_matches_id`) 
VALUES 
    ('Frank Warren', 'USA', 'NeverBackDown', '0', '1', null)
ON DUPLICATE KEY UPDATE `id` = `id`;

INSERT INTO `match_score_db`.`players` 
    (`full_name`, `country`, `sports_club`, `is_active`, `is_connected`, `statistics_matches_id`) 
VALUES 
    ('Susan Wilkinson', 'Bulgaria', 'Bulgarian Power', '0', '1', null)
ON DUPLICATE KEY UPDATE `id` = `id`;

INSERT INTO `match_score_db`.`players` 
    (`full_name`, `country`, `sports_club`, `is_active`, `is_connected`, `statistics_matches_id`) 
VALUES 
    ('Owen Garrett', 'UK', 'Boxing Club Bruf', '0', '0', null)
ON DUPLICATE KEY UPDATE `id` = `id`;

-- -----------------------------------------------------
-- Table `match_score_db`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `match_score_db`.`users` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `full_name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(70) NOT NULL,
  `password` VARCHAR(150) NOT NULL,
  `gender` VARCHAR(10) NOT NULL,
  `role` VARCHAR(10) NOT NULL,
  `players_id` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_users_players1_idx` (`players_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_players1`
    FOREIGN KEY (`players_id`)
    REFERENCES `match_score_db`.`players` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = latin1;

-- Insert the provided user information only if the table is empty
INSERT INTO `match_score_db`.`users` 
    (`full_name`, `email`, `password`, `gender`, `role`, `players_id`) 
VALUES 
    ('Steven Atkinson', 'steven.atkinson@gmail.com', '2fca7af39df396e0890de73cf93628cc50261c1c5bff980995ce740279a740f9', 'male', 'admin', null)
ON DUPLICATE KEY UPDATE `id` = `id`;

INSERT INTO `match_score_db`.`users` 
    (`full_name`, `email`, `password`, `gender`, `role`, `players_id`) 
VALUES 
    ('Michael Scott', 'michael.scott@gmail.com', 'd24259be13407e0d132337bd8398ee9aaff43a249c38d0bf222429f311c9c939', 'male', 'director', '1')
ON DUPLICATE KEY UPDATE `id` = `id`;

INSERT INTO `match_score_db`.`users` 
    (`full_name`, `email`, `password`, `gender`, `role`, `players_id`) 
VALUES 
    ('Pamela Beasly', 'pamela.beasly@gmail.com', '78d7ba5153684388785609ab6fc8beafa7d63c394481026999f6ccf420d9ab9a', 'female', 'director', '2')
ON DUPLICATE KEY UPDATE `id` = `id`;

INSERT INTO `match_score_db`.`users` 
    (`full_name`, `email`, `password`, `gender`, `role`, `players_id`) 
VALUES 
    ('Jim Halpert', 'jim.halpert@gmail.com', '3cb7aff2146cd44bbdef023e465424e3c4a6ac793b7fa250c8895d93065ec53c', 'male', 'director', '3')
ON DUPLICATE KEY UPDATE `id` = `id`;

INSERT INTO `match_score_db`.`users` 
    (`full_name`, `email`, `password`, `gender`, `role`, `players_id`) 
VALUES 
    ('Owen Garrett', 'owen.garrett@yahoo.com', 'c2b41017a8036252bb2308ea026284ffd455a9eab57c4b65777fbcd0ac891964', 'male', 'spectator', null)
ON DUPLICATE KEY UPDATE `id` = `id`;

INSERT INTO `match_score_db`.`users` 
    (`full_name`, `email`, `password`, `gender`, `role`, `players_id`) 
VALUES 
    ('Kyan Chandler', 'chandler_kyan@gmx.de', 'c53c1c5f81b36257b951965239ef46c1c6e6fbb4d4eb01cee58b6dc9bc2ae80c', 'male', 'spectator', null)
ON DUPLICATE KEY UPDATE `id` = `id`;

INSERT INTO `match_score_db`.`users` 
    (`full_name`, `email`, `password`, `gender`, `role`, `players_id`) 
VALUES 
    ('Frank Warren', 'warwarbinks@gmail.com', '74fca0325b5fdb3a34badb40a2581cfbd5344187e8d3432952a5abc0929c1246', 'male', 'player', '4')
ON DUPLICATE KEY UPDATE `id` = `id`;

INSERT INTO `match_score_db`.`users` 
    (`full_name`, `email`, `password`, `gender`, `role`, `players_id`) 
VALUES 
    ('Susan Wilkinson', 'suuusan_123@abv.bg', 'ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f', 'female', 'player', '5')
ON DUPLICATE KEY UPDATE `id` = `id`;



-- -----------------------------------------------------
-- Table `match_score_db`.`admin_requests`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `match_score_db`.`admin_requests` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `type_of_request` VARCHAR(45) NOT NULL,
  `players_id` INT(11) NULL DEFAULT NULL,
  `users_id` INT(11) NOT NULL,
  `status` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_admin_requests_users1_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_admin_requests_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `match_score_db`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `match_score_db`.`dates`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `match_score_db`.`dates` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `date` DATE NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `match_score_db`.`matches_players`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `match_score_db`.`matches_players` (
  `matches_id` INT(11) NOT NULL,
  `team_name` VARCHAR(45) NULL DEFAULT NULL,
  `players_id` INT(11) NOT NULL,
  PRIMARY KEY (`matches_id`, `players_id`),
  INDEX `fk_matches_has_players_players1_idx` (`players_id` ASC) VISIBLE,
  INDEX `fk_matches_has_players_matches1_idx` (`matches_id` ASC) VISIBLE,
  CONSTRAINT `fk_matches_has_players_matches1`
    FOREIGN KEY (`matches_id`)
    REFERENCES `match_score_db`.`matches` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_matches_has_players_players1`
    FOREIGN KEY (`players_id`)
    REFERENCES `match_score_db`.`players` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = latin1;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
