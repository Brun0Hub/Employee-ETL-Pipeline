CREATE VIEW vw_department_cost AS

SELECT
    d.department_name,
    SUM(
        e.salary +
        e.meal_allowance +
        e.transport_allowance
    ) AS total_cost
FROM Employees e
INNER JOIN Departments d
    ON e.department_id = d.department_id
GROUP BY d.department_name

SELECT * FROM vw_department_cost