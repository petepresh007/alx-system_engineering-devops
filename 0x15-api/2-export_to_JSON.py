#!/usr/bin/python3
""" Export api to a json format"""
import json
import requests
import sys


if __name__ == '__main__':
    userID = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/' + userID
    res = requests.get(url)
    username = res.json().get('username')
    task = url + '/todos'
    res = requests.get(task)
    tasks = res.json()

    data = {userID: []}
    for task in tasks:
        comp_task = task.get("complete")
        task_title = task.get("title")
        data[userID].append({
            "task": task_title,
            "completed": comp_task,
            "username": username
            })
    with open("{}.json".format(userID), "w") as f:
        json.dump(data, f)
