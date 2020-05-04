#!/usr/bin/python3
"""Python script to export data in the CSV format."""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    url1 = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    url2 = "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1]
    user = requests.get(url1).json()
    todolist = requests.get(url2).json()

    file = "" + argv[1] + ".csv"
    with open(file, mode="w") as f:
        task_writer = csv.writer(
            f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for task in todolist:
            task_writer.writerow([argv[1]] + [user.get('username')] +
                                 [task.get("completed")] + [task.get("title")])
