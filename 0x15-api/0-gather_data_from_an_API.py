#!/usr/bin/python3
"""
get users todo list from an api
"""
import requests
import sys


res = requests.get(f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}")
if res.status_code != 200:
    print("an error occured")
employee_data = res.json()
employee_name = employee_data["name"]

res_todo = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={sys.argv[1]}"
        )
if res_todo.status_code != 200:
    print("an error occured")
emp_todo = res_todo.json()

total_task = len(emp_todo)
completed_task = [task for task in emp_todo if task["completed"]]
len_completedtask = len(completed_task)
print(f"{employee_name} is done with tasks({len_completedtask}/{total_task}):")
for task in completed_task:
    print(f"\t{task['title']}")
