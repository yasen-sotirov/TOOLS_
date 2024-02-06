ALTER TABLE match_score_db.admin_requests AUTO_INCREMENT = 1;
ALTER TABLE match_score_db.dates AUTO_INCREMENT = 1;
ALTER TABLE match_score_db.matches AUTO_INCREMENT = 1;
ALTER TABLE match_score_db.players AUTO_INCREMENT = 1;
ALTER TABLE match_score_db.statistics AUTO_INCREMENT = 1;
ALTER TABLE match_score_db.tournaments AUTO_INCREMENT = 1;
ALTER TABLE match_score_db.users AUTO_INCREMENT = 1;


-- DATES
-- ----------------------------------------------------------------------------------
INSERT INTO match_score_db.dates (date) VALUES ('2020-1-1');




-- USERS
-- ----------------------------------------------------------------------------------
-- Insert the provided user information only if the table is empty
-- ----------------------------------------------------------------------------------
INSERT INTO match_score_db.users (full_name, email, password, gender, role, players_id) 
VALUES  ('Steven Atkinson', 'steven.atkinson@gmail.com', '2fca7af39df396e0890de73cf93628cc50261c1c5bff980995ce740279a740f9', 'male', 'admin', null),
	    ('Michael Scott', 'michael.scott@gmail.com', 'd24259be13407e0d132337bd8398ee9aaff43a249c38d0bf222429f311c9c939', 'male', 'director', null),
        ('Pamela Beasly', 'pamela.beasly@gmail.com', '78d7ba5153684388785609ab6fc8beafa7d63c394481026999f6ccf420d9ab9a', 'female', 'director', null),
		('Jim Halpert', 'jim.halpert@gmail.com', '3cb7aff2146cd44bbdef023e465424e3c4a6ac793b7fa250c8895d93065ec53c', 'male', 'director', null);



-- INSERT INTO `match_score_db`.`users` 
--     (`full_name`, `email`, `password`, `gender`, `role`, `players_id`) 
-- VALUES 
--     ('Owen Garrett', 'owen.garrett@yahoo.com', 'c2b41017a8036252bb2308ea026284ffd455a9eab57c4b65777fbcd0ac891964', 'male', 'spectator', null)
-- ON DUPLICATE KEY UPDATE `id` = `id`;

-- INSERT INTO `match_score_db`.`users` 
--     (`full_name`, `email`, `password`, `gender`, `role`, `players_id`) 
-- VALUES 
--     ('Kyan Chandler', 'chandler_kyan@gmx.de', 'c53c1c5f81b36257b951965239ef46c1c6e6fbb4d4eb01cee58b6dc9bc2ae80c', 'male', 'spectator', null)
-- ON DUPLICATE KEY UPDATE `id` = `id`;

-- INSERT INTO `match_score_db`.`users` 
--     (`full_name`, `email`, `password`, `gender`, `role`, `players_id`) 
-- VALUES 
--     ('Frank Warren', 'warwarbinks@gmail.com', '74fca0325b5fdb3a34badb40a2581cfbd5344187e8d3432952a5abc0929c1246', 'male', 'player', '4')
-- ON DUPLICATE KEY UPDATE `id` = `id`;

-- INSERT INTO `match_score_db`.`users` 
--     (`full_name`, `email`, `password`, `gender`, `role`, `players_id`) 
-- VALUES 
--     ('Susan Wilkinson', 'suuusan_123@abv.bg', 'ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f', 'female', 'player', '5')
-- ON DUPLICATE KEY UPDATE `id` = `id`;






-- PLAYERS
-- ----------------------------------------------------------------------------------
INSERT INTO match_score_db.players (full_name, country, sports_club, is_active, is_connected) 
VALUES  ('Michael Scott', 'Jamaica', 'Dunder Mufflin sports club', 1, 0),
	    ('Pam Beasly', 'France', 'La Boxeur Club', 1, 0),
	    ('Jim Halpert', 'USA', 'TheOfficeFans', 1, 0),
		('Frank Warren', 'USA', 'NeverBackDown', 1, 0),
		('Susan Wilkinson', 'Bulgaria', 'Bulgarian Power', 1, 0),
		('Owen Garrett', 'UK', 'Boxing Club Bruf', 1, 0);


-- MATCHES
-- ----------------------------------------------------------------------------------
INSERT INTO match_score_db.matches (id, format, game_type, participant_1, participant_2, date, winner, tournament_name)
VALUES	(1, 'time limit', 'one on one',	'Michael Scott', 'Frank Warren', '2020-01-03', 'Frank Warren', null),
		(2, 'time limit', 'one on one',	'Michael Scott', 'Pam Beasly', '2020-02-03', 'Michael Scott', null),
		(3, 'time limit', 'one on one',	'Jim Halpert', 'Pam Beasly', '2020-03-04', 'Pam Beasly', null),
		(4, 'time limit', 'one on one',	'Jim Halpert', 'Frank Warren', '2023-01-14', null, null),
		(5, 'time limit', 'one on one',	'Jim Halpert', 'Michael Scott',	'2023-02-06', null, null);
		

-- TOURNAMENTS
-- ----------------------------------------------------------------------------------
INSERT INTO match_score_db.tournaments (title, format, date, prize, game_type, users_creator_id, is_finished)
VALUES ('first tournament', 'knockout', '2023-1-20', 10, 'one on one', 1, 0),
       ('second tournament', 'knockout', '2023-1-21', 10, 'league', 1, 0);





