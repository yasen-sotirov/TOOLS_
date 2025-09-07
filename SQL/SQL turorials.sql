SELECT *
FROM parks_and_recreation.employee_salary
WHERE first_name = 'Leslie';


SELECT first_name, 
last_name, 
birth_date,
age,
age + 10
FROM parks_and_recreation.employee_demographics;


SELECT distinct gender
FROM  parks_and_recreation.employee_demographics;



SELECT *
FROM parks_and_recreation.employee_demographics
WHERE birth_date > '1985-01-01';

SELECT *
FROM parks_and_recreation.employee_demographics
WHERE birth_date > '1985-01-01'
AND gender = 'male '
;


SELECT *
FROM parks_and_recreation.employee_demographics
WHERE (first_name = 'Leslie' AND age = 44) OR age > 55
;