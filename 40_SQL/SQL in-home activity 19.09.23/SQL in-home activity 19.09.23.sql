# 1. Write a SQL query to find all information about all departments (use "TelerikAcademy" database).
SELECT * FROM departments;

-- 1. Write a SQL query to find all department names.
SELECT name FROM departments;

-- 1. Write a SQL query to find the salary of each employee.
SELECT salary FROM employees;

-- 1. Write a SQL to find the full name of each employee.
SELECT firstname, middlename, lastname FROM employees;

SELECT concat(firstname, " ", middlename, " ", lastname) FROM employees;

SELECT concat(firstname, " ", coalesce(middlename, "noMiddleName"), " ", lastname) as "Full Name" FROM employees;

SELECT 
    IF(middlename IS NULL,
        CONCAT(firstname, ' ', lastname),
        CONCAT(firstname,
                ' ',
                middlename,
                ' ',
                lastname)) AS 'Full Name'
FROM
    employees;

SELECT concat_ws(" ", firstname, middlename, lastname) as FullName FROM employees;

SELECT concat(firstname, " ", ifNull(middlename, ""), " ", lastname) as "Full Name" FROM employees;


-- 1. Write a SQL query to find the email addresses of each employee (by his first and last name). Consider that the mail domain is telerikacademy.com. Emails should look like “John.Doe@telerikacademy.com". The produced column should be named "Full Email Addresses".
SELECT concat(firstname, ".", lastname, "@telerikacademy.com") as "Full Email Addresses" FROM employees;


-- 1. Write a SQL query to find all different employee salaries.
SELECT DISTINCT
    salary
FROM
    emploYEes;


-- 1. Write a SQL query to find all information about the employees whose job title is “Sales Representative“.
SELECT 
    *
FROM
    employees
WHERE
    JobTitle = 'Sales Representative';


-- 1. Write an SQL query to find all employees whose salary is bigger than their manager's.
SELECT e.firstname, e.lastname, e.salary as EmployeeSalary, e.ManagerID, m.EmployeeID, m.firstname, m.lastname, m.salary as ManagerSalary
FROM employees as e, employees m
WHERE e.managerID = m.employeeID and e.salary > m.salary;


-- 1. Write a SQL query to find the names of all employees whose first name starts with "SA".
SELECT firstname, lastname FROM employees WHERE firstname like "SA%";

SELECT e.firstname, e.lastname FROM employees as e WHERE e.firstname regexp("^SA");

SELECT firstname, lastname FROM employees WHERE left(firstname, 2) like "sa";


-- 1. Write a SQL query to find the names of all employees whose last name contains "ei".
SELECT firstname, lastname FROM employees WHERE lastname like "%ei%";

SELECT e.firstname, e.lastname FROM employees as e WHERE e.lastname regexp("ei");


-- 1. Write a SQL query to find the salary of all employees whose salary is in the range [20000…30000].
SELECT firstname, lastname, round(salary, 2) as salary FROM employees WHERE salary between 20000 and 30000;

SELECT firstname, lastname, round(salary, 2) as salary FROM employees WHERE salary >= 20000 and  salary <= 30000;


-- 1. Write a SQL query to find the names of all employees whose salary is 25000, 14000, 12500 or 23600.
SELECT firstname, lastname, round(salary, 2) as salary FROM employees WHERE salary in (25000, 14000, 12500, 23600);


-- 1. Write a SQL query to find all employees that do not have manager.
SELECT firstname, lastname, jobtitle FROM employees WHERE ManagerID is Null;


-- 1. Write a SQL query to find the names of all employees who are hired before their managers.
SELECT e.firstname, e.lastname, e.HireDate, e.ManagerID, m.EmployeeID, m.firstname, m.lastname, m.HireDate
FROM employees as e, employees m
WHERE e.managerID = m.employeeID and e.HireDate < m.HireDate;


-- 1. Write a SQL query to find all employees that have salary more than 50000. Order them in decreasing order by salary.
SELECT * FROM employees WHERE salary >= 50000 ORDER BY salary desc;
SELECT * FROM employees WHERE salary >= 50000 ORDER BY salary asc; -- възходящ ред

-- 1. Write a SQL query to find the top 5 best paid employees.
SELECT * FROM employees ORDER BY salary desc LIMIT 5;

