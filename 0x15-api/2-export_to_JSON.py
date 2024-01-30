#!/usr/bin/python3
""" Extends task-0 to export data in the JSON format """
import requests
import sys


if __name__ == "__main__":
    ID = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(ID)
    username = requests.get(url).json().get("username")
    tasks = requests.get(url + "/todos").json()

    with open("{}.json".format(ID), 'w') as f:
        f.write('{"' + ID + '": [')
        for task in tasks:
            status = str(task.get("completed")).lower()
            f.write('{"task": "' + task.get("title") + '", ')
            f.write('"completed": ' + status + ', ')
            f.write('"username": "' + username + '"}')
            if task != tasks[-1]:
                f.write(', ')
        f.write(']}')
