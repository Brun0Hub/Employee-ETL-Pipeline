import pyodbc
import pandas as pd

#Creating the connection python/sql

def db_connection(driver: str, server: str, db: str):

    connection_settings = (
        f"Driver={driver};"
        f"Server={server};"
        f"Database={db};"
    )
    connection = pyodbc.connect(connection_settings)
    print("Connection Established")
    return connection


connection = db_connection(
    "SQL Server",
    "Bruno_Santos",
    "hr_database"
)

cursor = connection.cursor()





#recebe o csv employees

def load_employees(connection, employees):

    cursor = connection.cursor()

    for _, row in employees.iterrows():

        employee_name = row['employee_name']
        email = row['email']
        hire_date = row['hire_date']
        salary = row['salary']
        meal_allowance = row['meal_allowance']
        transport_allowance = row['transport_allowance']
        department_id = row['department_id']
        position_id = row['position_id']

        cursor.execute(
            f"SELECT COUNT(*) FROM Employees WHERE email = '{email}'"
        )

        exists = cursor.fetchone()[0]

        if exists:

            command = f"""
            UPDATE Employees
            SET employee_name = '{employee_name}',
                hire_date = '{hire_date}',
                salary = {salary},
                meal_allowance = {meal_allowance},
                transport_allowance = {transport_allowance},
                department_id = {department_id},
                position_id = {position_id}
            WHERE email = '{email}'
            """

        else:

            command = f"""
            INSERT INTO Employees(
                employee_name,
                email,
                hire_date,
                salary,
                meal_allowance,
                transport_allowance,
                department_id,
                position_id
            )
            VALUES(
                '{employee_name}',
                '{email}',
                '{hire_date}',
                {salary},
                {meal_allowance},
                {transport_allowance},
                {department_id},
                {position_id}
            )
            """

        cursor.execute(command)

    connection.commit()

    print("Employees loaded successfully")




# recebe o csv positions

def load_positions(connection, positions):

    cursor = connection.cursor()

    for _, row in positions.iterrows():

        position_id = row['position_id']
        position_name = row['position_name']

        cursor.execute(
            f"SELECT COUNT(*) FROM Positions WHERE position_id = {position_id}"
        )

        exists = cursor.fetchone()[0]

        if exists:

            command = f"""
            UPDATE Positions
            SET position_name = '{position_name}'
            WHERE position_id = {position_id}
            """

        else:

            command = f"""
            INSERT INTO Positions(
                position_id,
                position_name
            )
            VALUES(
                {position_id},
                '{position_name}'
            )
            """

        cursor.execute(command)

    connection.commit()

    print("Positions loaded successfully")

#recebe o csv departments

def load_departments(connection, departments):

    cursor = connection.cursor()

    for _, row in departments.iterrows():

        department_id = row['department_id']
        department_name = row['department_name']

        cursor.execute(
            f"SELECT COUNT(*) FROM Departments WHERE department_id = {department_id}"
        )

        exists = cursor.fetchone()[0]

        if exists:

            command = f"""
            UPDATE Departments
            SET department_name = '{department_name}'
            WHERE department_id = {department_id}
            """

        else:

            command = f"""
            INSERT INTO Departments(
                department_id,
                department_name
            )
            VALUES(
                {department_id},
                '{department_name}'
            )
            """

        cursor.execute(command)

    connection.commit()

    print("Departments loaded successfully")