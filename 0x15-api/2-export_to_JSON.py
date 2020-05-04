#!/usr/bin/python3
"""Python script to export data in the JSON format."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url1 = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    url2 = "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1]
    user = requests.get(url1).json()
    todolist = requests.get(url2).json()

    file = "" + argv[1] + ".json"
    task_completed = []
    json_dict = {}
    for task in todolist:
        dictionary = {}
        dictionary["task"] = task["title"]
        dictionary["completed"] = task["completed"]
        dictionary["username"] = user["username"]
        task_completed.append(dictionary)
    json_dict[argv[1]] = task_completed
    with open(file, "w") as f:
        json.dump(json_dict, f)
