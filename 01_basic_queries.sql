-- Step 1: Create a basic Employees table
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Department VARCHAR(50),
    Salary DECIMAL(10, 2)
);

-- Step 2: Insert dummy data into the table
INSERT INTO Employees (EmployeeID, FirstName, LastName, Department, Salary) VALUES
(1, 'Amit', 'Sharma', 'IT', 60000.00),
(2, 'Priya', 'Patil', 'HR', 45000.00),
(3, 'Rahul', 'Verma', 'Finance', 55000.00),
(4, 'Sneha', 'Joshi', 'IT', 65000.00);

-- Step 3: Practice Basic Selection Queries

-- 1. Fetch all records
SELECT * FROM Employees;

-- 2. Fetch employees from IT department
SELECT * FROM Employees 
WHERE Department = 'IT';

-- 3. Sort employees by salary in descending order
SELECT * FROM Employees 
ORDER BY Salary DESC;
