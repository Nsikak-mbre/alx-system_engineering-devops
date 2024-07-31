#!/usr/bin/python3

"""
using REST API to gather todo list progress for a given employee ID, and
exports the data in JSON format.
"""


import json
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        sys.exit(1)
    user_data = user_response.json()
    username = user_data.get('username')

    todo_url = (
        f"https://jsonplaceholder.typicode.com/todos"
        f"?userId={employee_id}"
    )
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()
