#!/usr/bin/python3
'''
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
'''


if __name__ == "__main__":
    import json
    import requests
    import sys

    api_url_3 = "https://jsonplaceholder.typicode.com/"
    user_id = int(sys.argv[1])
    # fetch the dictionary for the user of given id
    user_infoResponse = requests.get('{}users/{}'.format(api_url_3, user_id))
    user_info = user_infoResponse.json()

    # Get the list of todos list of the specified user id
    params = {'userId': user_id}
    user_todosResponse = requests.get('{}{}'.format(
                                      api_url_3, 'todos'),
                                      params=params)
    user_todos = user_todosResponse.json()
    # Creating Json file with 'with' keyword and create the file with dump
    json_filename = f"{user_id}.json"
    with open(json_filename, "w", newline="") as json_file:
        # create empty task list
        task_list = []

        # create the inside dict
        for task in user_todos:
            task_dict = {"task": task.get('title'),
                         "completed": task.get('completed'),
                         "username": user_info.get('username')}
            task_list.append(task_dict)
        # create the outside dict
        json_dict = {f"{user_id}": task_list}
        json.dump(json_dict, json_file)
