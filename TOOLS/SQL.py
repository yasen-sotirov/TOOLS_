"DATABASE MANAGEMENT SYSTEM"   # софтуера, с който работим. Изпълнява инструкции и връща резултат


"""
    INSERT (за създаване)
    SELECT (за четене)
    UPDATE (за актуализиране)
    DELETE (за изтриване)
    
===== ФИЛТРИ / ОПЕРАТОРИ =====
==============================

    IN ОПЕРАТОР
        WHERE departments.Name in ("Sales", "Finance")
    
    
    LIKE
        % - не се интересува колко елемента има преди/след него
        WHERE FirstName like "SA%"  
        
    
    REGEXP
        WHERE FirstName regexp("^SA")  
        
        
    СЕЛЕКТИРА ЕЛЕМЕНТИ НА КОЛОНАТА
        WHERE left(firstname, 2) = "sa"
        WHERE right(lastname, 2) = "ov"
    
    
    ДИАПАЗОН / ТОЧНИ ЧИСЛА
        WHERE salary between 2000 and 3000          - инклузив
        WHERE Salary >= 20000 and salary <= 30000;
        WHERE Salary in (25000, 14000, 12500, 23600);
    
     
    ЛОГИЧЕСКИ ОПЕРАТОРИ
        -- Write a SQL query to find all information about the employees whose job title is “Sales Representative“.
        SELECT * FROM employees WHERE JobTitle = "Sales Representative";
        
    
    ВРЪЩА УНИКАЛНИТЕ СТОЙНОСТИ
        -- Write a SQL query to find all different employee salaries.
        SELECT distinct salary FROM employees;
    
    
    ВРЪЩА ПРИ NULL    
        WHERE isnull(ManagerID);
        
        
    ЛИМИТ НА ПОЛУЧЕНИТЕ РЕЗУЛТАТИ
        ORDER BY Salary desc LIMIT 5;    





ОБЕДИНЯВАНЕ НА ТАБЛИЦИ
    JOIN (INNER JOIN) - ако не е NULL
        SELECT firstname, lastname, o.customer_id   # префикс: при повтаряне на колоните се уточнява от коя таблица ги селектираме 
        FROM orders as o JOIN customers as c        # обединява таблиците order и customers
        ON o.customer_id = c.customer_id            # където id-то им съвпада

    FULL JOIN - връща всички данни от двете таблици, дои тези с NULL
    LEFT JOIN - връща всички от таблица 1 и тези от таблица 2 дето са без NULL
    RIGHT JOIN - връща таблица 1 без тези с NULL и цялата таблица 2



ОБЕДИНЯВА ТАБЛИЦИ В ЛИСТ
    UNION - връща само уникалните елементи
    UNION ALL - връща всички елементи
    
    SELECT name FROM departments
    UNION ALL
    SELECT name FROM towns;



NULL
    АКО НЕ Е НИЩО
        WHERE manager_id IS NOT NULL
    
    ЗАМЕНЯ ЕЛЕМЕНТ АКО Е NULL
        coalesce(middle_name, "")   - от много изброени елементи заменя първия NULL
        ifnull(middle_name, "")     - заменя само един елемент
        
    ИЗПУСКА РЕДА, АКО Е NULL
        coalesce(middlename, " ")
    
 

ЗАКРЪГЛЯНЕ  слага се елиас, иначе round(...) ще се появи в името на колоната
    SELECT round(salary, 2) as salary


СОРТИРА
    WHERE salary > 5000 ORDER BY salary         - възходящо или  asc;
    WHERE salary > 5000 ORDER BY salary desc    - низходящо
    
    
ОБЕДИНЯВА КОЛОНИ В ЕДНА
    concat(first, " ", middle, " ", last)
    concat_ws(" ", first, middle, last) - подобно на   ' '.join()


ПРЕИМЕНУВАНЕ - ALIAS
    as "Full name"
    employee e  ==  employee as e 


ИЗПУСКА РЕДА, АКО Е NULL
    coalesce(middlename, " ")


УСЛОВИЕ
    SELECT IF(middle is NULL, concat(first, " ", last), concat(first, " ", middle, " ", last)


ДАТА и ЧАС ФОРМАТИРАНЕ
    SELECT year(e.HireDate), month(e.HireDate)



===== ТЕОРИЯ =====

ВИДОВЕ БАЗИ ДАННИ 
    NoSQL - не работи с SQL езика, съвсем различна бира
    Relational - съхранява инфото в таблици с връзки (релации) между тях
    работят с езика SQL - Structured Query Language


ПРЕДИМСТВА
    – организирани, структурирани
    - в една таблица да държим всичко необходимо за едно приложение
    - данните не трябва да се повтарят (нормализиране)
    - интегритет - подсигурява на няколко нива че данните са правилни


ЕЛЕМЕНТИ НА БД
    - база данни -  дава голяма стая с много място, където се разполагат схемите
    - схема групира и организира таблиците
    - таблиците организират информацията ни. Таблицата може да я оприличим 
      на Клас, атрибутите са колоните, редовете са инстанциите


WORKBENCH
    - дава визуална представ как изграждаме схемите. 
      може и през конзолата, но е по трудно


ЕЛЕМЕНТИ НА КОЛОНАТА     MySQL Workbench

    PK - PRIMARY KEY, еднозначо идентифицира (ID) точно тази
    NN - NOT NUL (None)ЗАДЪЛЖИТЕЛНО ИЗИСКВА ДА БЪДЕ ПОПЪЛНЕНО
    UQ - UNIQUE
    ZF - ZERO FILlL - ПОПЪЛВА АВТОАМАТИЧНО 0 АКО Е ПРАЗНО
    AI - auto increment - АВТОМАТИЧНО ПОПЪЛВА КЛЮЧОВЕТ
    Foreign key - слага се на подчинената таблица. Една компания има много служители. Служителите има FK

    varchar(100) - стринг с определена дължина


ОПЕРАЦИИ
    reverse engineering     - от SQL в таблица   
    forward engineering     - от таблица в my SQL
    indexes - индексиране   - осигурява по-бърз достъп до
    Drop Table              - трие таблицата
    Trunkate Table          - трие информацията в таблицата




===== ВСИКИ ПРИМЕРИ =====
=========================

    ТЪРСИ ПО ПРАЗНА КЛЕТКА
-- Write a SQL query to find all employees that do not have manager.
SELECT firstname, lastname FROM employees WHERE isnull(ManagerID);

-- Write a SQL query to find the salary of each employee.
SELECT salary FROM employees;




    ОБЕДИНЯВА КОЛОНИ В ЕДНА
-- Write a SQL to find the full name of each employee.
SELECT firstname, lastname FROM employees;
SELECT concat(firstname, " ", coalesce(middlename, " "), " ", lastname) as "Full name" FROM employees;
SELECT concat_ws(" ", firstname, coalesce(middlename, " "), lastname) as "Full name" FROM employees;
SELECT IF(middlename is NULL, concat(firstname, " ", lastname), concat(firstname, " ", middlename, " ", lastname) as "Full name" from employees; 




    ГЕНЕРИРА ИМЕЙЛ 
-- Write a SQL query to find the email addresses of each employee (by his first and last name). Consider that the mail domain is telerikacademy.com. Emails should look like “John.Doe@telerikacademy.com". The produced column should be named "Full Email Addresses".
SELECT concat(firstname, ".", lastname, "@telerikacademy.com") AS "Full Email Addresses" FROM employees;




    ВРЪЩА УНИКАЛНИТЕ РЕЗУЛТАТИ
-- Write a SQL query to find all different employee salaries.
SELECT distinct salary FROM employees;




    ВРЪЩА РЕЗУЛТАТ ОТ SELF RELATION 
-- Write an SQL query to find all employees whose salary is bigger 
-- than their manager's.
SELECT concat(e.firstname, " ", e.lastname) as "employee name", e.salary as "employee salary", concat(m.firstname, " ", m.lastname) as "manager name", m.Salary as "manager salary"
FROM employees as e, employees as m
WHERE m.EmployeeID = e.managerID  and e.salary > m.salary;  -- относно мениджъра на конкретния служител

-- Write a SQL query to find the names of all employees who are hired before their managers.
SELECT concat(e.firstname, " ", e.lastname) as "employee name", e.HireDate as "hire date", concat(m.firstname, " ", m.lastname) as "manager name", m.HireDate as "hire date"
FROM employees as e, employees as m
WHERE e.HireDate < m.HireDate and e.ManagerID = m.EmployeeID; 




    ТЪРСИ ПО ЧАСТ ОТ ДУМА
-- Write a SQL query to find the names of all employees whose first name starts with "SA".
SELECT firstname FROM employees WHERE FirstName like "SA%";
SELECT firstname FROM employees WHERE firstname regexp("^SA");
SELECT firstname FROM employees WHERE left(firstname, 2) = "sa";

-- Write a SQL query to find the names of all employees whose last name conta "ei".
SELECT lastname FROM employees WHERE LastName like "%ei%";




    ТЪРСИ ПО ДИАПАЗОН ИЛИ ТОЧНИ ПАРАМЕТРИ
-- Write a SQL query to find the salary of all employees whose salary is in the range [20000…30000].
SELECT firstname, lastname, salary 
FROM employees 
WHERE Salary >= 20000 and salary <= 30000 ORDER BY salary desc;

SELECT firstname, lastname, round(salary, 2) as salary 
FROM employees 
WHERE Salary between 20000 and 30000;

-- Write a SQL query to find the names of all employees whose salary is 25000, 14000, 12500 or 23600.
SELECT firstname, lastname, salary FROM employees WHERE Salary in (25000, 14000, 12500, 23600);




    ВРЪЩА ЛИМИТИТАН БРОЙ РЕЗУЛТАТИ
-- Write a SQL query to find the top 5 best paid employees.
SELECT concat(firstname, " ", lastname) as "employee name", salary FROM employees ORDER BY Salary desc LIMIT 5;




    ОБЕДИНЯВА КОЛОНИ ОТ РАЗЛИЧНИ ТАБЛИЦИ
-- Write a SQL query to find all employees and their address.
SELECT e.firstname, e.lastname, a.addresstext, t.name as "town name"
FROM employees e, addresses a, towns t
WHERE e.AddressID = a.AddressID and a.TownID = t.TownID;

-- Write a SQL query to find all employees whose MiddleName 
-- is the same as the first letter of their town.
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

    ОБЕДИНЯВА ДВЕ КОЛОНИ ЕДНА НАД ДРУГА
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




    ДОБАВЯ НОВ ОБЕКТ
INSERT INTO employees  (FirstName, LastName, JobTitle, DepartmentID, ManagerID, HireDate, Salary, AddressID)
VALUES ("Todor", "Todorov", "Engineering Manager", 1, 6, "2020-02-02", 15000, 40);




    ПРОМЕНЯ СЪЩЕСТВУВАЩ ОБЕКТ
UPDATE employees 
SET Salary = 25000, ManagerID = 45
WHERE  employeeID = 294;
-- задължително по PRIMARY KEY







"""


