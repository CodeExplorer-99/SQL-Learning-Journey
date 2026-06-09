-- ==============================================================================
-- 📊 DAY 4: ADVANCED SQL - WINDOW FUNCTIONS & JOINS PRACTICE
-- ==============================================================================

-- 1. Create Sample Tables (Employees & Departments)
CREATE TABLE IF NOT EXISTS employees (
    emp_id INT,
    emp_name VARCHAR(50),
    department VARCHAR(50),
    salary INT
);

-- Insert Sample Dataset
INSERT INTO employees (emp_id, emp_name, department, salary) VALUES 
(1, 'Amit', 'IT', 85000),
(2, 'Rahul', 'IT', 90000),
(3, 'Priya', 'HR', 65000),
(4, 'Neha', 'HR', 65000),
(5, 'Siddharth', 'IT', 90000),
(6, 'Pooja', 'Finance', 75000);


-- 2. WINDOW FUNCTIONS PRACTICE (ROW_NUMBER, RANK, DENSE_RANK)
-- Objective: Rank employees based on their salary within each department
SELECT 
    emp_id, 
    emp_name, 
    department, 
    salary,
    ROW_NUMBER() OVER(PARTITION BY department ORDER BY salary DESC) AS row_num,
    RANK() OVER(PARTITION BY department ORDER BY salary DESC) AS rnk,
    DENSE_RANK() OVER(PARTITION BY department ORDER BY salary DESC) AS dense_rnk
FROM employees;


-- 3. COMMON INTERVIEW QUESTION SOLUTION:
-- Objective: Find the 2nd Highest Salary earner in each department using CTE
WITH RankedSalary AS (
    SELECT 
        emp_name, 
        department, 
        salary,
        DENSE_RANK() OVER(PARTITION BY department ORDER BY salary DESC) AS rnk
    FROM employees
)
SELECT 
    emp_name, 
    department, 
    salary 
FROM RankedSalary 
WHERE rnk = 2;
