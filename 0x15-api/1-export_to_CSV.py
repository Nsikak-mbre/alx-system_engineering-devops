#!/usr/bin/python3
"""
exporting api data in the CSV format
"""


import csv
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

    csv_file = "{}.csv".format(employee_id)

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todo_data:
            writer.writerow([employee_id, username, task.get(
                'completed'), task.get('title')])
        print("Data from employee ID {} has been exported to {}".format(
            employee_id, csv_file))
