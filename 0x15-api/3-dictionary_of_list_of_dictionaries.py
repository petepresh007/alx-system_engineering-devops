#!/usr/bin/python3
"""python script to export to json"""

import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    resp = requests.get(url)
    Users = resp.json()

    users_dict = {}
    for user in Users:
        userID = user.get('id')
        USERNAME = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(userID)
        url = url + '/todos/'
        resp = requests.get(url)

        tasks = resp.json()
        users_dict[userID] = []
        for task in tasks:
            TASK_COMPLETED_STATUS = task.get('completed')
            TASK_TITLE = task.get('title')
            users_dict[userID].append({
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME
            })
    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_dict, f)
