#!/usr/bin/python3
"""export data in the json format."""
import json
import requests


def to_do_list(id):
    """retrieve information about employees """
    url = "https://jsonplaceholder.typicode.com/users/"
    res = requests.get(url + "{}".format(id))
    data1 = res.json()
    EMPLOYEE_NAME = data1["username"]
    url1 = "https://jsonplaceholder.typicode.com/todos/?userId="
    response = requests.get(url1 + "{}".format(id))
    data = response.json()
    row = []
    for i in data:
        new_dict = {}
        new_dict['username'] = EMPLOYEE_NAME
        new_dict['task'] = i['title']
        new_dict['completed'] = i['completed']
        row.append(new_dict)

    final_dict = {}
    final_dict[id] = row
    json_obj = json.dumps(final_dict)
    file = str(id) + ".json"

    with open(file,  "w") as f:
        f.write(json_obj)


if __name__ == "__main__":
    import sys
    employee_id = int(sys.argv[1])
    to_do_list(employee_id)
