#!/usr/bin/python3
"""
Checks student output for returning info from REST API
"""
import requests
import sys

def get_employee_info(employee_id):
    # Fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    employee_data = response.json()

    if response.status_code != 200:
        print(f"Error: Unable to fetch employee data for ID {employee_id}")
        return

    employee_name = employee_data["name"]

    # Fetch TODO list for the employee
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todos_url)
    todos_data = response.json()

    if response.status_code != 200:
        print(f"Error: Unable to fetch TODO list for ID {employee_id}")
        return

    # Calculate completed tasks
    completed_tasks = [todo for todo in todos_data if todo["completed"]]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos_data)

    # Display employee progress
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

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