-- 1. Write a SQL query to find all employees and their address.
SELECT e.firstname, e.lastname, a.addresstext
FROM employees e
JOIN addresses a on e.AddressID = a.AddressID;

SELECT e.firstname, e.lastname, a.addresstext, t.name
FROM employees e
JOIN addresses a on e.AddressID = a.AddressID
JOIN towns as t on a.TownID = t.TownID;

SELECT e.firstname, e.lastname, a.addresstext, t.name
FROM employees e,  addresses a, towns t
WHERE e.AddressID = a.AddressID and a.TownID = t.TownID;

-- Write a SQL query to -- find all employees whose MiddleName is the same as the first letter of their town.

SELECT * FROM employees e
INNER JOIN addresses a on e.addressID = a.AddressID
INNER JOIN towns t on a.TownID = t.townID  
WHERE e.middlename = left(t.name, 1);


-- 1. Write a SQL query to find all employees that have manager, along with their manager.
SELECT e.firstname, e.lastname, m.firstname, m.lastname FROM employees e, employees m
WHERE e.ManagerID is not Null and e.ManagerID = m.EmployeeID;

-- 1. Write a SQL query to find all employees that have manager, along with their manager and their address.
SELECT 
    CONCAT(e.firstname, ' ', e.lastname) AS EmployeeName,
    ea.addresstext AS EmployeeAddress,
    CONCAT(m.firstname, ' ', m.lastname) AS ManagerName,
    ma.addresstext AS ManagerAddress
FROM
    employees e,
    employees m,
    addresses ea,
    addresses ma
WHERE
    e.ManagerID = m.EmployeeID AND e.AddressID = ea.AddressID AND m.AddressID = ma.AddressID;
    
    
SELECT 
    CONCAT(e.firstname, ' ', e.lastname) AS EmployeeName,
    ae.addresstext AS EmployeeAddress,
    CONCAT(m.firstname, ' ', m.lastname) AS ManagerName,
    am.addresstext AS ManagerAddress
FROM
    employees e
        JOIN
    employees m ON e.ManagerID = m.EmployeeID
        JOIN
    addresses ae ON ae.AddressID = e.AddressID
        JOIN
    addresses am ON am.AddressID = m.AddressID;
    

-- 1. Write a SQL query to find all departments and all town names as a single list.
SELECT name FROM departments
union all
SELECT name FROM towns; 


-- 1. Write a SQL query to find all the employees and the manager for each of them along with the employees that do not have manager.
SELECT e.firstname, e.lastname, m.firstname, m.lastname FROM employees e, employees m
WHERE e.ManagerID = m.EmployeeID
UNION
SELECT e.firstname, e.lastname, null as firstname, null as lastname FROM employees e
WHERE e.ManagerID is Null;

SELECT e.firstname, e.lastname, m.firstname, m.lastname FROM employees e
JOIN employees m on e.ManagerID = m.EmployeeID;

SELECT e.firstname, e.lastname, m.firstname, m.lastname FROM employees e
RIGHT JOIN employees m on e.EmployeeID = m.ManagerID;               -- разглеждаме с повишено внимание 

SELECT e.firstname, e.lastname, m.firstname, m.lastname FROM employees e
LEFT JOIN employees m on e.ManagerID = m.EmployeeID;

-- 1. Write a SQL query to find the names of all employees from the departments "Sales" and "Finance" whose hire year is between 1995 and 2005.
SELECT concat(e.firstname, " ", e.lastname) as FullName FROM employees as e
JOIN departments d on e.DepartmentID = d.DepartmentID
WHERE d.Name in ("Sales" , "Finance") and year(e.hiredate) between 1995 and 2005;

SELECT concat(e.firstname, " ", e.lastname) as FullName FROM employees as e, departments as d
WHERE e.DepartmentID = d.departmentid and d.name in ("Sales" , "Finance") and year(e.hiredate) between 1995 and 2005; 


SELECT 
    e.EmployeeID AS EmployeeID,
    e.firstname AS EmployeeFirstName,
    e.lastname AS EmployeeLastName,
    m.EmployeeID AS ManagerID,
    m.firstname AS ManagerFirstName,
    m.lastname AS ManagerFirstName
FROM
    employees e
        RIGHT JOIN
    employees m ON e.ManagerID = m.EmployeeID;


SELECT distinct managerid from employees;
