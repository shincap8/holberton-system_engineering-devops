#!/usr/bin/python3
"""Python script to export data in the JSON format."""
import json
import requests


if __name__ == "__main__":
    url1 = "https://jsonplaceholder.typicode.com/users"
    url2 = "https://jsonplaceholder.typicode.com/todos"
    users = requests.get(url1).json()
    todolist = requests.get(url2).json()

    file = "todo_all_employees.json"
    json_dict = {}
    for user in users:
        all_tasks = []
        for task in todolist:
            if task["userId"] == user["id"]:
                dictionary = {}
                dictionary["task"] = task.get("title")
                dictionary["completed"] = task.get("completed")
                dictionary["username"] = user.get("username")
                all_tasks.append(dictionary)
        json_dict[user["id"]] = all_tasks
    with open(file, "w") as f:
        json.dump(json_dict, f)
