#!/usr/bin/python3
'''
Python script that, using this REST API, for a given employee ID,
returns information about his/her todo list progress.
'''


if __name__ == "__main__":
    import json
    import requests
    import sys

    api_url_3 = "https://jsonplaceholder.typicode.com/"
    all_todosResponse = requests.get('{}{}'.format(
                                      api_url_3, 'todos'))
    all_todos = all_todosResponse.json()

    # Create Set and append user Ids
    user_idSet = set()
    for user_todo in all_todos:
        user_idSet.add(int(user_todo.get('userId')))

    # conver the set to list and sort it
    user_idList = sorted(list(user_idSet))

    # create the main dict
    main_dict = {}

    # for each user id create list of all tasks dict
    for user_id in user_idList:
        task_list = []
        user_infoResponse = requests.get('{}users/{}'.format(
                                         api_url_3, user_id))
        user_info = user_infoResponse.json()
        params = {'userId': user_id}
        user_todosResponse = requests.get('{}{}'.format(
                                      api_url_3, 'todos'),
                                      params=params)
        user_todos = user_todosResponse.json()
        for task in user_todos:
            task_dict = {"username": user_info.get('username'),
                         "task": task.get('title'),
                         "completed": task.get('completed'),
                         }
            task_list.append(task_dict)
        main_dict[f"{user_id}"] = task_list
    # Creating Json file with 'with' keyword and create the file with dump
    json_filename = "todo_all_employees.json"
    with open(json_filename, "w", newline="") as json_file:
        json.dump(main_dict, json_file)
