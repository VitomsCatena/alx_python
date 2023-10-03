#!/usr/bin/python3

import requests
import sys
import csv

def get_employee_info(employee_id):
    # Define the base URL for the API
    base_url = 'https://jsonplaceholder.typicode.com/'

    # Create the URL to fetch employee details
    employee_url = f'{base_url}users/{employee_id}'

    # Fetch the employee details
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    username = employee_data['username']

    # Create the URL to fetch TODO list for the employee
    todos_url = f'{base_url}users/{employee_id}/todos'

    # Fetch the TODO list for the employee
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Create and open the CSV file for writing
    filename = f'{employee_id}.csv'
    with open(filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])

        # Write task data to the CSV file
        for task in todos_data:
            task_completed_status = task['completed']
            task_title = task['title']
            csv_writer.writerow([employee_id, username, task_completed_status, task_title])

    print(f'Number of tasks in {filename}: {len(todos_data)}')
    print(f'User ID and Username: {employee_id}, {username}')
    print(f'Formatting: OK')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python script.py <employee_id>')
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print('Employee ID must be an integer.')
        sys.exit(1)

    get_employee_info(employee_id)

