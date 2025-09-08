-- 	   _____ ____    __       __________  ____  __   _____
-- 	  / ___// __ \  / /      /_  __/ __ \/ __ \/ /  / ___/
-- 	  \__ \/ / / / / /        / / / / / / / / / /   \__ \ 
-- 	 ___/ / /_/ / / /___     / / / /_/ / /_/ / /______/ / 
-- 	/____/\___\_\/_____/    /_/  \____/\____/_____/____/  

-- 	Ultimate DA Bootcamp: https://www.youtube.com/watch?v=wQQR60KtnFY                                                       
--  примерите са обвързани с схемата parks_and_recreation


-- ===== ТЕОРИЯ =====

-- ВИДОВЕ БАЗИ ДАННИ 
--     NoSQL - не работи с SQL езика, съвсем различна бира
--     Relational - съхранява инфото в таблици с връзки (релации) между тях
--     работят с езика SQL - Structured Query Language


-- ПРЕДИМСТВА
--     – организирани, структурирани
--     - в една таблица да държим всичко необходимо за едно приложение
--     - данните не трябва да се повтарят (нормализиране)
--     - интегритет - подсигурява на няколко нива че данните са правилни


-- ЕЛЕМЕНТИ НА БД
--     - база данни -  дава голяма стая с много място, където се разполагат схемите
--     - схема групира и организира таблиците
--     - таблиците организират информацията ни. Таблицата може да я оприличим 
--       на Клас, атрибутите са колоните, редовете са инстанциите


-- WORKBENCH
--     - дава визуална представ как изграждаме схемите. 
--       може и през конзолата, но е по трудно


-- ЕЛЕМЕНТИ НА КОЛОНАТА     MySQL Workbench

--     PK - PRIMARY KEY, еднозначо идентифицира (ID) точно тази
--     NN - NOT NUL (None)ЗАДЪЛЖИТЕЛНО ИЗИСКВА ДА БЪДЕ ПОПЪЛНЕНО
--     UQ - UNIQUE
--     ZF - ZERO FILlL - ПОПЪЛВА АВТОАМАТИЧНО 0 АКО Е ПРАЗНО
--     AI - auto increment - АВТОМАТИЧНО ПОПЪЛВА КЛЮЧОВЕТ
--     Foreign key - слага се на подчинената таблица. Една компания има много служители. Служителите има FK

--     varchar(100) - стринг с определена дължина


-- ОПЕРАЦИИ
--     reverse engineering     - от SQL в таблица   
--     forward engineering     - от таблица в my SQL
--     indexes - индексиране   - осигурява по-бърз достъп до
--     Drop Table              - трие таблицата
--     Trunkate Table          - трие информацията в таблицата



-- КОНВЕНЦИЯ ЗА ИМЕНУВАНЕ
--     Таблици:
--         в множествено число
--         snake_case
--     Колони:
--         съществителни
--         единствено число
--         snake_case
--         избягваме ключови думи като:  key, int, date
--     Primary key:
--         използваме id или table_name_id
--     Foreign key:
--         използваме referenced_tabl_name_id

 
--     INSERT (за създаване)
--     SELECT (за четене)
--     UPDATE (за актуализиране)
--     DELETE (за изтриване)
    
    

-- --------------------------------------------
##	DISTINCT	-  връща уникалните (неповтарящи) се записи 

-- SELECT distinct gender
-- FROM parks_and_recreation.employee_demographics;



-- --------------------------------------------
##	OPERATORS	AND OR ><=

-- SELECT salary
-- FROM parks_and_recreation.employee_salary
-- WHERE salary > 60000;

-- SELECT *
-- FROM parks_and_recreation.employee_demographics
-- WHERE birth_date > '1985-01-01' 
-- AND gender = 'male';

-- SELECT *
-- FROM parks_and_recreation.employee_demographics
-- WHERE (first_name = 'Leslie' AND age = 44) OR age > 55;




-- --------------------------------------------
##	LIKE

#	% - заменя произволен брой елементи преди/след търсената част отдума:    1986% 
-- SELECT *
-- FROM parks_and_recreation.employee_demographics
-- WHERE first_name LIKE "A%";     

