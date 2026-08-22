CREATE VIEW vw_headcount_department AS

SELECT
    d.department_name,
    COUNT(*) AS total_employees
FROM Employees e
INNER JOIN Departments d
    ON e.department_id = d.department_id
GROUP BY d.department_name

SELECT * FROM vw_headcount_department
