ALTER TABLE match_score_db.admin_requests AUTO_INCREMENT = 1;
ALTER TABLE match_score_db.dates AUTO_INCREMENT = 1;
ALTER TABLE match_score_db.matches AUTO_INCREMENT = 1;
ALTER TABLE match_score_db.players AUTO_INCREMENT = 1;
ALTER TABLE match_score_db.players_has_matches AUTO_INCREMENT = 1;
ALTER TABLE match_score_db.tournaments AUTO_INCREMENT = 1;
ALTER TABLE match_score_db.users AUTO_INCREMENT = 1;


-- DATES
-- ----------------------------------------------------------------------------------
INSERT INTO match_score_db.dates (date) VALUES ('2023-1-1');




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
		('Owen Garrett', 'UK', 'Boxing Club Bruf', 1, 0),
        ('Jack Thompson', 'USA', 'NeverBackDown', 1, 0),
		('Sophie Williams', 'Jamaica', 'La Boxeur Club', 1, 0),
		('Antoine Martin', 'France', 'TheOfficeFans', 1, 0),
		('Elena Petrova', 'Bulgaria', 'Bulgarian Power', 1, 0),
		('Oliver Smith', 'UK', 'Dunder Mufflin sports club', 1, 0),
		('Isabella Davis', 'USA', 'Boxing Club Bruf', 1, 0),
		('Carlos Rodriguez', 'Jamaica', 'NeverBackDown', 1, 0),
		('Camille Dupont', 'France', 'La Boxeur Club', 1, 0),
		('Dimitar Ivanov', 'Bulgaria', 'TheOfficeFans', 1, 0),
		('Grace White', 'UK', 'Bulgarian Power', 1, 0),
		('Mason Taylor', 'USA', 'Dunder Mufflin sports club', 1, 0),
		('Ava Robinson', 'Jamaica', 'Boxing Club Bruf', 1, 0),
		('Lucas Garcia', 'France', 'NeverBackDown', 1, 0),
		('Stella Johnson', 'Bulgaria', 'La Boxeur Club', 1, 0),
		('Liam Anderson', 'UK', 'TheOfficeFans', 1, 0),
		('Natalie Brown', 'USA', 'Bulgarian Power', 1, 0),
		('Diego Martinez', 'Jamaica', 'Dunder Mufflin sports club', 1, 0),
		('Emma Wilson', 'France', 'Boxing Club Bruf', 1, 0),
		('Eva Harris', 'Bulgaria', 'NeverBackDown', 1, 0),
		('Aiden Clark', 'UK', 'La Boxeur Club', 1, 0),
		('Zoe Green', 'USA', 'TheOfficeFans', 1, 0),
		('Julian Scott', 'Jamaica', 'Bulgarian Power', 1, 0),
		('Sophia King', 'France', 'Dunder Mufflin sports club', 1, 0),
		('Landon Miller', 'Bulgaria', 'Boxing Club Bruf', 1, 0),
		('Chloe Adams', 'UK', 'NeverBackDown', 1, 0),
		('Gabriel Turner', 'USA', 'La Boxeur Club', 1, 0),
		('Luna Martinez', 'Jamaica', 'TheOfficeFans', 1, 0),
		('Maxwell Harris', 'France', 'Bulgarian Power', 1, 0),
		('Victoria Thomas', 'Bulgaria', 'Dunder Mufflin sports club', 1, 0),
		('Leo Garcia', 'UK', 'Boxing Club Bruf', 1, 0),
		('Penelope White', 'USA', 'NeverBackDown', 1, 0),
		('Miguel Rodriguez', 'Jamaica', 'La Boxeur Club', 1, 0),
		('Madison Lewis', 'France', 'TheOfficeFans', 1, 0),
		('Daniel Turner', 'Bulgaria', 'Bulgarian Power', 1, 0),
		('Aria Davis', 'UK', 'Dunder Mufflin sports club', 1, 0),
		('William Scott', 'USA', 'Boxing Club Bruf', 1, 0),
		('Isabel Brown', 'Jamaica', 'NeverBackDown', 1, 0),
		('Ethan Taylor', 'France', 'La Boxeur Club', 1, 0),
		('Mia Wilson', 'Bulgaria', 'TheOfficeFans', 1, 0),
		('Noah Turner', 'UK', 'Bulgarian Power', 1, 0),
		('Sophie Robinson', 'USA', 'Dunder Mufflin sports club', 1, 0),
		('Oliver Miller', 'Jamaica', 'Boxing Club Bruf', 1, 0),
		('Ava Perez', 'France', 'NeverBackDown', 1, 0),
		('Lucas Adams', 'Bulgaria', 'La Boxeur Club', 1, 0),
		('Emma Thomas', 'UK', 'TheOfficeFans', 1, 0),
		('Liam Harris', 'USA', 'Bulgarian Power', 1, 0),
		('Chloe Martin', 'Jamaica', 'Dunder Mufflin sports club', 1, 0),
		('Ella Turner', 'France', 'Boxing Club Bruf', 1, 0),
		('Mason Robinson', 'Bulgaria', 'NeverBackDown', 1, 0),
		('Zoe Garcia', 'UK', 'La Boxeur', 1, 0),
        ('Jackson White', 'USA', 'TheOfficeFans', 1, 0),
		('Sophia Garcia', 'Jamaica', 'Bulgarian Power', 1, 0),
		('Ethan Robinson', 'France', 'Dunder Mufflin sports club', 1, 0),
		('Aria Smith', 'Bulgaria', 'Boxing Club Bruf', 1, 0),
		('Oscar Turner', 'UK', 'NeverBackDown', 1, 0),
		('Lily Martinez', 'USA', 'La Boxeur Club', 1, 0),
		('Lucas Harris', 'Jamaica', 'TheOfficeFans', 1, 0),
		('Isabel Turner', 'France', 'Bulgarian Power', 1, 0),
		('Leo Anderson', 'Bulgaria', 'Dunder Mufflin sports club', 1, 0),
		('Mia Taylor', 'UK', 'Boxing Club Bruf', 1, 0),
		('Ella Martin', 'USA', 'NeverBackDown', 1, 0),
		('Oliver Davis', 'Jamaica', 'La Boxeur Club', 1, 0),
		('Ava Thompson', 'France', 'TheOfficeFans', 1, 0),
		('Mason Brown', 'Bulgaria', 'Bulgarian Power', 1, 0),
		('Emma Garcia', 'UK', 'Dunder Mufflin sports club', 1, 0),
		('Liam Harris', 'USA', 'Boxing Club Bruf', 1, 0),
		('Chloe Rodriguez', 'Jamaica', 'NeverBackDown', 1, 0),
		('Gabriel Turner', 'France', 'La Boxeur Club', 1, 0),
		('Luna Perez', 'Bulgaria', 'TheOfficeFans', 1, 0),
		('Maxwell Smith', 'UK', 'Bulgarian Power', 1, 0),
		('Victoria Turner', 'USA', 'Dunder Mufflin sports club', 1, 0),
		('Leo Adams', 'Jamaica', 'Boxing Club Bruf', 1, 0),
		('Penelope White', 'France', 'NeverBackDown', 1, 0),
		('Miguel Turner', 'Bulgaria', 'La Boxeur Club', 1, 0),
		('Madison Taylor', 'UK', 'TheOfficeFans', 1, 0),
		('Daniel Robinson', 'USA', 'Bulgarian Power', 1, 0),
		('Aria Martin', 'Jamaica', 'Dunder Mufflin sports club', 1, 0),
		('William Davis', 'France', 'Boxing Club Bruf', 1, 0),
		('Isabel Turner', 'Bulgaria', 'NeverBackDown', 1, 0),
		('Ethan Taylor', 'UK', 'La Boxeur Club', 1, 0),
		('Mia Robinson', 'USA', 'TheOfficeFans', 1, 0),
		('Noah Garcia', 'Jamaica', 'Bulgarian Power', 1, 0),
		('Sophie Turner', 'France', 'Dunder Mufflin sports club', 1, 0),
		('Oliver White', 'Bulgaria', 'Boxing Club Bruf', 1, 0),
		('Ava Turner', 'UK', 'NeverBackDown', 1, 0),
		('Liam Smith', 'USA', 'La Boxeur Club', 1, 0),
		('Chloe Davis', 'Jamaica', 'TheOfficeFans', 1, 0),
		('Ella Thompson', 'France', 'Bulgarian Power', 1, 0),
		('Mason Garcia', 'Bulgaria', 'Dunder Mufflin sports club', 1, 0),
		('Zoe Turner', 'UK', 'Boxing Club Bruf', 1, 0),
		('Jackson Harris', 'USA', 'NeverBackDown', 1, 0),
		('Sophia Robinson', 'Jamaica', 'La Boxeur Club', 1, 0),
		('Ethan Turner', 'France', 'TheOfficeFans', 1, 0),
		('Aria Harris', 'Bulgaria', 'Bulgarian Power', 1, 0),
		('Oscar Turner', 'UK', 'Dunder Mufflin sports club', 1, 0),
		('Lily Adams', 'USA', 'Boxing Club Bruf', 1, 0),
		('Lucas Harris', 'Jamaica', 'NeverBackDown', 1, 0),
		('Isabel Turner', 'France', 'La Boxeur Club', 1, 0),
		('Leo Anderson', 'Bulgaria', 'TheOfficeFans', 1, 0),
		('Mia Taylor', 'UK', 'Bulgarian Power', 1, 0),
		('Ella Martin', 'USA', 'Dunder Mufflin sports club', 1, 0),
		('Oliver Davis', 'Jamaica', 'Boxing Club Bruf', 1, 0),
		('Ava Thompson', 'France', 'NeverBackDown', 1, 0),
		('Mason Brown', 'Bulgaria', 'La Boxeur Club', 1, 0),
		('Emma Garcia', 'UK', 'TheOfficeFans', 1, 0),
		('Liam Harris', 'USA', 'Bulgarian Power', 1, 0),
		('Chloe Rodriguez', 'Jamaica', 'Dunder Mufflin sports club', 1, 0),
		('Gabriel Turner', 'France', 'Boxing Club Bruf', 1, 0),
		('Luna Perez', 'Bulgaria', 'NeverBackDown', 1, 0),
		('Maxwell Smith', 'UK', 'La Boxeur Club', 1, 0),
		('Victoria Turner', 'USA', 'TheOfficeFans', 1, 0),
		('Leo Adams', 'Jamaica', 'Bulgarian Power', 1, 0),
		('Penelope White', 'France', 'Dunder Mufflin sports club', 1, 0),
		('Miguel Turner', 'Bulgaria', 'Boxing Club Bruf', 1, 0),
		('Madison Taylor', 'UK', 'NeverBackDown', 1, 0),
		('Daniel Robinson', 'USA', 'La Boxeur Club', 1, 0),
		('Aria Martin', 'Jamaica', 'TheOfficeFans', 1, 0),
		('William Davis', 'France', 'Bulgarian Power', 1, 0),
		('Isabel Turner', 'Bulgaria', 'Dunder Mufflin sports club', 1, 0),
		('Ethan Taylor', 'UK', 'Boxing Club Bruf', 1, 0),
		('Mia Robinson', 'USA', 'NeverBackDown', 1, 0),
		('Noah Garcia', 'Jamaica', 'La Boxeur Club', 1, 0),
		('Sophie Turner', 'France', 'TheOfficeFans', 1, 0),
        ('Ava Turner', 'UK', 'Bulgarian Power', 1, 0),
		('Liam Smith', 'USA', 'Dunder Mufflin sports club', 1, 0),
		('Chloe Davis', 'Jamaica', 'Boxing Club Bruf', 1, 0),
		('Ella Thompson', 'France', 'NeverBackDown', 1, 0),
		('Mason Garcia', 'Bulgaria', 'La Boxeur Club', 1, 0),
		('Zoe Turner', 'UK', 'TheOfficeFans', 1, 0),
		('Jackson Harris', 'USA', 'Bulgarian Power', 1, 0),
		('Sophia Robinson', 'Jamaica', 'Dunder Mufflin sports club', 1, 0),
		('Ethan Turner', 'France', 'Boxing Club Bruf', 1, 0),
		('Aria Harris', 'Bulgaria', 'NeverBackDown', 1, 0),
		('Oscar Turner', 'UK', 'La Boxeur Club', 1, 0),
		('Lily Adams', 'USA', 'TheOfficeFans', 1, 0),
		('Lucas Harris', 'Jamaica', 'Bulgarian Power', 1, 0),
		('Isabel Turner', 'France', 'Dunder Mufflin sports club', 1, 0),
		('Leo Anderson', 'Bulgaria', 'Boxing Club Bruf', 1, 0),
		('Mia Taylor', 'UK', 'NeverBackDown', 1, 0),
		('Ella Martin', 'USA', 'La Boxeur Club', 1, 0),
		('Oliver Davis', 'Jamaica', 'TheOfficeFans', 1, 0),
		('Ava Thompson', 'France', 'Bulgarian Power', 1, 0),
		('Mason Brown', 'Bulgaria', 'Dunder Mufflin sports club', 1, 0),
		('Emma Garcia', 'UK', 'Boxing Club Bruf', 1, 0),
		('Liam Harris', 'USA', 'NeverBackDown', 1, 0),
		('Chloe Rodriguez', 'Jamaica', 'La Boxeur Club', 1, 0),
		('Gabriel Turner', 'France', 'TheOfficeFans', 1, 0),
		('Luna Perez', 'Bulgaria', 'Bulgarian Power', 1, 0),
		('Maxwell Smith', 'UK', 'Dunder Mufflin sports club', 1, 0),
		('Victoria Turner', 'USA', 'Boxing Club Bruf', 1, 0),
		('Leo Adams', 'Jamaica', 'NeverBackDown', 1, 0),
		('Penelope White', 'France', 'La Boxeur Club', 1, 0),
		('Miguel Turner', 'Bulgaria', 'TheOfficeFans', 1, 0),
		('Madison Taylor', 'UK', 'Bulgarian Power', 1, 0),
		('Daniel Robinson', 'USA', 'Dunder Mufflin sports club', 1, 0),
		('Aria Martin', 'Jamaica', 'Boxing Club Bruf', 1, 0),
		('William Davis', 'France', 'NeverBackDown', 1, 0),
		('Isabel Turner', 'Bulgaria', 'La Boxeur Club', 1, 0),
		('Ethan Taylor', 'UK', 'TheOfficeFans', 1, 0),
		('Mia Robinson', 'USA', 'Bulgarian Power', 1, 0),
		('Noah Garcia', 'Jamaica', 'Dunder Mufflin sports club', 1, 0),
		('Sophie Turner', 'France', 'Boxing Club Bruf', 1, 0),
		('Oliver White', 'Bulgaria', 'NeverBackDown', 1, 0),
		('Ava Turner', 'UK', 'La Boxeur Club', 1, 0),
		('Liam Smith', 'USA', 'TheOfficeFans', 1, 0),
		('Chloe Davis', 'Jamaica', 'Bulgarian Power', 1, 0),
		('Ella Thompson', 'France', 'Dunder Mufflin sports club', 1, 0),
		('Mason Garcia', 'Bulgaria', 'Boxing Club Bruf', 1, 0),
		('Zoe Turner', 'UK', 'NeverBackDown', 1, 0),
		('Jackson Harris', 'USA', 'La Boxeur Club', 1, 0),
		('Sophia Robinson', 'Jamaica', 'TheOfficeFans', 1, 0),
		('Ethan Turner', 'France', 'Bulgarian Power', 1, 0),
		('Aria Harris', 'Bulgaria', 'Dunder Mufflin sports club', 1, 0),
		('Oscar Turner', 'UK', 'Boxing Club Bruf', 1, 0),
		('Lily Adams', 'USA', 'NeverBackDown', 1, 0),
		('Lucas Harris', 'Jamaica', 'La Boxeur Club', 1, 0),
		('Isabel Turner', 'France', 'TheOfficeFans', 1, 0),
		('Leo Anderson', 'Bulgaria', 'Bulgarian Power', 1, 0),
		('Mia Taylor', 'UK', 'Dunder Mufflin sports club', 1, 0),
		('Ella Martin', 'USA', 'Boxing Club Bruf', 1, 0),
		('Oliver Davis', 'Jamaica', 'NeverBackDown', 1, 0),
		('Ava Thompson', 'France', 'La Boxeur Club', 1, 0),
		('Mason Brown', 'Bulgaria', 'TheOfficeFans', 1, 0),
		('Emma Garcia', 'UK', 'Bulgarian Power', 1, 0),
		('Liam Harris', 'USA', 'Dunder Mufflin sports club', 1, 0),
		('Chloe Rodriguez', 'Jamaica', 'Boxing Club Bruf', 1, 0),
		('Gabriel Turner', 'France', 'NeverBackDown', 1, 0),
		('Luna Perez', 'Bulgaria', 'La Boxeur Club', 1, 0),
		('Maxwell Smith', 'UK', 'TheOfficeFans', 1, 0),
		('Victoria Turner', 'USA', 'Bulgarian Power', 1, 0),
		('Leo Adams', 'Jamaica', 'Dunder Mufflin sports club', 1, 0),
		('Penelope White', 'France', 'Boxing Club Bruf', 1, 0),
		('Miguel Turner', 'Bulgaria', 'NeverBackDown', 1, 0),
		('Madison Taylor', 'UK', 'La Boxeur Club', 1, 0),
		('Daniel Robinson', 'USA', 'TheOfficeFans', 1, 0),
		('Aria Martin', 'Jamaica', 'Bulgarian Power', 1, 0);




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