# 	_ - заменя един елемент преди/след търсената част отдума: A_  __a% 
-- SELECT *
-- FROM parks_and_recreation.employee_demographics
-- WHERE first_name LIKE "A__";   



-- --------------------------------------------
##	GROUP BY	+ AVG  MIN  MAX
-- групира редовете според еднa или повече колони 
-- използва се с агрегатни функции като SUM(), COUNT(), AVG(), MIN(), MAX(), 
-- за да се изчислят стойности за всяка група. Така се обобщават и изчисляват данни по групи.

-- SELECT gender, first_name
-- FROM parks_and_recreation.employee_demographics
-- GROUP BY gender;







-- --------------------------------------------
##	COUNT()	

#1
-- SELECT COUNT(distinct salary)		-- брой уникалните, неповтарящи се записи
-- FROM parks_and_recreation.employee_salary;

#2
-- SELECT count(age), gender
-- FROM parks_and_recreation.employee_demographics
-- GROUP BY gender;



-- --------------------------------------------
## 	ROUND

-- SELECT round(avg(age), -0) AS 'средни години', gender
-- FROM parks_and_recreation.employee_demographics
-- GROUP BY gender;






-- --------------------------------------------
##	ORDER BY	ASC/DESC

-- SELECT *
-- FROM parks_and_recreation.employee_demographics
-- ORDER BY gender, age DESC;

-- SELECT *
-- FROM parks_and_recreation.employee_salary
-- WHERE salary > 60000
-- ORDER BY salary DESC;



-- --------------------------------------------
##	HAVING		-- Показва резултатите имащи дадено условие. Работи с агрегатни функции след group by. 

# 1		-- office manager avg 5500
-- SELECT occupation, AVG(salary)
-- FROM parks_and_recreation.employee_salary
-- GROUP BY occupation;		

-- #2
-- SELECT occupation, AVG(salary)
-- FROM parks_and_recreation.employee_salary
-- WHERE occupation LIKE '%manager%'
-- GROUP BY occupation;

-- #3
-- SELECT occupation, AVG(salary)
-- FROM parks_and_recreation.employee_salary
-- WHERE occupation LIKE '%manager%'
-- GROUP BY occupation
-- HAVING AVG(salary) > 75000;



-- --------------------------------------------
## LIMIT		- ограничава показаните резултати до определен брой

-- #1
-- SELECT first_name, age
-- FROM parks_and_recreation.employee_demographics
-- ORDER BY age DESC		-- връща тримата старци 
-- LIMIT 3;

-- #2		- селектира (показва) резултата след лимита
-- SELECT first_name, age
-- FROM parks_and_recreation.employee_demographics
-- ORDER BY age DESC		-- връща тримата старци 
-- LIMIT 2, 1;



-- --------------------------------------------
# ALIASING

-- SELECT gender, AVG(age) AS avg_age
-- FROM parks_and_recreation.employee_demographics
-- GROUP BY gender
-- HAVING avg_age > 40;




-- --------------------------------------------
## SELF RELATION		-- обединява колони от различни таблици

#1	-- обединява колони от трите таблици
-- SELECT demo.first_name, demo.age, sala.salary, dept.department_name
-- FROM employee_demographics AS demo, employee_salary AS sala, parks_departments AS dept
-- WHERE demo.employee_id = sala.employee_id AND sala.dept_id = department_id;

#2
-- Write an SQL query to find all employees whose salary is bigger 
-- than their manager's.
-- SELECT 
-- 	concat(e.firstname, " ", e.lastname) as "employee name", 
-- 	e.salary as "employee salary", 
-- 	concat(m.firstname, " ", m.lastname) as "manager name", 
-- 	m.Salary as "manager salary"
-- FROM employees as e, employees as m
-- WHERE m.EmployeeID = e.managerID  and e.salary > m.salary;  -- относно мениджъра на конкретния служител

	




-- --------------------------------------------
##	ISNULL		-- търси празна клетка в колоната dept_id

