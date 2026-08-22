CREATE VIEW vw_department_salary AS

SELECT
    d.department_name,
    COUNT(e.employee_id) AS total_employees,
    AVG(e.salary) AS average_salary,
    MIN(e.salary) AS minimum_salary,
    MAX(e.salary) AS maximum_salary,
    SUM(e.salary) AS total_salary
FROM Employees e
INNER JOIN Departments d
    ON e.department_id = d.department_id
GROUP BY
    d.department_name;

SELECT * FROM vw_department_salary