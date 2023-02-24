#!/usr/bin/python3
"""
    a script that uses API for a given employee ID and returns
    a list of his/her todo list
"""
import json
import requests
import sys


if __name__ == "__main__":
    """ get employee ID and make it int """
    employee_ID = int(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com'
    """ request the information of an employee using ID """
    response = requests.get(
            f'{url}/users/{employee_ID}')
    EMPLOYEE_NAME = response.json()['name']
    """ request the employee's todo list """
    todo_response = requests.get(f'{url}/todos?userId={employee_ID}')
    todo_list = todo_response.json()
    NUMBER_OF_DONE_TASKS = sum(task['completed'] for task in todo_list)
    TOTAL_NUMBER_OF_TASKS = len(todo_list)
    tasks = {}
    for dictionary in todo_list:
        tasks.update({dictionary.get("title"): dictionary.get("completed")})
    """ print the employee's progress """
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for k, v in tasks.items():
        if v is True:
            print("\t {}".format(k))