SELECT first_name, last_name 
FROM parks_and_recreation.employee_salary 
WHERE isnull(dept_id);



-- --------------------------------------------
## JOINS		- обединява две таблици ако имат колони със сходни данни


#1	JOIN (INNER)	- обединява редовете, ако ги има и в двете таблици
#					- ако колоната я има и в двете таблици се упоменава от къде вземам инфото

-- SELECT dem.employee_id, dem.first_name, age, occupation AS длъжност, salary AS заплата
-- FROM parks_and_recreation.employee_demographics AS dem	-- left table 
-- INNER JOIN parks_and_recreation.employee_salary AS sal	-- right table
-- 	ON dem.employee_id = sal.employee_id;					-- обединяваме на беза ID


#2	LEFT (OUTER) JOIN		- взима всички попълнени редове от лявата (първата) таблица и добавя втората

-- SELECT dem.employee_id, dem.first_name, age, occupation AS длъжност, salary AS заплата
-- FROM parks_and_recreation.employee_demographics AS dem
-- LEFT JOIN parks_and_recreation.employee_salary AS sal
-- 	ON dem.employee_id = sal.employee_id;


#3	RIGHT (OUTER) JOIN		- взима всички попълнени редове от дяснат (втората) таблица и добавя първата таблица

-- SELECT dem.employee_id, dem.first_name, age, occupation AS длъжност, salary AS заплата
-- FROM parks_and_recreation.employee_demographics AS dem
-- RIGHT JOIN parks_and_recreation.employee_salary AS sal
-- 	ON dem.employee_id = sal.employee_id;


#4	SELF JOIN		- реферира към записи от същата таблица

-- SELECT emp1.first_name AS santa, emp2.first_name AS reciver
-- FROM parks_and_recreation.employee_salary emp1
-- JOIN parks_and_recreation.employee_salary emp2
-- 	ON emp1.employee_id + 1 = emp2.employee_id;



#5	MULTIPLE TABLES

-- SELECT demo.first_name, demo.age, sala.occupation, sala.salary, pdep.department_id, pdep.department_name
-- FROM parks_and_recreation.employee_demographics AS demo
-- INNER JOIN parks_and_recreation.employee_salary AS sala
-- 	ON demo.employee_id = sala.employee_id
-- INNER JOIN parks_and_recreation.parks_departments AS pdep
-- 	ON sala.dept_id = pdep.department_id;



-- --------------------------------------------
## UNION	- обединява един SELECT statemant с друг SELECT statemant
			-- 1:32:05

#1		- връща записите от двете таблици в една колона, отгоре кол 1 после кол 2
-- SELECT age, gender
-- FROM parks_and_recreation.employee_demographics
-- UNION 
-- SELECT first_name, last_name
-- FROM parks_and_recreation.employee_salary;



#2		- по подразбиране това е UNION DISTINCT, маха дупликатите
-- SELECT first_name, last_name
-- FROM parks_and_recreation.employee_demographics
-- UNION 
-- SELECT first_name, last_name
-- FROM parks_and_recreation.employee_salary;


#3		- обединява всичко и показва и дупликатите
-- SELECT first_name, last_name
-- FROM parks_and_recreation.employee_demographics
-- UNION ALL
-- SELECT first_name, last_name
-- FROM parks_and_recreation.employee_salary;


#4		- пример за орязване на старите и скъпите
-- SELECT first_name, last_name, 'стар мъж' AS Label
-- FROM parks_and_recreation.employee_demographics
-- WHERE age > 40 AND gender = 'male'
-- UNION
-- SELECT first_name, last_name, 'старa жена' AS Label
-- FROM parks_and_recreation.employee_demographics
-- WHERE age > 40 AND gender = 'female'
-- UNION
-- SELECT first_name, last_name, 'скъп' AS Label
-- FROM parks_and_recreation.employee_salary
-- WHERE salary > 70000
-- ORDER BY first_name, last_name;



-- --------------------------------------------
##	STRING FUNCTIONS	1:34:54		- build in functions


