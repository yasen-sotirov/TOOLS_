-- CATEGORIES
INSERT INTO new_forum_project.category (name_of_category)
VALUE ('Fitness'), ('Football'), ('volleyball');


-- USERS
INSERT INTO new_forum_project.new_user (email, nickname, password, date_of_birth, gender)
VALUES ('user5@gmail.com', 'user5', '123321', '2005-05-05', 'male'),
       ('user6@gmail.com', 'user6', '123321', '2006-06-06', 'female'),
       ('user7@gmail.com', 'user7', '123321', '2007-07-07', 'male'),
       ('user8@gmail.com', 'user8', '123321', '2008-08-08', 'female'),
       ('user9@gmail.com', 'user9', '123321', '2009-09-09', 'male');


-- TOPICS
INSERT INTO new_forum_project.new_topic (title, topic_text, date_of_creation, category_name_of_category, id_of_author)
VALUES ('Latest news on BG football', 'Do you read about the new football record?', '2023-10-28', 'Football', 9),
       ('Latest fitness world news!', 'The equipment price is rising!', '2023-10-28', 'Fitness', 8),
       ('Best volleyball teams', 'First, lets talk about BG', '2023-10-28', 'Fitness', 6);


-- REPLIES
INSERT INTO new_forum_project.replies (text, new_topic_id_of_topic, new_user_id_of_user)
VALUES ("I thing it's a facke news", 1, 5),
	   ("It's real! I'm sure!", 1, 6),
       ("I will sell everything and be rich :)", 2, 5),
       ("How are you going to train without equipment?", 2, 6),
       ("My favorite team is the Men's National Team of Bulgaria", 3, 9),
       ("Yes, they are really great! This is my favorite too", 3, 8);


