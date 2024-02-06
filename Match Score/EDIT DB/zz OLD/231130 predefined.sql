


-- Insert initial data into the teams table
-- ----------------------------------------------------------------------------------
INSERT INTO match_score_db.teams (team_name, number_of_players)
VALUES	('Bulgarian Power', 5),
		('Man City', 5),
		('Jam RC Club', 5),
		('L’Usine', 5),
		('Benefica', 5),
		('Boston Celtics', 5),
		('Steaua Bucharest', 5),
		('Barcelona', 5),
		('KS Rakow', 5),
		('Bayer Leverkusen', 5);
        
        

-- Insert initial data into the players table
-- ----------------------------------------------------------------------------------
INSERT INTO match_score_db.players (full_name, country, sports_club, is_active, is_connected, teams_id, blocked_players_id) 
VALUES	("Michael Scott", "Jamaica",  'Dunder Mufflin sports club',  "0",  "1", null, null),
		("Pamela Beasly", "France",  'La Sport Club',  "1",  "1", null, null),
		("Jim Halpert", "USA",  'TheOfficeFans',  "0",  "1", null, null),
		("Frank Warren", "USA",  'NeverBackDown',  "0",  "1", null, null),
		("Toshko Yordanov", "Bulgaria",  'Bulgarian Power',  "0",  "0", null, null),
		("Owen Garrett", "UK",  'Sports Club Bruf',  "0",  "1", null, null),

		("Aleksandar Dimitrov", "Bulgaria", "Bulgarian Power", "0", "0", "1", null),
		("Georgi Ivanov", "Bulgaria", "Bulgarian Power", "0", "0", "1", null),
		("Stefan Petrov", "Bulgaria", "Bulgarian Power", "0", "0", "1", null),
		("MartinStoyanov", "Bulgaria", "Bulgarian Power", "0", "0", "1", null),
		("Nikolay Vasilev", "Bulgaria", "Bulgarian Power", "0", "0", "1", null),
		("Adam Smith", "UK", "Man City", "0", "0", "2", null),
		("Benjamin Taylor", "UK", "Man City", "0", "0", "2", null),
		("Christopher Harris", "UK", "Man City", "0", "0", "2", null),
		("David Robinson", "UK", "Man City", "0", "0", "2", null),
		("Edward Turner", "UK", "Man City", "0", "0", "2", null),
		("Andre Brown", "Jamaica", "Jam RC Club", "0", "0", "3", null),
		("Christopher Campbell", "Jamaica", "Jam RC Club", "0", "0", "3", null),
		("David Foster", "Jamaica", "Jam RC Club", "0", "0", "3", null),
		("Marcus Mitchell", "Jamaica", "Jam RC Club", "0", "0", "3", null),
		("Sean Thompson", "Jamaica", "Jam RC Club", "0", "0", "3", null),
		("Achille Bernard", "France", "L’Usine", "0", "0", "4", null),
		("Etienne Durand", "France", "L’Usine", "0", "0", "4", null),
		("Gaston Lefevre", "France", "L’Usine", "0", "0", "4", null),
		("Lucas Moreau", "France", "L’Usine", "0", "0", "4", null),
		("Romain Olivier", "France", "L’Usine", "0", "0", "4", null),
		("Adrianus Silva", "Portugal", "Benefica", "0", "0", "5", null),
		("Brunus Costa", "Portugal", "Benefica", "0", "0", "5", null),
		("Claudius Pereira", "Portugal", "Benefica", "0", "0", "5", null),
		("Darius Santos", "Portugal", "Benefica", "0", "0", "5", null),
		("Eduardus Fernandes", "Portugal", "Benefica", "0", "0", "5", null),
		("Aemilius Tullius", "USA", "Boston Celtics", "0", "0", "6", null),
		("Cornelius Augustinus", "USA", "Boston Celtics", "0", "0", "6", null),
		("Gaius Antonius", "USA", "Boston Celtics", "0", "0", "6", null),
		("Lucius Cassius", "USA", "Boston Celtics", "0", "0", "6", null),
		("Quintus Octavius", "USA", "Boston Celtics", "0", "0", "6", null),
		("Adrian Ionescu", "Romania", " Steaua Bucharest", "0", "0", "7", null),
		("Bogdan Marinescu", "Romania", " Steaua Bucharest", "0", "0", "7", null),
		("Cristian Popescu", "Romania", " Steaua Bucharest", "0", "0", "7", null),
		("Dragos Radulescu", "Romania", " Steaua Bucharest", "0", "0", "7", null),
		("Emil Vasilescu", "Romania", " Steaua Bucharest", "0", "0", "7", null),
		("Carlos Alvarez", "Spain", "Barcelona", "0", "0", "8", null),
		("Diego Fernandez", "Spain", "Barcelona", "0", "0", "8", null),
		("Javier Garcia", "Spain", "Barcelona", "0", "0", "8", null),
		("Miguel Rodriguez", "Spain", "Barcelona", "0", "0", "8", null),
		("Pedro Sanchez", "Spain", "Barcelona", "0", "0", "8", null),
		("Adamus Kowalskius", "Poland", "KS Rakow", "0", "0", "9", null),
		("Bartosz Nowak", "Poland", "KS Rakow", "0", "0", "9", null),
		("Czeslaw Wojciechowski", "Poland", "KS Rakow", "0", "0", "9", null),
		("Dariusz Szymanski", "Poland", "KS Rakow", "0", "0", "9", null),
		("Emilian Jankowski", "Poland", "KS Rakow", "0", "0", "9", null),
		("Alexander Becker", "Germany", "Bayer Leverkusen", "0", "0", "10", null),
		("Felix Berger", "Germany", "Bayer Leverkusen", "0", "0", "10", null),
		("Lukas Fischer", "Germany", "Bayer Leverkusen", "0", "0", "10", null),
		("Maximilian Muller", "Germany", "Bayer Leverkusen", "0", "0", "10", null),
		("Sebastian Schmidt", "Germany", "Bayer Leverkusen", "0", "0", "10", null);




