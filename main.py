from src.hr_management import (
    db_connection,
    load_positions,
    load_departments,
    load_employees
)

import pandas as pd


def main():

    employees = pd.read_csv("data/employees.csv")
    positions = pd.read_csv("data/positions.csv")
    departments = pd.read_csv("data/departments.csv")

    connection = db_connection(
        "SQL Server",
        "Bruno_Santos",
        "hr_database"
    )

    load_positions(connection, positions)
    load_departments(connection, departments)
    load_employees(connection, employees)

    connection.close()

    print("Process completed successfully")


if __name__ == "__main__":
    main()


main()