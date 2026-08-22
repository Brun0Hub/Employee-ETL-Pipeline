CREATE VIEW vw_employee_summary AS

SELECT
    e.employee_id,
    e.employee_name,
    e.email,
    e.hire_date,
    e.salary,
    d.department_name,
    p.position_name
FROM Employees e
INNER JOIN Departments d
    ON e.department_id = d.department_id
INNER JOIN Positions p
    ON e.position_id = p.position_id;

SELECT * FROM vw_employee_summary