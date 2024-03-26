#!/usr/bin/python3
'''
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
'''


if __name__ == "__main__":
    import requests
    import sys

    api_url_3 = "https://jsonplaceholder.typicode.com/"
    user_id = int(sys.argv[1])
    # Get the dictionary for the user of given id
    user_infoResponse = requests.get('{}users/{}'.format(api_url_3, user_id))
    user_info = user_infoResponse.json()

    # Get the list of todos list of the specified user id
    params = {'userId': user_id}
    user_todosResponse = requests.get('{}{}'.format(api_url_3, 'todos'), params=params)
    user_todos = user_todosResponse.json()

    # Create the completed tasks empty list and append completed task 
    # If its completed key is True
    task_completed = []
    for task in user_todos:
        if task.get('completed') == True:
            task_completed.append(task.get('title'))
    # print the information according to the requirments
    print(f"Employee {user_info.get('name')} is done with tasks({len(task_completed)}/{len(user_todos)}):")
    for task in task_completed:
        print(f"\t {task}")
