ALTER TABLE match_score_db.admin_requests AUTO_INCREMENT = 1;
ALTER TABLE match_score_db.dates AUTO_INCREMENT = 1;
ALTER TABLE match_score_db.matches AUTO_INCREMENT = 1;
ALTER TABLE match_score_db.players AUTO_INCREMENT = 1;
ALTER TABLE match_score_db.players_statistics AUTO_INCREMENT = 1;
ALTER TABLE match_score_db.teams AUTO_INCREMENT = 1;
ALTER TABLE match_score_db.teams_statistics AUTO_INCREMENT = 1;
ALTER TABLE match_score_db.tournaments AUTO_INCREMENT = 1;
ALTER TABLE match_score_db.tournaments_matches AUTO_INCREMENT = 1;
ALTER TABLE match_score_db.users AUTO_INCREMENT = 1;


-- DATES
-- ----------------------------------------------------------------------------------
INSERT INTO match_score_db.dates (date) VALUES ('2020-1-1');





-- USERS
-- ----------------------------------------------------------------------------------
INSERT INTO match_score_db.users (full_name, email, password, gender, role, players_id) 
VALUES  ('Steven Atkinson', 'steven.atkinson@gmail.com', '2fca7af39df396e0890de73cf93628cc50261c1c5bff980995ce740279a740f9', 'male', 'admin', null),
	    ('Michael Scott', 'michael.scott@gmail.com', 'd24259be13407e0d132337bd8398ee9aaff43a249c38d0bf222429f311c9c939', 'male', 'director', null),
        ('Pamela Beasly', 'pamela.beasly@gmail.com', '78d7ba5153684388785609ab6fc8beafa7d63c394481026999f6ccf420d9ab9a', 'female', 'director', null),
		('Jim Halpert', 'jim.halpert@gmail.com', '3cb7aff2146cd44bbdef023e465424e3c4a6ac793b7fa250c8895d93065ec53c', 'male', 'director', null),
		('Owen Garrett', 'owen.garrett@yahoo.com', 'c2b41017a8036252bb2308ea026284ffd455a9eab57c4b65777fbcd0ac891964', 'male', 'spectator', null),
		('Kyan Chandler', 'chandler_kyan@gmx.de', 'c53c1c5f81b36257b951965239ef46c1c6e6fbb4d4eb01cee58b6dc9bc2ae80c', 'male', 'spectator', null),
		('Frank Warren', 'warwarbinks@gmail.com', '74fca0325b5fdb3a34badb40a2581cfbd5344187e8d3432952a5abc0929c1246', 'male', 'spectator', null),
		('Susan Wilkinson', 'suuusan_123@abv.bg', 'ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f', 'female', 'spectator', null);





-- TEAMS
-- ----------------------------------------------------------------------------------
INSERT INTO match_score_db.teams (team_name, number_of_players, owners_id)
VALUES	('Team 1', 5, 2),
		('Team 2', 5, 3),
		('Team 3', 5, 3),
		('Team 4', 5, 3),
		('Team 5', 5, 3),
		('Team 6', 5, 3),
		('Team 7', 5, 3),
		('Team 8', 5, 3),
		('Team 9', 5, 3),
		('Team 10', 5, 3),
		('Team 11', 5, 3),
		('Team 12', 5, 3),
		('Team 13', 5, 3),
		('Team 14', 5, 3),
		('Team 15', 5, 3),
		('Team 16', 5, 3);
 
-- MATCHES 
INSERT INTO match_score_db.matches (format, game_type, participant_1, participant_2, date, winner, tournament_name)
VALUES	('time limit', 'one on one', 'Owen Garrett', 'Jack Thompso', '2022-1-2', 'not played', null),   
		('time limit', 'one on one', 'Owen Garrett', 'Elena Petrova', '2022-1-2', 'not played', null),        
		('time limit', 'one on one', 'Owen Garrett', 'Pam Beasly', '2022-1-2', 'not played', null),        
		('time limit', 'one on one', 'Owen Garrett', 'Carlos Rodriguez', '2022-1-2', 'not played', null),        
		('time limit', 'one on one', 'Owen Garrett', 'Julian Scott', '2022-1-2', 'not played', null),        
		('time limit', 'one on one', 'Owen Garrett', 'Natalie Brown', '2022-1-2', 'not played', null);        






