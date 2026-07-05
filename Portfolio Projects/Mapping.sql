--emp_record_table creation
create table emp_record_table(
(x1...> emp_id text primary key,
(x1...> first_name text,
(x1...> last_name text,
(x1...> gender text,
(x1...> role text,
(x1...> dept text,
(x1...> exp int,
(x1...> country text,
(x1...> continent text,
(x1...> salary int,
(x1...> emp_rating int,
(x1...> manager text,
(x1...> proj_id text); 

--imported emp_record_table.csv into emp_record_table
.import --skip | emp_record_table.csv emp_record_table 

--creation of data_science_table
create table data_science_team(
(x1...> emp_id text primary key,
(x1...> first_name text,
(x1...> last_name text,
(x1...> gender text,
(x1...> role text,
(x1...> dept text,
(x1...> exp int,
(x1...> country text,
(x1...> continent text);

--Imported data_science_team.csv into data_science_team
.import --skip 1 data_science_team.csv data_science_team;

--Creation of proj_table
create table proj_table(
(x1...> project_id text primary key,
(x1...> proj_name text,
(x1...> domain text,
(x1...> start_date date,
(x1...> closure_date date,
(x1...> dev_qtr text,
(x1...> status text);

--Imported proj_table.csv into proj_table
.import --skip 1 proj_table.csv proj_table;

--Extracted employees with their rating and categorized them into 3 groups based on their rating
select emp_id, first_name, last_name, gender, dept as department, emp_rating,      
   ...> case
   ...> when emp_rating < 2 then 'less than 2'
   ...> when emp_rating between 2 and 4 then 'between 2 and 4'
   ...> when emp_rating > 4 then 'greater than 4'
   ...> end as Rating         
   ...> from emp_record_table;

--Created another column Name by concatenating first_name and last_name
select first_name || ' ' || last_name  as Name, dept as department from emp_record_table;

--Write a SQL query to retrieve the employee ID, first name, role, and department of employees who hold leadership positions (Manager, President, or CEO).
select * from emp_record_table
   ...> where role in ('PRESIDENT', 'MANAGER');

--Write a query to list employee details such as EMP_ID, FIRST_NAME, LAST_NAME, ROLE, DEPARTMENT, and EMP_RATING grouped by dept. Also include the respective employee rating along with the max emp rating for the department. 
SELECT EMP_ID, FIRST_NAME, LAST_NAME, ROLE, DEPT,      
   ...> EMP_RATING, MAX(EMP_RATING)OVER (PARTITION BY DEPT) AS 
   ...> MAX_EMP_RATING FROM emp_record_table;  

--Write a query to calculate the minimum and the maximum salary of the employees in each role. Take data from the employee record table.
SELECT DISTINCT(ROLE), MAX(SALARY) 
   ...> OVER (PARTITION BY ROLE) MAX_SALARY, MIN(SALARY) 
   ...> OVER (PARTITION BY ROLE) MIN_SALARY FROM emp_record_table; 

-- Write a query to assign ranks to each employee based on their experience. Take data from the employee record table.
SELECT EMP_ID, FIRST_NAME, LAST_NAME, DEPT, EXP,
   ...> RANK() OVER (ORDER BY EXP) EXP_RANK,    
   ...> DENSE_RANK() OVER (ORDER BY EXP) EXP_DENSE_RANK 
   ...> FROM emp_record_table;

-- Write a query to create a view that displays employees in various countries whose salary is more than six thousand. Take data from the employee record table. 
create view emp as 
   ...> select EMP_ID, FIRST_NAME, LAST_NAME, country, salary from emp_record_table where salary >6000;
sqlite> select * from emp;

-- Write a nested query to find employees with experience of more than ten years. Take data from the employee record table.
SELECT EMP_ID, FIRST_NAME, LAST_NAME, GENDER, DEPT, ROLE, EXP
   ...> FROM emp_record_table
   ...> WHERE EMP_ID IN (select EMP_ID from emp_record_table WHERE EXP >10); 

--Write a query to calculate the bonus for all the employees, based on their ratings and salaries (Use the formula: 5% of salary * employee rating). 
select EMP_ID, FIRST_NAME, LAST_NAME, country, salary, 
   ...> (0.05*salary*EMP_RATING) as Bonus from emp_record_table;

-- Write a query to calculate the average salary distribution based on the continent and country. Take data from the employee record table. 
select CONTINENT, COUNTRY,avg(salary) as Avg_Salary from emp_record_table group by CONTINENT, COUNTRY;