#!/usr/bin/python3
"""export data in the json format."""
import json
import requests


def to_do_list():
    """retrieve information about employees """
    url = "https://jsonplaceholder.typicode.com/users"
    res = requests.get(url)
    data1 = res.json()
    url1 = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url1)
    data = response.json()
    new_dict1 = {}

    for j in data1:

        row = []
        for i in data:

            new_dict2 = {}

            if j['id'] == i['userId']:

                new_dict2['username'] = j['username']
                new_dict2['task'] = i['title']
                new_dict2['completed'] = i['completed']
                row.append(new_dict2)

        new_dict1[j['id']] = row

    with open("todo_all_employees.json",  "w") as f:

        json_obj = json.dumps(new_dict1)
        f.write(json_obj)


if __name__ == "__main__":
    to_do_list()
