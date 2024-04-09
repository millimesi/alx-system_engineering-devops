#!/usr/bin/python3
'''
Api advanced
'''
import requests


def number_of_subscribers(subreddit):
    '''
    returns the number of subscribers
    (not active users, total subscribers) for a given subreddit
    '''
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Reddit API v1.0"}

    try:
        response = requests.get(
            api_url, allow_redirects=False, headers=headers
            )
        response.raise_for_status()

        data = response.json()
        if "data" in data and "subscribers" in data["data"]:
            return data["data"]["subscribers"]
        else:
            return 0
    except requests.exceptions.RequestException:
        return 0
