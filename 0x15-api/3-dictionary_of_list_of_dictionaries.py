#!/usr/bin/python3
"""
Using REST API to gather todo list progress, and
exports the data in JSON format.
"""

import json
import requests

if __name__ == "__main__":
    # Fetch user data
    users_response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = users_response.json()

    # Create dictionary to hold data
    todo_data = {}

    # Loop through each user
    for user in users:
        user_id = user['id']
        username = user['username']

        # Fetch todo for the user
        todo_response = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')
        todos = todo_response.json()

        tasks = []

        for todo in todos:
            task_info = {
                "username": username,
                "task": todo['title'],
                "completed": todo['completed']
            }
            tasks.append(task_info)

        todo_data[user_id] = tasks

    # Write the data to a JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(todo_data, json_file)