-- Insert initial data into the users table
INSERT INTO match_score_db.users (full_name, email, password, gender, role, players_id, is_verified, verification_code) 
VALUES ('Steven Atkinson', 'steven.atkinson@gmail.com', '2fca7af39df396e0890de73cf93628cc50261c1c5bff980995ce740279a740f9', 'male', 'admin', null, '1', '123450'),
       ('Michael Scott', 'michael.scott@gmail.com', 'd24259be13407e0d132337bd8398ee9aaff43a249c38d0bf222429f311c9c939', 'male', 'director', '1', '1', '123451'),
       ('Pamela Beasly', 'pamela.beasly@gmail.com', '78d7ba5153684388785609ab6fc8beafa7d63c394481026999f6ccf420d9ab9a', 'female', 'director', '2', '1', '123452'),
       ('Jim Halpert', 'jim.halpert@gmail.com', '3cb7aff2146cd44bbdef023e465424e3c4a6ac793b7fa250c8895d93065ec53c', 'male', 'director', '3', '1', '123453'),
       ('Owen Garrett', 'owen.garrett@yahoo.com', 'c2b41017a8036252bb2308ea026284ffd455a9eab57c4b65777fbcd0ac891964', 'male', 'spectator', null, '1', '123454'),
       ('Kyan Chandler', 'chandler_kyan@gmx.de', 'c53c1c5f81b36257b951965239ef46c1c6e6fbb4d4eb01cee58b6dc9bc2ae80c', 'male', 'spectator', null, '1', '123455'),
       ('Frank Warren', 'warwarbinks@gmail.com', '74fca0325b5fdb3a34badb40a2581cfbd5344187e8d3432952a5abc0929c1246', 'male', 'player', '4', '1', '123456'),
       ('Susan Wilkinson', 'suuusan_123@abv.bg', 'ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f', 'female', 'player', null, '1', '123457');



-- Insert initial data into the matches table
-- ----------------------------------------------------------------------------------
-- INSERT INTO match_score_db.matches (match_format, game_type, sport, participant_1, participant_2, , creator, date, winner, tournament_name, stage)
-- VALUES	('score limit',	'one on one', 'Boxing',	'Jim Halpert',	'-----------', 'Steven Atkinson',	'2023-01-01', 'not played', 'not part of a tournament',	'0')



-- Insert initial data into the tournaments table
-- ----------------------------------------------------------------------------------
-- INSERT INTO match_score_db.tournaments (title, format, date, prize, game_type, users_creator_id, is_finished)
-- VALUES ('first tournament', 'knockout', '2023-1-20', 10, 'one on one', 1, 0);


-- Insert initial data into the admin_requests table
-- ----------------------------------------------------------------------------------
INSERT INTO match_score_db.admin_requests (type_of_request, players_id, users_id, status)
VALUES ('connection', 6, 5, 'pending');


