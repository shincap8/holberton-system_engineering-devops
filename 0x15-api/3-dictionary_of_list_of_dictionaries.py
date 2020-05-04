#!/usr/bin/python3
"""Python script to export data in the JSON format."""
import requests
import json

if __name__ == "__main__":
    url1 = "https://jsonplaceholder.typicode.com/users"
    url2 = "https://jsonplaceholder.typicode.com/todos"
    users = requests.get(url1).json()
    todolist = requests.get(url2).json()

    file = "todo_all_employees.json"
    task_completed = []
    json_dict = {}
    for user in users:
        for task in todolist:
            if task["userId"] == user["id"]:
                dictionary = {}
                dictionary["task"] = task["title"]
                dictionary["completed"] = task["completed"]
                dictionary["username"] = user["username"]
                task_completed.append(dictionary)
        json_dict[user["name"]] = task_completed
    with open(file, "w") as f:
        json.dump(json_dict, f)
