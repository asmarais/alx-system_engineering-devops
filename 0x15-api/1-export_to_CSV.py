#!/usr/bin/python3
"""export data in the CSV format."""
import csv
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

    csv_file = "{}.csv".format(id)

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for i in data:

            row = []
            row.append(id)
            row.append(EMPLOYEE_NAME)
            row.append(i['completed'])
            row.append(i['title'])

            writer.writerow(row)


if __name__ == "__main__":
    import sys
    employee_id = int(sys.argv[1])
    to_do_list(employee_id)
