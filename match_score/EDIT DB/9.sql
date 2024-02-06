INSERT INTO match_score_db.tournaments (id, title, number_participants, t_format, match_format, sport, date, prize, game_type, winner, users_creator_id, is_complete, stage)
VALUES	('1', 'tournament 1', '8', 'knockout', 'score limit', 'tennis', '2023-2-2', '10000', 'one on one', 'Liam Anderson', '1', '1', '3');


INSERT INTO match_score_db.matches (id, match_format, game_type, sport, participant_1, participant_2, creator, date, winner, tournament_name, stage)
VALUES	('1', 'score limit', 'one on one', 'tennis', 'Dimitar Ivanov', 'Liam Anderson', 'Steven Atkinson', '2023-2-2', 'Liam Anderson', 'tournament 1', '1'),
		('2', 'score limit', 'one on one', 'tennis', 'Oliver Smith', 'Diego Martinez', 'Steven Atkinson', '2023-2-2', 'Oliver Smith', 'tournament 1', '1'),
		('3', 'score limit', 'one on one', 'tennis', 'Carlos Rodriguez', 'Frank Warren', 'Steven Atkinson', '2023-2-2', 'Frank Warren', 'tournament 1', '1'),
		('4', 'score limit', 'one on one', 'tennis', 'Mason Taylor', 'Jack Thompson', 'Steven Atkinson', '2023-2-2', 'Jack Thompson', 'tournament 1', '1'),
        
		('5', 'score limit', 'one on one', 'tennis', 'Liam Anderson', 'Oliver Smith', 'Steven Atkinson', '2023-2-4', 'Liam Anderson', 'tournament 1', '2'),
		('6', 'score limit', 'one on one', 'tennis', 'Frank Warren', 'Jack Thompson', 'Steven Atkinson', '2023-2-4', 'Jack Thompson', 'tournament 1', '2'),
        
		('7', 'score limit', 'one on one', 'tennis', 'Liam Anderson', 'Jack Thompson', 'Steven Atkinson', '2023-2-6', 'Liam Anderson', 'tournament 1', '3');
        


INSERT INTO match_score_db.tournaments_players (players_id, tournaments_id, tournaments_title, player_name, stage)
VALUES	('15', '1', 'tournament 1', 'Dimitar Ivanov', '1'),
		('21', '1', 'tournament 1', 'Liam Anderson', '1'),
		('11', '1', 'tournament 1', 'Oliver Smith', '1'),
		('23', '1', 'tournament 1', 'Diego Martinez', '1'),
		('13', '1', 'tournament 1', 'Carlos Rodriguez', '1'),
		('4', '1', 'tournament 1', 'Frank Warren', '1'),
		('17', '1', 'tournament 1', 'Mason Taylor', '1'),
		('7', '1', 'tournament 1', 'Jack Thompson', '1'),
        
        ('21', '1', 'tournament 1', 'Liam Anderson', '2'),
        ('11', '1', 'tournament 1', 'Oliver Smith', '2'),
        ('4', '1', 'tournament 1', 'Frank Warren', '2'),
        ('7', '1', 'tournament 1', 'Jack Thompson', '2'),
        
        ('21', '1', 'tournament 1', 'Liam Anderson', '3'),
        ('7', '1', 'tournament 1', 'Jack Thompson', '3');


SELECT * FROM match_score_db.players_statistics;

INSERT INTO match_score_db.players_statistics (players_id, player_name, player_score, opponent_name, opponent_score, win, loss, matches_id, tournament_name, tournament_trophy, stage, date)
VALUES	('15', 'Dimitar Ivanov', '3', 'Liam Anderson', '5',  '0', '1',   '1', 'tournament 1', '0', '1', '2023-2-2'),
		('21', 'Liam Anderson', '5', 'Dimitar Ivanov', '3',  '1', '0',   '1', 'tournament 1', '0', '1', '2023-2-2'),
        
		('11', 'Oliver Smith', '6', 'Diego Martinez', '4',  '1', '0',   '2', 'tournament 1', '0', '1', '2023-2-2'),
		('23', 'Diego Martinez', '4', 'Oliver Smith', '6',  '0', '1',   '2', 'tournament 1', '0', '1', '2023-2-2'),
        
		('13', 'Carlos Rodriguez', '1', 'Frank Warren', '3',  '0', '1',   '3', 'tournament 1', '0', '1', '2023-2-2'),
		('4', 'Frank Warren', '3', 'Carlos Rodriguez', '1',   '1', '0',   '3', 'tournament 1', '0', '1', '2023-2-2'),
        
		('17', 'Mason Taylor', '0', 'Jack Thompson', '5',   '0', '1',   '4', 'tournament 1', '0', '1', '2023-2-2'),
		('7', 'Jack Thompson', '5',   'Mason Taylor', '0',  '1', '0',   '4', 'tournament 1', '0', '1', '2023-2-2'),
        
		('21', 'Liam Anderson', '5', 'Oliver Smith', '4',  '1', '0',   '5', 'tournament 1', '0', '1', '2023-2-4'),
		('11', 'Oliver Smith', '4', 'Liam Anderson', '5',  '0', '1',   '5', 'tournament 1', '0', '1', '2023-2-4'),
        
		('4',  'Frank Warren', '3', 'Jack Thompson', '5',  '0', '1',   '6', 'tournament 1', '0', '1', '2023-2-2'),
		('17', 'Jack Thompson', '5', 'Frank Warren', '3',  '1', '1',   '6', 'tournament 1', '0', '1', '2023-2-2'),
        
        ('21', 'Liam Anderson', '6', 'Jack Thompson', '5',  '1', '0',   '7', 'tournament 1', '0', '1', '2023-2-2'),
        ('17', 'Jack Thompson', '5', 'Liam Anderson', '6',  '1', '0',   '7', 'tournament 1', '1', '1', '2023-2-2');



















