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
SELECT firstname, lastname, salary FROM employees WHERE Salary >= 20000 and salary <= 30000;
SELECT firstname, lastname, round(salary, 2) as salary FROM employees WHERE Salary between 20000 and 30000;



-- Write a SQL query to find the names of all employees whose salary is 25000, 14000, 12500 or 23600.
SELECT firstname, lastname, salary FROM employees WHERE Salary in (25000, 14000, 12500, 23600);



-- Write a SQL query to find all employees that do not have manager.
SELECT firstname, lastname FROM employees WHERE isnull(ManagerID);



-- Write a SQL query to find the names of all employees who are hired before their managers.
SELECT concat(e.firstname, " ", e.lastname) as "employee name", e.HireDate as "hire date", concat(m.firstname, " ", m.lastname) as "manager name", m.HireDate as "hire date"
FROM employees as e, employees as m
WHERE e.HireDate < m.HireDate and e.ManagerID = m.EmployeeID; 



-- Write a SQL query to find all employees that have salary more than 50000. Order them in decreasing order by salary.
SELECT concat_ws(" ", firstname, lastname, salary) FROM employees WHERE salary > 50000 ORDER BY salary desc;



-- Write a SQL query to find the top 5 best paid employees.
SELECT concat(firstname, " ", lastname) as "employee name", salary FROM employees ORDER BY Salary desc LIMIT 5;



-- Write a SQL query to find all employees and their address.
SELECT e.firstname, e.lastname, a.addresstext, t.name as "town name"
FROM employees e, addresses a, towns t
WHERE e.AddressID = a.AddressID and a.TownID = t.TownID;



-- Write a SQL query to find all employees whose MiddleName is the same as the first letter of their town.
SELECT e.firstname, e.MiddleName, t.name as "town name"
FROM employees as e  
JOIN addresses as a 					-- към таблицата employee добвяме addresses
	on e.AddressID = a.AddressID		-- ако id-та съвпадат
JOIN towns t 							-- добавяме таблица town
	on a.TownID = t.townID 				-- ако id-та съвпадат
WHERE e.MiddleName = left(t.name, 1);	-- при условие, че..



-- Write a SQL query to find all employees that have manager, along with their manager.
SELECT concat_ws(' ', e.firstname, e.lastname) as "employee name", e.ManagerID,
	   concat(m.firstname, " ", m.lastname) as "manager name",  m.ManagerID
FROM employees e, employees m
WHERE e.ManagerID = m.EmployeeID and m.ManagerID is not NULL;



-- Write a SQL query to find all employees that have manager, along with their manager and their address.
SELECT 
	concat(e.firstname, " ", e.lastname) as "employee name", ea.AddressText,
	concat(m.firstname, " ", m.lastname) as "manager name", ma.AddressText
FROM 
	employees e, 
    employees m,
    addresses ea,
    addresses ma
WHERE 
	e.ManagerID = m.EmployeeID AND e.AddressID = ea.AddressID AND m.AddressID = ma.AddressID;

-- ========= V2 ===============
SELECT 
concat(e.firstname, " ", e.lastname) as "employee", ea.addresstext as "e address",
concat(m.firstname, " ", m.lastname) as "manager",  ma.addresstext as "m address"

FROM employees e
JOIN employees m ON e.managerid = m.EmployeeID
JOIN addresses ea ON ea.AddressID = e.AddressID
JOIN addresses ma ON ma.AddressID = m.AddressID;



-- Write a SQL query to find all departments and all town names as a single list.
SELECT name FROM departments
UNION ALL
SELECT name FROM towns;



-- Write a SQL query to find all the employees and the manager for each of them along with the employees that do not have manager.
SELECT e.firstname, e.lastname, m.firstname, m.lastname
FROM employees e, employees m
WHERE e.ManagerID = m.EmployeeID
UNION
SELECT e.FirstName, e.LastName, NULL AS firstname, NULL as lastname
FROM employees e
WHERE e.ManagerID is NULL;




-- Write a SQL query to find the names of all employees from the departments "Sales" and "Finance" whose hire year is between 1995 and 2005.
SELECT CONCAT(firstname, " ", lastname) as name, d.Name, year(e.HireDate)
FROM employees e, departments d
WHERE 
	e.DepartmentID = d.DepartmentID AND 
    d.Name in ("Sales", "Finance") AND
	Year(e.hiredate) BETWEEN 1995 AND 2005;
    
    
-- === V2 ===
SELECT CONCAT(firstname, " ", lastname) as name, d.Name, year(e.HireDate), month(e.Hiredate), day(e.HireDate)
FROM employees e
JOIN departments d on e.DepartmentID = d.DepartmentID
WHERE 
	d.name in ("Sales", "Finance") and 
	year(e.hiredate) BETWEEN 1995 AND 2005;










