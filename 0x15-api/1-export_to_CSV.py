#!/usr/bin/python3
'''
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
'''


if __name__ == "__main__":
    import csv
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

    # Creating CSV file with 'with' keyword and create CVS writer object
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, "w", newline="") as csv_file:
        for task in user_todos:
            user_name = user_info.get('username')
            task_completedStatus = task.get('completed')
            task_title = task.get('title')

            # Write the information in the csv file
            csv_file.write(f'"{user_id}","{user_name}",'
                           f'"{task_completedStatus}","{task_title}"\n')
