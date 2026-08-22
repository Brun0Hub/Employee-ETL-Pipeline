-- HR management project

-- Creating the Database
CREATE DATABASE hr_database

-- Selecting our new database
USE hr_database

-- Creating our tables

-- Table 1: Departments
CREATE TABLE Departments (
		department_id INT PRIMARY KEY,
		department_name VARCHAR(100)
)

INSERT INTO Departments(department_id,department_name)
		VALUES(2,'Human Resources')


-- Table 2: Positions
CREATE TABLE Positions (
		position_id INT PRIMARY KEY,
		position_name VARCHAR (100)
)

INSERT INTO Positions(position_id,position_name)
		VALUES(1,'Junior Analyst')


-- Table 3: Employees
CREATE TABLE Employees (
		employee_id INT IDENTITY(1,1) PRIMARY KEY,
		employee_name VARCHAR(100) NOT NULL,
		email VARCHAR(100) NOT NULL,
		hire_date DATE NOT NULL,
		salary DECIMAL(10,2) NOT NULL,
		meal_allowance DECIMAL(10,2) NOT NULL,
		transport_allowance DECIMAL (10,2) NOT NULL,
		department_id INT NOT NULL,
		position_id INT NOT NULL,
		CONSTRAINT Departments_department_id_fk FOREIGN KEY(department_id) REFERENCES Departments(department_id),
		CONSTRAINT Positions_position_id_fk FOREIGN KEY(position_id) REFERENCES Positions(position_id),
		CONSTRAINT Employees_email_un UNIQUE(email)
)

INSERT INTO Employees(employee_name,email,hire_date,salary,meal_allowance,transport_allowance,department_id,position_id)
		VALUES('Bruno Souza','bruno.souza@company.com','2020-05-13',4200,1200,250,2,1)