#	CONCAT
-- SELECT first_name, last_name, CONCAT(first_name, ' ', last_name) AS 'име и фамилия'
-- FROM parks_and_recreation.employee_demographics;


# 	BETWEEN
-- SELECT first_name, salary BETWEEN 60000 AND 70000
-- FROM parks_and_recreation.employee_salary;



# 	IN 	- точно попадениеalter
-- SELECT first_name, salary, salary IN (55000, 70000)
-- FROM parks_and_recreation.employee_salary;



# 	LENGTH
-- SELECT  first_name, length(first_name)
-- FROM parks_and_recreation.employee_demographics;


# 	UPPER
-- SELECT  first_name, upper(first_name) AS 'главни'
-- FROM parks_and_recreation.employee_demographics;


#	TRIM	- премахва преди и след думата
-- SELECT trim('  sky  ') AS 'чиста дума';


#	LEFT TRIM	- премахва преди думата
-- SELECT ltrim('  sky         ') AS 'чиста дума';


#	RIGHT TRIM	- премахва след думата
-- SELECT rtrim('             sky  ') AS 'чиста дума';


# 	LEFT/RIGHT		- премахва брой символи отляво и отдясно 
-- SELECT first_name, LEFT(last_name, 1) AS 'family name'
-- FROM parks_and_recreation.employee_demographics;


# 	SUBSTRING		- като str sliceing 
-- SELECT last_name, SUBSTRING(birth_date, 6,2) AS 'рожден месец'
-- FROM parks_and_recreation.employee_demographics;	


# 	REPLACE
-- SELECT first_name, REPLACE(first_name, 'a', 'A')
-- FROM parks_and_recreation.employee_demographics;


#	LOCATE		- може да се ползва за проверка дали даден ред има търсената частица
-- SELECT first_name, LOCATE('An', first_name)
-- FROM parks_and_recreation.employee_demographics;




-- --------------------------------------------
##	CASE WHEN STATEMANT	1:48:00		- създава нова колона, където показва резултата от условието

-- SELECT first_name, age, 
-- CASE
-- 	WHEN age <= 30 THEN 'млад'
--     WHEN age BETWEEN 30 AND 50 THEN 'средна възраст'
--     WHEN age >= 50 THEN 'стар'
-- END AS 'възрастова група'
-- FROM parks_and_recreation.employee_demographics



#	PAY INCRESE and BONUS
-- < 50000 = 5%
-- >= 50000 = 7% 
-- Finance = 10% bonus

-- SELECT first_name, salary,
-- CASE
-- 	WHEN salary < 50000 THEN salary * 1.05
--     WHEN salary >= 50000 THEN salary * 1.07 
-- END AS 'new salary',
-- CASE 
-- 	WHEN dept_id = 6 THEN salary * 0.10
-- END AS bonusdepartment_iddepartment_name
-- FROM parks_and_recreation.employee_salary;





-- --------------------------------------------
##	SUBQUERY

#1
-- SELECT *
-- FROM parks_and_recreation.employee_demographics
-- WHERE employee_id IN (
-- 	SELECT employee_id
--     FROM parks_and_recreation.employee_salary
--     WHERE dept_id = 1);


#2
-- SELECT first_name, salary, (
-- 	SELECT AVG(salary)
--     FROM parks_and_recreation.employee_salary) avg_salary
-- FROM parks_and_recreation.employee_salary;


#3	- просто пример за вложен select, не е коректен 

-- SELECT AVG(max_age)
-- FROM (
-- 	SELECT gender, 
-- 		AVG(age) AS avg_age, 
--         MAX(age) AS max_age, 
--         MIN(age) AS min_age, 
--         COUNT(age) AS count_age
-- 	FROM parks_and_recreation.employee_demographics
-- 	GROUP BY gender) AS agg_table;





-- --------------------------------------------
## 	WINDOW FUNCTIONS	2:07:00



#	OVER	-- подбно на group by, но може да се включи допълнителна информация, 
			-- без тя да се повлияе от групирането

