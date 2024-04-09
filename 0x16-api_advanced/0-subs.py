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
    response = requests.get(api_url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
