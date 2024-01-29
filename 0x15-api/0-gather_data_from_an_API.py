#!/usr/bin/python3
"""
Returns information about a given employee's TODO list
progress, using a REST API, for his/her ID.
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users/{}".format(sys.argv[1])).json()
    tasks = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    done = [t.get("title") for t in tasks if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(done), len(tasks)))
    [print("\t {}".format(task)) for task in done]
