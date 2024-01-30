#!/usr/bin/python3
""" Extends task-0 to export data in the JSON format """
import requests
import sys
import json


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    users = requests.get(url).json()

    dictionary = {}
    for user in users:
        ID = user.get("id")
        tasks = requests.get(url + str(ID) + "/todos").json()
        dictionary[ID] = []
        for task in tasks:
            dictionary[ID].append({
                "username": user.get("username"),
                "task": task.get("title"),
                "completed": task.get("completed")
            })

    with open("todo_all_employees.json", 'w') as f:
        json.dump(dictionary, f)
