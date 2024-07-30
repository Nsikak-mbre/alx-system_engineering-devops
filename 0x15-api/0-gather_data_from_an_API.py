#!/usr/bin/python3
"""
Using REST API, return information about a given employee TODO list progress
"""


import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        sys.exit(1)

    user_data = user_response.json()
    employee_name = user_data.get('name')

    todo_url = (
        f"https://jsonplaceholder.typicode.com/todos"
        f"?userId={employee_id}"
    )
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()
    total_task = len(todo_data)
    completed_task = [task for task in todo_data if task.get('completed')]
    number_of_done_task = len(completed_task)

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          number_of_done_task, total_task))
    for task in completed_task:
        print("\t {}".format(task.get('title')))
