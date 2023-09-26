<img src="https://webassets.telerikacademy.com/images/default-source/logos/telerik-academy.svg" alt="logo" width="300px" style="margin-top: 20px;"/>

# SQL - Tasks

## Instructions

1. Start your favourite SQL Client and create new database "TelerikAcademy", using the [provided script](./database_telerikacademy.sql)
1. Connect to the database "TelerikAcademy" and examine the major tables.
1. Use the "TelerikAcademy" database for all tasks.
1. Happy querying :)


## Tasks

1. Write a SQL query to find the average salary of employees who have been hired before year 2000 incl. Round it down to the nearest integer.
1. Write a SQL query to find all town names that end with a vowel (a,o,u,e,i).
1. Write a SQL query to find all town names that start with a vowel (a,o,u,e,i).
1. Write a SQL query to find the name and the length of the name of the town with the longest name.
1. Write a SQL query to find the name and the length of the name of the town with the shortest name.
1. Write a SQL query to find all employees with even IDs.
1. Write a SQL query to find the names and salaries of the employees that take the minimal salary in the company.
1. Write a SQL query to find the names and salaries of the employees that have a salary that is up to 10% higher than the minimal salary for the company.
1. Write a SQL query to find the full name, salary and department of the employees that take the minimal salary in their department.
1. Write a SQL query to find the average salary in the department #1.
1. Write a SQL query to find the average salary  in the "Sales" department.
1. Write a SQL query to find the number of employees in the "Sales" department.
1. Write a SQL query to find the number of all employees that have manager.
1. Write a SQL query to find the number of all employees that have no manager.
1. Write a SQL query to find all departments and the average salary for each of them.
1. Write a SQL query to find all projects that took less than 1 year (365 days) to complete.
1. Write a SQL query to find the count of all employees in each department and for each town.
1. Write a SQL query to find all managers that have exactly 5 employees. Display their first name and last name.
1. Write a SQL query to find all employees along with their managers. For employees that do not have manager display the value "(no manager)".
1. Write a SQL query to find the names of all employees whose last name is exactly 5 characters long.
1. Write a SQL query to display the current date and time in the following format "`day.month.year hour:minutes:seconds:milliseconds`".
1. Write a SQL query to display the average employee salary by department and job title.
1. Write a SQL query to display the town where maximal number of employees work.
1. Write a SQL query to display the number of managers from each town.
1. Write a SQL query to find the manager who is in charge of the most employees and their average salary.
1. Write a SQL statement finds the names of the employees who have worked on the most projects.

## Activity walk through

Some tasks require you to search additional information.

1. Task 2: Write a SQL query to find all town names that end with a vowel (a,o,u,e,i).
  - [MySQL right() funtion](https://www.w3schools.com/sql/func_mysql_right.asp)

2. Task 16 : Write a SQL query to find all projects that took less than 1 year (365 days) to complete.

   - [Datediff](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_datediff)

3. Task 20: "Write a SQL query to find the names of all employees whose last name is exactly 5 characters long."

   - [MySQL lenght](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_length)

4. Task 21: "Write a SQL query to display the current date and time in the following format day.month.year hour:minutes:seconds:milliseconds."

   - [MySQL date functions](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html)