-- SELECT dem.first_name, dem.last_name, gender, 
-- 	AVG(salary)
--     OVER (PARTITION BY gender)
-- FROM parks_and_recreation.employee_demographics AS dem
-- JOIN parks_and_recreation.employee_salary AS sal
-- 	ON dem.employee_id = sal.employee_id



#	ROLLING TOTAL	-- добавя своята сума към всеки следващ запис

-- SELECT dem.first_name, dem.last_name, gender, salary,
-- 	SUM(salary)
--     OVER (PARTITION BY gender ORDER BY dem.employee_id) AS Rolling_Toatal
-- FROM parks_and_recreation.employee_demographics AS dem
-- JOIN parks_and_recreation.employee_salary AS sal
-- 	ON dem.employee_id = sal.employee_id




-- --------------------------------------------
## ROW NUMBER	2:10:00

# 1		-- дава ново число, което не се повтаря
-- SELECT dem.first_name, dem.last_name, gender, salary,
-- 	ROW_NUMBER()
-- 	OVER ()
-- FROM parks_and_recreation.employee_demographics AS dem
-- JOIN parks_and_recreation.employee_salary AS sal
-- 	ON dem.employee_id = sal.employee_id;


# 2		-- разбива новото число по полове, което не се повтаря в пола
-- SELECT dem.first_name, dem.last_name, gender, salary,
-- 	ROW_NUMBER() 
--     OVER(PARTITION BY gender)		-- подрежда ги по реда им в таблицата
-- FROM parks_and_recreation.employee_demographics AS dem
-- JOIN parks_and_recreation.employee_salary AS sal
-- 	ON dem.employee_id = sal.employee_id;


# 3		-- разбива новото число по полове, което не се повтаря в пола
-- SELECT dem.first_name, dem.last_name, gender, salary,
-- 	ROW_NUMBER() 
--     OVER(PARTITION BY gender ORDER BY salary DESC) AS row_num		-- подрежда ги по намаляваща заплата
-- FROM parks_and_recreation.employee_demographics AS dem
-- JOIN parks_and_recreation.employee_salary AS sal
-- 	ON dem.employee_id = sal.employee_id;
    
  
  
-- --------------------------------------------
##	RANK		-- добавя ранг, като дава следващото числ според позицията на записа: 5 после 7 
 
-- SELECT dem.first_name, dem.last_name, gender, salary,
-- 	ROW_NUMBER() OVER(PARTITION BY gender ORDER BY salary DESC) AS row_num,
--     RANK() OVER(PARTITION BY gender ORDER BY salary DESC) AS rank_num		
-- FROM parks_and_recreation.employee_demographics AS dem
-- JOIN parks_and_recreation.employee_salary AS sal
-- 	ON dem.employee_id = sal.employee_id;


##	DENSE_RANK		-- добавя ранг, като дава следващото числ по ред на числата
 
-- SELECT dem.first_name, dem.last_name, gender, salary,
-- 	ROW_NUMBER() OVER(PARTITION BY gender ORDER BY salary DESC) AS row_num,
--     RANK() OVER(PARTITION BY gender ORDER BY salary DESC) AS rank_num,
--     DENSE_RANK() OVER(PARTITION BY gender ORDER BY salary DESC) AS rank_num	
-- FROM parks_and_recreation.employee_demographics AS dem
-- JOIN parks_and_recreation.employee_salary AS sal
-- 	ON dem.employee_id = sal.employee_id;



-- --------------------------------------------
## 	ВМЪКВАНЕ В ТАБЛИЦАТА

-- INSERT INTO parks_and_recreation.employee_demographics (employee_id, first_name, last_name)
-- VALUES (employee_id, first_name, last_name);



-- --------------------------------------------
#	ПРОМЕНЯ СЪЩЕСТВУВАЩ ЗАПИС

-- UPDATE parks_and_recreation.employee_salary 
-- SET salary = 50000
-- WHERE  salary = 55000;




-- --------------------------------------------
## 	ИЗТРИВАНЕ

-- DELETE
-- FROM employee_salary
-- WHERE employee_id = 13;


-- --------------------------------------------
## ADVANCED SQL TUTORIAL	2:20:10



