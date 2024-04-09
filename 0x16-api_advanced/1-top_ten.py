#!/usr/bin/python3
import requests


def top_ten(subreddit):
    '''
    returns the number of subscribers
    (not active users, total subscribers) for a given subreddit
    '''
    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Reddit API v1.0"}

    try:
        response = requests.get(
            api_url, allow_redirects=False, headers=headers
            )
        response.raise_for_status()

        data = response.json()
        if 'data' in data and 'children' in data['data']:
                for post in data['data']['children']:
                    print(post['data']['title'])
        else:
            print("None")
    except requests.exceptions.RequestException:
        print("None")