-- PLAYERS
-- ----------------------------------------------------------------------------------
INSERT INTO match_score_db.players (full_name, country, sports_club, is_active, is_connected, teams_id) 
VALUES  ('Michael Scott', 'Jamaica', 'Dunder Mufflin sports club', 1, 0, 1),
	    ('Pam Beasly', 'France', 'La Boxeur Club', 1, 0, 1),
	    ('Jim Halpert', 'USA', 'TheOfficeFans', 1, 0, 1),
		('Frank Warren', 'USA', 'NeverBackDown', 1, 0, 1),
		('Susan Wilkinson', 'Bulgaria', 'Bulgarian Power', 1, 0, 1),
        
		('Owen Garrett', 'UK', 'Boxing Club Bruf', 1, 0, 2),
        ('Jack Thompson', 'USA', 'NeverBackDown', 1, 0, 2),
		('Sophie Williams', 'Jamaica', 'La Boxeur Club', 1, 0, 2),
		('Antoine Martin', 'France', 'TheOfficeFans', 1, 0, 2),
		('Elena Petrova', 'Bulgaria', 'Bulgarian Power', 1, 0, 2),
        
		('Oliver Smith', 'UK', 'Dunder Mufflin sports club', 1, 0, 3),
		('Isabella Davis', 'USA', 'Boxing Club Bruf', 1, 0, 3),
		('Carlos Rodriguez', 'Jamaica', 'NeverBackDown', 1, 0, 3),
		('Camille Dupont', 'France', 'La Boxeur Club', 1, 0, 3),
		('Dimitar Ivanov', 'Bulgaria', 'TheOfficeFans', 1, 0, 3),
        
		('Grace White', 'UK', 'Bulgarian Power', 1, 0, 4),
		('Mason Taylor', 'USA', 'Dunder Mufflin sports club', 1, 0, 4),
		('Ava Robinson', 'Jamaica', 'Boxing Club Bruf', 1, 0, 4),
		('Lucas Garcia', 'France', 'NeverBackDown', 1, 0, 4),
		('Isabel Turner', 'Bulgaria', 'NeverBackDown', 1, 0, 4),
		
        ('Stella Johnson', 'Bulgaria', 'La Boxeur Club', 1, 0, 5),
		('Liam Anderson', 'UK', 'TheOfficeFans', 1, 0, 5),
		('Natalie Brown', 'USA', 'Bulgarian Power', 1, 0, 5),
		('Diego Martinez', 'Jamaica', 'Dunder Mufflin sports club', 1, 0, 5),
		('Emma Wilson', 'France', 'Boxing Club Bruf', 1, 0, 5),
		
        ('Eva Harris', 'Bulgaria', 'NeverBackDown', 1, 0, 6),
		('Aiden Clark', 'UK', 'La Boxeur Club', 1, 0, 6),
		('Zoe Green', 'USA', 'TheOfficeFans', 1, 0, 6),
		('Julian Scott', 'Jamaica', 'Bulgarian Power', 1, 0, 6),
		('Sophia King', 'France', 'Dunder Mufflin sports club', 1, 0, 6),
		
        ('Landon Miller', 'Bulgaria', 'Boxing Club Bruf', 1, 0, 7),
		('Chloe Adams', 'UK', 'NeverBackDown', 1, 0, 7),
		('Gabriel Turner', 'USA', 'La Boxeur Club', 1, 0, 7),
		('Luna Martinez', 'Jamaica', 'TheOfficeFans', 1, 0, 7),
		('Maxwell Harris', 'France', 'Bulgarian Power', 1, 0, 7),
		
        ('Victoria Thomas', 'Bulgaria', 'Dunder Mufflin sports club', 1, 0, 8),
		('Leo Garcia', 'UK', 'Boxing Club Bruf', 1, 0, 8),
		('Penelope White', 'USA', 'NeverBackDown', 1, 0, 8),
		('Miguel Rodriguez', 'Jamaica', 'La Boxeur Club', 1, 0, 8),
		('Madison Lewis', 'France', 'TheOfficeFans', 1, 0, 8),
		
        ('Daniel Turner', 'Bulgaria', 'Bulgarian Power', 1, 0, 9),
		('Aria Davis', 'UK', 'Dunder Mufflin sports club', 1, 0, 9),
		('William Scott', 'USA', 'Boxing Club Bruf', 1, 0, 9),
		('Isabel Brown', 'Jamaica', 'NeverBackDown', 1, 0, 9),
        ('William Davis', 'France', 'Boxing Club Bruf', 1, 0, 9),

        ('Ethan Taylor', 'France', 'La Boxeur Club', 1, 0, 10),
		('Mia Wilson', 'Bulgaria', 'TheOfficeFans', 1, 0, 10),
		('Noah Turner', 'UK', 'Bulgarian Power', 1, 0, 10),
		('Sophie Robinson', 'USA', 'Dunder Mufflin sports club', 1, 0, 10),
		('Oliver Miller', 'Jamaica', 'Boxing Club Bruf', 1, 0, 10),
		
        ('Ava Perez', 'France', 'NeverBackDown', 1, 0, 11),
		('Lucas Adams', 'Bulgaria', 'La Boxeur Club', 1, 0, 11),
		('Emma Thomas', 'UK', 'TheOfficeFans', 1, 0, 11),
		('Liam Harris', 'USA', 'Bulgarian Power', 1, 0, 11),
		('Chloe Martin', 'Jamaica', 'Dunder Mufflin sports club', 1, 0, 11),
		
        ('Ella Turner', 'France', 'Boxing Club Bruf', 1, 0, 12),
		('Mason Robinson', 'Bulgaria', 'NeverBackDown', 1, 0, 12),
		('Zoe Garcia', 'UK', 'La Boxeur', 1, 0, 12),
        ('Jackson White', 'USA', 'TheOfficeFans', 1, 0, 12),
        ('Aria Martin', 'Jamaica', 'Dunder Mufflin sports club', 1, 0, 12),
		
        ('Sophia Garcia', 'Jamaica', 'Bulgarian Power', 1, 0, 13),
		('Ethan Robinson', 'France', 'Dunder Mufflin sports club', 1, 0, 13),
		('Aria Smith', 'Bulgaria', 'Boxing Club Bruf', 1, 0, 13),
		('Oscar Turner', 'UK', 'NeverBackDown', 1, 0, 13),
		('Lily Martinez', 'USA', 'La Boxeur Club', 1, 0, 13),
		
        ('Lucas Harris', 'Jamaica', 'TheOfficeFans', 1, 0, 14),
		('Isabel Turner', 'France', 'Bulgarian Power', 1, 0, 14),
		('Leo Anderson', 'Bulgaria', 'Dunder Mufflin sports club', 1, 0, 14),
		('Mia Taylor', 'UK', 'Boxing Club Bruf', 1, 0, 14),
		('Ella Martin', 'USA', 'NeverBackDown', 1, 0, 14),
		
        ('Oliver Davis', 'Jamaica', 'La Boxeur Club', 1, 0, 15),
		('Ava Thompson', 'France', 'TheOfficeFans', 1, 0, 15),
		('Mason Brown', 'Bulgaria', 'Bulgarian Power', 1, 0, 15),
		('Emma Garcia', 'UK', 'Dunder Mufflin sports club', 1, 0, 15),
		('Liam Harris', 'USA', 'Boxing Club Bruf', 1, 0, 15),
		
        ('Chloe Rodriguez', 'Jamaica', 'NeverBackDown', 1, 0, 16),
		('Gabriel Turner', 'France', 'La Boxeur Club', 1, 0, 16),
		('Luna Perez', 'Bulgaria', 'TheOfficeFans', 1, 0, 16),
		('Maxwell Smith', 'UK', 'Bulgarian Power', 1, 0, 16),
		('Victoria Turner', 'USA', 'Dunder Mufflin sports club', 1, 0, 16),
		
        ('Leo Adams', 'Jamaica', 'Boxing Club Bruf', 1, 0, null),
		('Penelope White', 'France', 'NeverBackDown', 1, 0, null),
		('Miguel Turner', 'Bulgaria', 'La Boxeur Club', 1, 0, null),
		('Madison Taylor', 'UK', 'TheOfficeFans', 1, 0, null),
		('Daniel Robinson', 'USA', 'Bulgarian Power', 1, 0, null),
		
		('Ethan Taylor', 'UK', 'La Boxeur Club', 1, 0, null),
		('Mia Robinson', 'USA', 'TheOfficeFans', 1, 0, null),
		('Noah Garcia', 'Jamaica', 'Bulgarian Power', 1, 0, null),
		('Sophie Turner', 'France', 'Dunder Mufflin sports club', 1, 0, null),
		('Oliver White', 'Bulgaria', 'Boxing Club Bruf', 1, 0, null),

		('Ava Turner', 'UK', 'NeverBackDown', 1, 0, null),
		('Liam Smith', 'USA', 'La Boxeur Club', 1, 0, null),
		('Chloe Davis', 'Jamaica', 'TheOfficeFans', 1, 0, null),
		('Ella Thompson', 'France', 'Bulgarian Power', 1, 0, null),
		('Mason Garcia', 'Bulgaria', 'Dunder Mufflin sports club', 1, 0, null),

		('Zoe Turner', 'UK', 'Boxing Club Bruf', 1, 0, null),
		('Jackson Harris', 'USA', 'NeverBackDown', 1, 0, null),
		('Sophia Robinson', 'Jamaica', 'La Boxeur Club', 1, 0, null),
		('Ethan Turner', 'France', 'TheOfficeFans', 1, 0, null),
		('Aria Harris', 'Bulgaria', 'Bulgarian Power', 1, 0, null);


        
        

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





