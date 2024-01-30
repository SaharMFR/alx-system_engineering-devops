#!/usr/bin/python3
""" Extends task-0 to export data in the CSV format """
import requests
import sys


if __name__ == "__main__":
    ID = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(ID)
    name = requests.get(url).json().get("username")
    tasks = requests.get(url + "/todos").json()

    with open("{}.csv".format(ID), 'w') as f:
        for task in tasks:
            status = task.get("completed")
            title = task.get("title")
            f.write('"{}","{}","{}","{}"\n'.format(ID, name, status, title))
