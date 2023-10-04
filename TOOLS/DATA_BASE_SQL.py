"DATABASE MANAGEMENT SYSTEM"   # софтуера, с който работим. Изпълнява инструкции и връща резултат


"""
ФИЛТРИ / ОПЕРАТОРИ

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
        WHERE JobTitle = < > "Sales Representative"
        
    
    ВРЪЩА УНИКАЛНИТЕ СТОЙНОСТИ
        distinct
    
    
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


GROUP BY
    SELECT column_name(s)
    FROM table_name
    WHERE condition
    GROUP BY column_name(s)
    ORDER BY column_name(s); 


HAVING Syntax
    SELECT column_name(s)
    FROM table_name
    WHERE condition
    GROUP BY column_name(s)
    HAVING condition;


ПРЕИМЕНУВАНЕ - ALIAS
    as "Full name"
    employee e  ==  employee as e 


ИЗПУСКА РЕДА, АКО Е NULL
    coalesce(middlename, " ")


УСЛОВИЕ
    SELECT IF(middle is NULL, concat(first, " ", last), concat(first, " ", middle, " ", last)


ДАТА и ЧАС ФОРМАТИРАНЕ
    SELECT year(e.HireDate), month(e.HireDate)



MIN() / MAX()
    SELECT MIN(Price)
    FROM Products;


SUM() Syntax
    SELECT SUM(column_name)
    FROM table_name


COUNT() 
    SELECT COUNT(ProductID)
    FROM Products;


AVG()
    SELECT AVG(Price)
    FROM Products;

===== ТЕОРИЯ =====

ВИДОВЕ БАЗИ ДАННИ 
    NoSQL - не работи с SQL езика, съвсем различна бира
    Relational - съхранпва инфото в таблици с връзки (релации) между тях
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


ЕЛЕМЕНТИНА КОЛОНАТА     MySQL Workbench

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






=== ПРИМЕРИ ===

-- Write an SQL query to find all employees whose salary is bigger than their manager's.
SELECT concat(e.firstname, " ", e.lastname) as "employee name", e.salary as "employee salary", concat(m.firstname, " ", m.lastname) as "manager name", m.Salary as "manager salary"
FROM employees as e, employees as m
WHERE m.EmployeeID = e.managerID  and e.salary > m.salary;  -- относно мениджъра на конкретния служител


"""


