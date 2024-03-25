#!/usr/bin/python3
"""
get users todo list from an api and display all the todos
with some certain criteria
"""


import requests
import sys
res = requests.get(f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}")
employee_data = res.json()
employee_name = employee_data.get("name")

res_todo = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={sys.argv[1]}"
        )
emp_todo = res_todo.json()
t_task = len(emp_todo)
com_task = [task for task in emp_todo if task.get("completed")]
len_compl = len(com_task)
print(
  f"Employee {employee_name} is done with tasks({len_compl}/{t_task}):"
  )
for task in com_task:
    print(f"\t{task.get('title')}")