-- --------------------------------------------
## CTE - Common Tabale Expression	
		-- временен резултат от заявка, който се дефинира в рамките на една SQL сесия 
		-- инструкция и може да бъде използван многократно в главната заявка, като ламбда функция
		-- използва се прости манипулации
        -- по-четими са от subquery


#1                                    
-- WITH CTE_Example AS
-- 	(
--     SELECT gender, AVG(salary) avg_sal, MAX(salary) max_sal, MIN(salary) min_sal, COUNT(salary) 
--     FROM parks_and_recreation.employee_demographics AS dem
--     JOIN parks_and_recreation.employee_salary AS sal
-- 		ON dem.employee_id = sal.employee_id
-- 	GROUP BY gender
--     )
-- SELECT AVG(avg_sal)		-- средната заплата между мъже и жени
-- FROM CTE_Example;
    

#2                                    
-- WITH CTE_Example (Gender, Avg_sal, Max_sal, Min_sal)AS
-- 	(
--     SELECT gender, round(AVG(salary), 0), MAX(salary), MIN(salary) 
--     FROM parks_and_recreation.employee_demographics AS dem
--     JOIN parks_and_recreation.employee_salary AS sal
-- 		ON dem.employee_id = sal.employee_id
-- 	GROUP BY gender
--     )
-- SELECT *	
-- FROM CTE_Example;





-- --------------------------------------------
## TEMPORARY TABLES	2:30:44		-- създава временна таблица, за сложни 

-- CREATE TEMPORARY TABLE salary_over_60k
-- SELECT *
-- FROM parks_and_recreation.employee_salary
-- WHERE salary >= 60000;

-- SELECT *
-- FROM salary_over_60k 




-- --------------------------------------------
-- STORED PROCEDURES 	2:38:20 
		-- съхранява кода и може да се преизползва многократно
        -- или се създава с десен бутон от SCHEMAS > stored procedures 

-- #1      
-- DELIMITER $$
-- CREATE PROCEDURE large_salaty2()
-- BEGIN
-- 	SELECT *
-- 	FROM parks_and_recreation.employee_salary
-- 	WHERE salary > 60000;
--     
-- 	SELECT *
-- 	FROM parks_and_recreation.employee_salary
-- 	WHERE salary > 10000;
-- END $$
-- DELIMITER ;
      
-- CALL large_salaty2()
      
      
-- # 2      
-- DELIMITER $$
-- CREATE PROCEDURE get_salary_by_id(employee_id_param INT)		-- задава параметър
-- BEGIN
-- 	SELECT salary
-- 	FROM parks_and_recreation.employee_salary
-- 	WHERE employee_id = employee_id_param;    
-- END $$
-- DELIMITER ;   
--       
-- CALL get_salary_by_id(1);		-- извиква функцията с аргумент 1





-- --------------------------------------------
## TRIGGERS	2:51:00		-- прави нещо при събитие

-- DELIMITER $$
-- CREATE TRIGGER employee_insert_into_salary
-- 	AFTER INSERT ON employee_salary
--     FOR EACH ROW
-- BEGIN
-- 	INSERT INTO employee_demographics (employee_id, first_name, last_name)
--     VALUES (NEW.employee_id, NEW.first_name, NEW.last_name);
-- END $$
-- DELIMITER ;


-- INSERT INTO employee_salary (employee_id, first_name, last_name, occupation, salary, dept_id)
-- VALUE (13, 'Jean', 'Separstein', 'Entertainment', 80000, NULL);

-- DELETE
-- FROM employee_salary
-- WHERE employee_id = 13;




-- --------------------------------------------
## EVENTS	3:01:01	-- случва се по график и прави нещо

-- DELIMITER $$
-- CREATE EVENT delete_id_13
-- ON SCHEDULE EVERY 30 SECOND
-- DO
-- BEGIN
-- 	DELETE
--     FROM employee_salary
--     WHERE employee_id = 13;
-- END $$
-- DELIMITER ;


# ПРОВЕРКА ПРОМЕНЛИВИ
-- SHOW VARIABLES LIKE 'event%'








































