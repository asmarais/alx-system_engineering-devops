#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""


import requests
import json

def to_do_list(id):
    """retrieve information about employees """
    response = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(id))
    data = response.json()
    EMPLOYEE_NAME = data["name"]
    response = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(id))
    data = response.json()
    tasks =[]
    for task in data:
        if task["completed"]:
            tasks.append(task["title"])
    NUMBER_OF_DONE_TASKS = len(tasks)
    TOTAL_NUMBER_OF_TASKS = len(data)
    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME, 
    NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task in tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    import sys
    employee_id = int(sys.argv[1])
    to_do_list(employee_id)

