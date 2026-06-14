# SQL-Learning-Journey
My SQL practice codes from scratch

---

## 📅 Day 1: SQL Basics
- Learned foundational SQL concepts.
- Created basic queries and uploaded `01_basic_queries.sql`.

## 📅 Day 2: PySpark SQL Introduction
- Setup PySpark environment with Python and Java (`JAVA_HOME`) paths.
- Created multiple DataFrames (`df`, `df1`, `cust`, `prod`) from raw structured data.
- Registered DataFrames as Temporary Views using `createOrReplaceTempView()`.
- Prepared the environment to run standard SQL queries on Big Data.


---

## 📅 Day 3: Advanced SQL with PySpark
- Implemented Spark SQL using temporary views.
- Practiced filtering with WHERE, IN, LIKE, and NULL conditions.
- Learned aggregate functions like COUNT, SUM, MIN, and MAX.
- Used CASE WHEN for conditional transformations.
- Explored string functions: CONCAT, LOWER, UPPER, TRIM, SUBSTRING, and SPLIT.
- Applied NULL handling using the COALESCE function.
- Performed GROUP BY with multiple aggregations and DISTINCT for data cleaning.
- Practiced set operations: UNION vs UNION ALL.
- Applied HAVING clause for post-aggregation filtering.
- Implemented Window Functions: ROW_NUMBER(), DENSE_RANK(), LEAD(), and LAG().
- Learned Join Types: INNER, LEFT, RIGHT, FULL, and LEFT ANTI JOIN.


## 📅 Day 4: Deep Dive into Window Functions & CTEs
- Created a comprehensive practice script `04_advanced_sql_queries.sql` to implement advanced querying techniques.
- Analyzed the practical differences between ranking functions: `ROW_NUMBER()`, `RANK()`, and `DENSE_RANK()`.
- Applied `PARTITION BY` and `ORDER BY` clauses to compute structural metrics within data groups.
- Mastered Common Table Expressions (CTEs) using the `WITH` clause to write cleaner, modular, and more readable queries.
- Solved a popular industry interview problem: Extracting the **2nd Highest Salary** in each department dynamically 

