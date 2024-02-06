ALTER TABLE match_score_db.admin_requests AUTO_INCREMENT = 1;

ALTER TABLE match_score_db.matches AUTO_INCREMENT = 1;
ALTER TABLE match_score_db.players AUTO_INCREMENT = 1;
ALTER TABLE match_score_db.players_statistics AUTO_INCREMENT = 1;
ALTER TABLE match_score_db.teams AUTO_INCREMENT = 1;
ALTER TABLE match_score_db.teams_statistics AUTO_INCREMENT = 1;
ALTER TABLE match_score_db.tournaments AUTO_INCREMENT = 1;
-- ALTER TABLE match_score_db.tournaments_players AUTO_INCREMENT = 1;
-- ALTER TABLE match_score_db.tournaments_teams AUTO_INCREMENT = 1;
ALTER TABLE match_score_db.users AUTO_INCREMENT = 1;




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
INSERT INTO match_score_db.players (full_name, country, sports_club, is_active, is_connected, teams_id) 
VALUES	("Aleksandar Dimitrov",  "Bulgarina",  "Bulgarian Power",  "0",  "1",  "1"),
		("Georgi Ivanov",  "Bulgarina",  "Bulgarian Power",  "0",  "1",  "1"),
		("Stefan Petrov",  "Bulgarina",  "Bulgarian Power",  "0",  "1",  "1"),
		("MartinStoyanov",  "Bulgarina",  "Bulgarian Power",  "0",  "1",  "1"),
		("Nikolay Vasilev",  "Bulgarina",  "Bulgarian Power",  "0",  "1",  "1"),
		("Adam Smith",  "UK",  "Man City",  "0",  "0",  "2"),
		("Benjamin Taylor",  "UK",  "Man City",  "0",  "0",  "2"),
		("Christopher Harris",  "UK",  "Man City",  "0",  "0",  "2"),
		("David Robinson",  "UK",  "Man City",  "0",  "0",  "2"),
		("Edward Turner",  "UK",  "Man City",  "0",  "0",  "2"),
		("Andre Brown",  "Jamaica",  "Jam RC Club",  "0",  "0",  "3"),
		("Christopher Campbell",  "Jamaica",  "Jam RC Club",  "0",  "0",  "3"),
		("David Foster",  "Jamaica",  "Jam RC Club",  "0",  "0",  "3"),
		("Marcus Mitchell",  "Jamaica",  "Jam RC Club",  "0",  "0",  "3"),
		("Sean Thompson",  "Jamaica",  "Jam RC Club",  "0",  "0",  "3"),
		("Achille Bernard",  "France",  "L’Usine",  "0",  "0",  "4"),
		("Etienne Durand",  "France",  "L’Usine",  "0",  "0",  "4"),
		("Gaston Lefevre",  "France",  "L’Usine",  "0",  "0",  "4"),
		("Lucas Moreau",  "France",  "L’Usine",  "0",  "0",  "4"),
		("Romain Olivier",  "France",  "L’Usine",  "0",  "0",  "4"),
		("Adrianus Silva",  "Portugal",  "Benefica",  "0",  "0",  "5"),
		("Brunus Costa",  "Portugal",  "Benefica",  "0",  "0",  "5"),
		("Claudius Pereira",  "Portugal",  "Benefica",  "0",  "0",  "5"),
		("Darius Santos",  "Portugal",  "Benefica",  "0",  "0",  "5"),
		("Eduardus Fernandes",  "Portugal",  "Benefica",  "0",  "0",  "5"),
		("Aemilius Tullius",  "USA",  "Boston Celtics",  "0",  "0",  "6"),
		("Cornelius Augustinus",  "USA",  "Boston Celtics",  "0",  "0",  "6"),
		("Gaius Antonius",  "USA",  "Boston Celtics",  "0",  "0",  "6"),
		("Lucius Cassius",  "USA",  "Boston Celtics",  "0",  "0",  "6"),
		("Quintus Octavius",  "USA",  "Boston Celtics",  "0",  "0",  "6"),
		("Adrian Ionescu",  "Romania",  " Steaua Bucharest",  "0",  "0",  "7"),
		("Bogdan Marinescu",  "Romania",  " Steaua Bucharest",  "0",  "0",  "7"),
		("Cristian Popescu",  "Romania",  " Steaua Bucharest",  "0",  "0",  "7"),
		("Dragos Radulescu",  "Romania",  " Steaua Bucharest",  "0",  "0",  "7"),
		("Emil Vasilescu",  "Romania",  " Steaua Bucharest",  "0",  "0",  "7"),
		("Carlos Alvarez",  "Spain",  "Barcelona",  "0",  "0",  "8"),
		("Diego Fernandez",  "Spain",  "Barcelona",  "0",  "0",  "8"),
		("Javier Garcia",  "Spain",  "Barcelona",  "0",  "0",  "8"),
		("Miguel Rodriguez",  "Spain",  "Barcelona",  "0",  "0",  "8"),
		("Pedro Sanchez",  "Spain",  "Barcelona",  "0",  "0",  "8"),
		("Adamus Kowalskius",  "Poland",  "KS Rakow",  "0",  "0",  "9"),
		("Bartosz Nowak",  "Poland",  "KS Rakow",  "0",  "0",  "9"),
		("Czeslaw Wojciechowski",  "Poland",  "KS Rakow",  "0",  "0",  "9"),
		("Dariusz Szymanski",  "Poland",  "KS Rakow",  "0",  "0",  "9"),
		("Emilian Jankowski",  "Poland",  "KS Rakow",  "0",  "0",  "9"),
		("Alexander Becker",  "Germany",  "Bayer Leverkusen",  "0",  "0",  "10"),
		("Felix Berger",  "Germany",  "Bayer Leverkusen",  "0",  "0",  "10"),
		("Lukas Fischer",  "Germany",  "Bayer Leverkusen",  "0",  "0",  "10"),
		("Maximilian Muller",  "Germany",  "Bayer Leverkusen",  "0",  "0",  "10"),
		("Sebastian Schmidt",  "Germany",  "Bayer Leverkusen",  "0",  "0",  "10");



