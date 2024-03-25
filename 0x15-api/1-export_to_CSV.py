#!/usr/bin/python3
""" Export api to a csv format"""
import csv
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

    with open('{}.csv'.format(userID), 'w') as csvfile:
        for task in tasks:
            completed = task.get('completed')
            title_task = task.get('title')
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                userID, username, completed, title_task))
