-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema match_score_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema match_score_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `match_score_db` DEFAULT CHARACTER SET latin1 ;
USE `match_score_db` ;

-- -----------------------------------------------------
-- Table `match_score_db`.`teams`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `match_score_db`.`teams` (
  `id` INT NOT NULL,
  `teams_name` VARCHAR(45) NOT NULL,
  `number_of_players` INT NULL DEFAULT 0,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `match_score_db`.`players`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `match_score_db`.`players` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `full_name` VARCHAR(45) NOT NULL,
  `country` VARCHAR(45) NOT NULL,
  `sports_club` VARCHAR(45) NOT NULL,
  `is_active` TINYINT(4) NULL DEFAULT 1,
  `is_connected` TINYINT(4) NULL DEFAULT 0,
  `teams_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_players_teams1_idx` (`teams_id` ASC) VISIBLE,
  CONSTRAINT `fk_players_teams1`
    FOREIGN KEY (`teams_id`)
    REFERENCES `match_score_db`.`teams` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 203
DEFAULT CHARACTER SET = latin1;


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
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = latin1;


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
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `match_score_db`.`dates`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `match_score_db`.`dates` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `date` DATE NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 12
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `match_score_db`.`matches`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `match_score_db`.`matches` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `format` VARCHAR(45) NOT NULL,
  `game_type` VARCHAR(45) NOT NULL,
  `participant_1` VARCHAR(45) NOT NULL,
  `participant_2` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  `winner` VARCHAR(45) NULL DEFAULT NULL,
  `tournament_name` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 54
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `match_score_db`.`players_statistics`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `match_score_db`.`players_statistics` (
  `players_id` INT(11) NOT NULL,
  `player_name` VARCHAR(45) NULL DEFAULT NULL,
  `opponent_name` VARCHAR(45) NULL DEFAULT NULL,
  `win` INT(11) NULL DEFAULT NULL,
  `loss` INT(11) NULL DEFAULT NULL,
  `matches_id` INT(11) NOT NULL,
  `tournament_name` VARCHAR(45) NULL DEFAULT NULL,
  `tournament_trophy` INT(11) NULL DEFAULT 0,
  `date` DATE NULL DEFAULT NULL,
  INDEX `fk_players_statistics_players1_idx` (`players_id` ASC) VISIBLE,
  INDEX `fk_players_statistics_matches1_idx` (`matches_id` ASC) VISIBLE,
  CONSTRAINT `fk_players_statistics_players1`
    FOREIGN KEY (`players_id`)
    REFERENCES `match_score_db`.`players` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_players_statistics_matches1`
    FOREIGN KEY (`matches_id`)
    REFERENCES `match_score_db`.`matches` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `match_score_db`.`tournaments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `match_score_db`.`tournaments` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NOT NULL,
  `format` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  `prize` INT(11) NOT NULL,
  `game_type` VARCHAR(45) NOT NULL,
  `users_creator_id` INT(11) NOT NULL,
  `is_finished` TINYINT(4) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  INDEX `fk_tournaments_users1_idx` (`users_creator_id` ASC) VISIBLE,
  CONSTRAINT `fk_tournaments_users1`
    FOREIGN KEY (`users_creator_id`)
    REFERENCES `match_score_db`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `match_score_db`.`teams_statistics`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `match_score_db`.`teams_statistics` (
  `teams_id` INT NOT NULL,
  `team_name` VARCHAR(45) NULL DEFAULT NULL,
  `opponent_name` VARCHAR(45) NULL DEFAULT NULL,
  `win` INT NULL DEFAULT 0,
  `loss` INT NULL DEFAULT 0,
  `matches_id` INT(11) NOT NULL,
  `tournament_name` VARCHAR(100) NULL DEFAULT NULL,
  `tournament_trophy` INT NULL DEFAULT 0,
  `date` DATE NULL,
  INDEX `fk_teams_statistics_teams1_idx` (`teams_id` ASC) VISIBLE,
  INDEX `fk_teams_statistics_matches1_idx` (`matches_id` ASC) VISIBLE,
  CONSTRAINT `fk_teams_statistics_teams1`
    FOREIGN KEY (`teams_id`)
    REFERENCES `match_score_db`.`teams` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_teams_statistics_matches1`
    FOREIGN KEY (`matches_id`)
    REFERENCES `match_score_db`.`matches` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `match_score_db`.`tournaments_matches`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `match_score_db`.`tournaments_matches` (
  `tournaments_id` INT(11) NOT NULL,
  `matches_id` INT(11) NOT NULL,
  PRIMARY KEY (`tournaments_id`, `matches_id`),
  INDEX `fk_tournaments_has_matches_matches1_idx` (`matches_id` ASC) VISIBLE,
  INDEX `fk_tournaments_has_matches_tournaments1_idx` (`tournaments_id` ASC) VISIBLE,
  CONSTRAINT `fk_tournaments_has_matches_tournaments1`
    FOREIGN KEY (`tournaments_id`)
    REFERENCES `match_score_db`.`tournaments` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_tournaments_has_matches_matches1`
    FOREIGN KEY (`matches_id`)
    REFERENCES `match_score_db`.`matches` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
