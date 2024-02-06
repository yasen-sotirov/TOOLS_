-- Insert initial data into the teams table
-- ----------------------------------------------------------------------------------
INSERT INTO match_score_db.teams (team_name, number_of_players, owners_id)
VALUES	('Bulgarian Power', 5, 2),
		('Man City', 5, 3),
		('Jam RC Club', 5, 3),
		('L’Usine', 5, 3),
		('Benefica', 5, 3),
		('Boston Celtics', 5, 3),
		('Steaua Bucharest', 5, 3),
		('Barcelona', 5, 3),
		('KS Rakow', 5, 3),
		('Bayer Leverkusen', 5, 3);
        
        

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





50 row(s) affected, 64 warning(s): 1265 Data truncated for column 'is_active' at row 1 1265 Data truncated for column 'is_connected' at row 1 1265 Data truncated for column 'teams_id' at row 1 1265 Data truncated for column 'is_active' at row 2 1265 Data truncated for column 'is_connected' at row 2 1265 Data truncated for column 'teams_id' at row 2 1265 Data truncated for column 'is_active' at row 3 1265 Data truncated for column 'is_connected' at row 3 1265 Data truncated for column 'teams_id' at row 3 1265 Data truncated for column 'is_active' at row 4 1265 Data truncated for column 'is_connected' at row 4 1265 Data truncated for column 'teams_id' at row 4 1265 Data truncated for column 'is_active' at row 5 1265 Data truncated for column 'is_connected' at row 5 1265 Data truncated for column 'teams_id' at row 5 1265 Data truncated for column 'is_active' at row 6 1265 Data truncated for column 'is_connected' at row 6 1265 Data truncated for column 'teams_id' at row 6 1265 Data truncated for column 'is_active' at row 7 1265 Data truncated for column 'is_connected' at row 7 1265 Data truncated for column 'teams_id' at row 7 1265 Data truncated for column 'is_active' at row 8 1265 Data truncated for column 'is_connected' at row 8 1265 Data truncated for column 'teams_id' at row 8 1265 Data truncated for column 'is_active' at row 9 1265 Data truncated for column 'is_connected' at row 9 1265 Data truncated for column 'teams_id' at row 9 1265 Data truncated for column 'is_active' at row 10 1265 Data truncated for column 'is_connected' at row 10 1265 Data truncated for column 'teams_id' at row 10 1265 Data truncated for column 'is_active' at row 11 1265 Data truncated for column 'is_connected' at row 11 1265 Data truncated for column 'teams_id' at row 11 1265 Data truncated for column 'is_active' at row 12 1265 Data truncated for column 'is_connected' at row 12 1265 Data truncated for column 'teams_id' at row 12 1265 Data truncated for column 'is_active' at row 13 1265 Data truncated for column 'is_connected' at row 13 1265 Data truncated for column 'teams_id' at row 13 1265 Data truncated for column 'is_active' at row 14 1265 Data truncated for column 'is_connected' at row 14 1265 Data truncated for column 'teams_id' at row 14 1265 Data truncated for column 'is_active' at row 15 1265 Data truncated for column 'is_connected' at row 15 1265 Data truncated for column 'teams_id' at row 15 1265 Data truncated for column 'is_active' at row 16 1265 Data truncated for column 'is_connected' at row 16 1265 Data truncated for column 'teams_id' at row 16 1265 Data truncated for column 'is_active' at row 17 1265 Data truncated for column 'is_connected' at row 17 1265 Data truncated for column 'teams_id' at row 17 1265 Data truncated for column 'is_active' at row 18 1265 Data truncated for column 'is_connected' at row 18 1265 Data truncated for column 'teams_id' at row 18 1265 Data truncated for column 'is_active' at row 19 1265 Data truncated for column 'is_connected' at row 19 1265 Data truncated for column 'teams_id' at row 19 1265 Data truncated for column 'is_active' at row 20 1265 Data truncated for column 'is_connected' at row 20 1265 Data truncated for column 'teams_id' at row 20 1265 Data truncated for column 'is_active' at row 21 1265 Data truncated for column 'is_connected' at row 21 1265 Data truncated for column 'teams_id' at row 21 1265 Data truncated for column 'is_active' at row 22 Records: 50  Duplicates: 0  Warnings: 150
