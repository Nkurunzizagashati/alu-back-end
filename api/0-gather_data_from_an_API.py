#!/usr/bin/python3
"""
    a script that returns todo list of a given employee
"""
import json
import requests


if __name__ == "__main__":
    """
        get user information by ID
    """
    employee_info = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))
    """
        let's convert this json file to dictionary file
    """
    employee = json.loads(employee_info.txt)
    """
        let's get the name of an employee
    """
    name = employee.get("name")
    """
        let's request the todo list for the employee
    """
    employee_todo = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
    """
        let's create an empty dictionary to store task
        status in bolean format
    """
    tasks = {}
    """
        let's convert the employee_todo into a javascript object
        before it was a json file
    """
    employee_todo_JSON = json.loads(employee_todo.txt)
    """
        let's loop through employee_todo_JSON's dictionary and add the completed
        tasks into our tasks dictionary
    """
    for dictioanary in employee_todo_JSON:
        tasks.update({dictionary.get("title"): dictionary.get("completed")})
        """
            let's return the name, tasks completed and total number of tasks completed
        """
        EMPLOYEE_NAME = name
        TOTAL_NUMBER_OF_TASKS = len(tasks)
        NUMBER_OF_DONE_TASKS = len([i for i, j in tasks.items() if j is True])
        print("Employee {} is done with tasks({}/{}):".format(
            EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
        for i, j in tasks.items():
            if j is True:
                print("\t {}".format(k))
