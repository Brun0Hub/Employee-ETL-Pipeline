# Employee ETL Pipeline

A simple end-to-end data pipeline that demonstrates how HR data can be ingested from CSV files, stored and transformed in SQL Server, and consumed through Power BI dashboards.

## Technologies

- Python
- Pandas
- SQL Server
- Power BI
- Git

## Project Overview

This project simulates an HR data workflow:

1. CSV files are used as the data source.
2. Python loads the data into SQL Server.
3. Existing records are updated and new records are inserted.
4. SQL Views prepare the data for reporting and analysis.
5. Power BI consumes the Views and presents business insights through dashboards.

## Data Flow

CSV Files
    ↓
Python ETL
    ↓
SQL Server Tables
    ↓
SQL Views
    ↓
Power BI Dashboard


## SQL Views

vw_employee_summary

Provides a complete employee view, including department and position information.

vw_headcount_department

Displays the number of employees by department.

vw_department_salary

Provides salary metrics by department.

vw_department_cost

Calculates total department costs, including salaries and employee benefits.

## Power BI Dashboard

The dashboard was built to demonstrate the final consumption layer of the pipeline and includes:

Total Employees
Total Departments
Average Salary
Total Company Cost
Employees by Department
Department Cost Analysis
Employee Details Matrix
Objective

The purpose of this project is to demonstrate data ingestion, transformation, and presentation using a simple ETL workflow built with Python, SQL Server, and Power BI.
