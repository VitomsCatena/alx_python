#!/usr/bin/python3
"""
Checks student output for returning info from REST API and exports it to CSV
"""
import requests
import sys
import csv

def get_employee_info(employee_id):
    # Fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    employee_data = response.json()

    if response.status_code != 200:
        print(f"Error: Unable to fetch employee data for ID {employee_id}")
        return

    employee_name = employee_data["name"]
    user_id = employee_data["id"]

    # Fetch TODO list for the employee
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todos_url)
    todos_data = response.json()

    if response.status_code != 200:
        print(f"Error: Unable to fetch TODO list for ID {employee_id}")
        return

    # Create CSV file
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write tasks to CSV
        for task in todos_data:
            task_completed_status = "Completed" if task["completed"] else "Not Completed"
            csv_writer.writerow([user_id, employee_name, task_completed_status, task["title"]])

    print(f"CSV data exported to {csv_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    get_employee_info(employee_id)

