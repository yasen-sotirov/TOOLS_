-- Write a SQL query to find all information about all departments (use "TelerikAcademy" database).
SELECT * FROM departments;


-- Write a SQL query to find all department names.
SELECT name FROM departments;


-- Write a SQL query to find the salary of each employee.
SELECT salary FROM employees;


-- Write a SQL to find the full name of each employee.
SELECT firstname, lastname FROM employees;
SELECT concat(firstname, " ", coalesce(middlename, " "), " ", lastname) as "Full name" FROM employees;
SELECT concat_ws(" ", firstname, coalesce(middlename, " "), lastname) as "Full name" FROM employees;
SELECT IF(middlename is NULL, concat(firstname, " ", lastname), concat(firstname, " ", middlename, " ", lastname) as "Full name" from employees; 


-- Write a SQL query to find the email addresses of each employee (by his first and last name). Consider that the mail domain is telerikacademy.com. Emails should look like “John.Doe@telerikacademy.com". The produced column should be named "Full Email Addresses".
SELECT concat(firstname, ".", lastname, "@telerikacademy.com") AS "Full Email Addresses" FROM employees;


-- Write a SQL query to find all different employee salaries.
SELECT distinct salary FROM employees;


-- Write a SQL query to find all information about the employees whose job title is “Sales Representative“.
SELECT * FROM employees WHERE JobTitle = "Sales Representative";


-- Write an SQL query to find all employees whose salary is bigger than their manager's.
SELECT concat(e.firstname, " ", e.lastname) as "employee name", e.salary as "employee salary", concat(m.firstname, " ", m.lastname) as "manager name", m.Salary as "manager salary"
FROM employees as e, employees as m
WHERE m.EmployeeID = e.managerID  and e.salary > m.salary;  -- относно мениджъра на конкретния служител


-- Write a SQL query to find the names of all employees whose first name starts with "SA".
SELECT firstname FROM employees WHERE FirstName like "SA%";
SELECT firstname FROM employees WHERE firstname regexp("^SA");
SELECT firstname FROM employees WHERE left(firstname, 2) = "sa";


-- Write a SQL query to find the names of all employees whose last name contains "ei".
SELECT lastname FROM employees WHERE LastName like "%ei%";


-- Write a SQL query to find the salary of all employees whose salary is in the range [20000…30000].
-- Write a SQL query to find the names of all employees whose salary is 25000, 14000, 12500 or 23600.
-- Write a SQL query to find all employees that do not have manager.
-- Write a SQL query to find the names of all employees who are hired before their managers.
-- Write a SQL query to find all employees that have salary more than 50000. Order them in decreasing order by salary.
-- Write a SQL query to find the top 5 best paid employees.
-- Write a SQL query to find all employees and their address.
-- Write a SQL query to find all employees whose MiddleName is the same as the first letter of their town.
-- Write a SQL query to find all employees that have manager, along with their manager.
-- Write a SQL query to find all employees that have manager, along with their manager and their address.
-- Write a SQL query to find all departments and all town names as a single list.
-- Write a SQL query to find all the employees and the manager for each of them along with the employees that do not have manager.
-- Write a SQL query to find the names of all employees from the departments "Sales" and "Finance" whose hire year is between 1995 and 2005.