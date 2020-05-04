#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests
from sys import argv

if __name__ == "__main__":
    url1 = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    url2 = "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1]
    user = requests.get(url1).json()
    todolist = requests.get(url2).json()
    done = 0
    tasks_completed = []
    for task in todolist:
        if task["completed"] is True:
            done += 1
            tasks_completed.append(task["title"])
    print("Employee {} is done with tasks({}/{}):".
          format(user['name'], done, len(todolist)))
    for task in tasks_completed:
        print("\t {}".format(task))
