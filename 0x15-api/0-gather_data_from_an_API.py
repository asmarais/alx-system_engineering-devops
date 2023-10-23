#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import json
import requests


def to_do_list(id):
    """retrieve information about employees """
    url = "https://jsonplaceholder.typicode.com/users/"
    res = requests.get(url + "{}".format(id))
    data1 = res.json()
    EMPLOYEE_NAME = data1["name"]
    url1 = "https://jsonplaceholder.typicode.com/todos/?userId="
    response = requests.get(url1 + "{}".format(id))
    data = response.json()
    tasks = []
    for task in data:
        if task["completed"]:
            tasks.append(task["title"])
    NUMBER_TASKS = len(tasks)
    TOTAL_TASKS = len(data)
    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          NUMBER_TASKS,
                                                          TOTAL_TASKS))
    for task in tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    import sys
    employee_id = int(sys.argv[1])
    to_do_list(employee_id)
