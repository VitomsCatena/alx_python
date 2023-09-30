
import requests
import csv
import sys

def get_employee_info(employee_id):
    # Fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    employee_data = response.json()

    if response.status_code != 200:
        print(f"Error: Unable to fetch employee data for ID {employee_id}")
        return

    user_id = employee_data["id"]
    username = employee_data["username"]

    # Fetch TODO list for the employee
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todos_url)
    todos_data = response.json()

    if response.status_code != 200:
        print(f"Error: Unable to fetch TODO list for ID {employee_id}")
        return

    # Create and write to CSV file
    csv_file_name = f"{user_id}.csv"
    with open(csv_file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todos_data:
            task_completed = "True" if task["completed"] else "False"
            csv_writer.writerow([user_id, username, task_completed, task["title"]])

    print(f"Data exported to {csv_file_name}")

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

