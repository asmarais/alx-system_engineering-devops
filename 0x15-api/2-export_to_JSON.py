#!/usr/bin/python3
"""export data in the json format."""


import requests
import json
import csv

def to_do_list(id):
    """retrieve information about employees """
    response = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(id))
    data1 = response.json()
    EMPLOYEE_NAME = data1["username"]
    response = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(id))
    data = response.json()
    row =[]
    for i in data:
        new_dict = {}
        new_dict['username'] = EMPLOYEE_NAME
        new_dict['task'] = i['title']
        new_dict['completed'] = i['completed']
        row.append(new_dict)

    final_dict = {}
    final_dict[id] = row
    json_obj = json.dumps(final_dict)
    file ="{}.json".format(id)

    with open(file,  "w") as f:
        f.write(json_obj)

    
if __name__ == "__main__":
    import sys
    employee_id = int(sys.argv[1])
    to_do_list(employee_id)
