-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema new_forum_project
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema new_forum_project
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `new_forum_project` DEFAULT CHARACTER SET latin1 ;
-- -----------------------------------------------------
-- Schema match_score_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema match_score_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `match_score_db` DEFAULT CHARACTER SET latin1 ;
USE `new_forum_project` ;

-- -----------------------------------------------------
-- Table `new_forum_project`.`category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `new_forum_project`.`category` (
  `name_of_category` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`name_of_category`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `new_forum_project`.`new_user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `new_forum_project`.`new_user` (
  `id_of_user` INT(11) NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(60) NOT NULL,
  `nickname` VARCHAR(40) NOT NULL,
  `password` VARCHAR(50) NOT NULL,
  `date_of_birth` DATE NOT NULL,
  `gender` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id_of_user`))
ENGINE = InnoDB
AUTO_INCREMENT = 20
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `new_forum_project`.`conversations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `new_forum_project`.`conversations` (
  `id_of_conversations` INT(11) NOT NULL AUTO_INCREMENT,
  `the_receiver` INT(11) NOT NULL,
  `the_sender` INT(11) NOT NULL,
  PRIMARY KEY (`id_of_conversations`),
  INDEX `fk_conversations_new_user1_idx` (`the_receiver` ASC) VISIBLE,
  INDEX `fk_conversations_new_user2_idx` (`the_sender` ASC) VISIBLE,
  CONSTRAINT `fk_conversations_new_user1`
    FOREIGN KEY (`the_receiver`)
    REFERENCES `new_forum_project`.`new_user` (`id_of_user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_conversations_new_user2`
    FOREIGN KEY (`the_sender`)
    REFERENCES `new_forum_project`.`new_user` (`id_of_user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `new_forum_project`.`messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `new_forum_project`.`messages` (
  `id_of_messages` INT(11) NOT NULL AUTO_INCREMENT,
  `text_message` TEXT NOT NULL,
  `conversation_id` INT(11) NOT NULL,
  `the_sender` INT(11) NOT NULL,
  PRIMARY KEY (`id_of_messages`),
  INDEX `fk_messages_conversations_between_users1_idx` (`conversation_id` ASC) VISIBLE,
  INDEX `fk_messages_new_user1_idx` (`the_sender` ASC) VISIBLE,
  CONSTRAINT `fk_messages_conversations_between_users1`
    FOREIGN KEY (`conversation_id`)
    REFERENCES `new_forum_project`.`conversations` (`id_of_conversations`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_messages_new_user1`
    FOREIGN KEY (`the_sender`)
    REFERENCES `new_forum_project`.`new_user` (`id_of_user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 27
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `new_forum_project`.`replies`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `new_forum_project`.`replies` (
  `id_of_replies` INT(11) NOT NULL AUTO_INCREMENT,
  `text` TEXT NOT NULL,
  `new_topic_id` INT(11) NOT NULL,
  `new_user_id` INT(11) NOT NULL,
  PRIMARY KEY (`id_of_replies`),
  INDEX `fk_replies_new_topic1_idx` (`new_topic_id` ASC) VISIBLE,
  INDEX `fk_replies_new_user1_idx` (`new_user_id` ASC) VISIBLE,
  CONSTRAINT `fk_replies_new_topic1`
    FOREIGN KEY (`new_topic_id`)
    REFERENCES `new_forum_project`.`new_topic` (`id_of_topic`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_replies_new_user1`
    FOREIGN KEY (`new_user_id`)
    REFERENCES `new_forum_project`.`new_user` (`id_of_user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 65
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `new_forum_project`.`new_topic`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `new_forum_project`.`new_topic` (
  `id_of_topic` INT(11) NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NOT NULL,
  `topic_text` LONGTEXT NOT NULL,
  `date_of_creation` DATETIME NOT NULL,
  `category_name_of_category` VARCHAR(25) NOT NULL,
  `id_of_author` INT(11) NOT NULL,
  `best_reply_id` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id_of_topic`),
  INDEX `fk_new_topic_category1_idx` (`category_name_of_category` ASC) VISIBLE,
  INDEX `fk_new_topic_new_user1_idx` (`id_of_author` ASC) VISIBLE,
  INDEX `fk_new_topic_replies1_idx` (`best_reply_id` ASC) VISIBLE,
  CONSTRAINT `fk_new_topic_category1`
    FOREIGN KEY (`category_name_of_category`)
    REFERENCES `new_forum_project`.`category` (`name_of_category`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_new_topic_new_user1`
    FOREIGN KEY (`id_of_author`)
    REFERENCES `new_forum_project`.`new_user` (`id_of_user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_new_topic_replies1`
    FOREIGN KEY (`best_reply_id`)
    REFERENCES `new_forum_project`.`replies` (`id_of_replies`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 17
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `new_forum_project`.`reactions_of_replies`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `new_forum_project`.`reactions_of_replies` (
  `id_of_likes` INT(11) NOT NULL AUTO_INCREMENT,
  `UpVote` INT(11) NULL DEFAULT NULL,
  `DownVote` INT(11) NULL DEFAULT NULL,
  `new_user_id` INT(11) NOT NULL,
  `id_of_replies` INT(11) NOT NULL,
  PRIMARY KEY (`id_of_likes`),
  INDEX `fk_likes_of_post_new_user1_idx` (`new_user_id` ASC) VISIBLE,
  INDEX `fk_reactions_of_post_replies1_idx` (`id_of_replies` ASC) VISIBLE,
  CONSTRAINT `fk_likes_of_post_new_user1`
    FOREIGN KEY (`new_user_id`)
    REFERENCES `new_forum_project`.`new_user` (`id_of_user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_reactions_of_post_replies1`
    FOREIGN KEY (`id_of_replies`)
    REFERENCES `new_forum_project`.`replies` (`id_of_replies`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 98
DEFAULT CHARACTER SET = latin1;

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
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `match_score_db`.`matches`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `match_score_db`.`matches` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(100) NOT NULL,
  `player_1` VARCHAR(45) NULL DEFAULT NULL,
  `player_2` VARCHAR(45) NULL DEFAULT NULL,
  `date` DATE NOT NULL,
  `format` VARCHAR(45) NOT NULL,
  `prize` INT(11) NOT NULL,
  `tournament_name` VARCHAR(100) NULL DEFAULT NULL,
  `creator` VARCHAR(45) NULL DEFAULT NULL,
  `played` TINYINT(4) NOT NULL DEFAULT 0,
  `winner` VARCHAR(45) NULL DEFAULT NULL,
  `tournament_id` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_match_tournament_idx` (`tournament_id` ASC) VISIBLE,
  CONSTRAINT `fk_match_tournament`
    FOREIGN KEY (`tournament_id`)
    REFERENCES `match_score_db`.`tournaments` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 7
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
  `full_name` VARCHAR(45) NULL DEFAULT NULL,
  `country` VARCHAR(45) NULL DEFAULT NULL,
  `sport_club` VARCHAR(45) NULL DEFAULT NULL,
  `titles` INT(11) NOT NULL DEFAULT 0,
  `wins` INT(11) NOT NULL DEFAULT 0,
  `draws` INT NOT NULL DEFAULT 0,
  `losses` INT(11) NOT NULL DEFAULT 0,
  `money_prize` INT(11) NOT NULL DEFAULT 0,
  `is_active` TINYINT(4) NOT NULL DEFAULT 1,
  `statistics_matches_id` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_players_statistics1_idx` (`statistics_matches_id` ASC) VISIBLE,
  CONSTRAINT `fk_players_statistics1`
    FOREIGN KEY (`statistics_matches_id`)
    REFERENCES `match_score_db`.`statistics` (`matches_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 37
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `match_score_db`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `match_score_db`.`users` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `full_name` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `password` VARCHAR(300) NOT NULL,
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
AUTO_INCREMENT = 20
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `match_score_db`.`admin_requests`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `match_score_db`.`admin_requests` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `type_of_request` VARCHAR(45) NOT NULL,
  `players_id` INT(11) NULL DEFAULT NULL,
  `users_id` INT(11) NOT NULL,
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
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `match_score_db`.`matches_players`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `match_score_db`.`matches_players` (
  `matches_id` INT(11) NOT NULL,
  `team` INT NULL,
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
DEFAULT CHARACTER SET = latin1;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
