#!/usr/bin/python3
'''
Api Advanced
'''
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    '''
    returns the number of subscribers
    (not active users, total subscribers) for a given subreddit
    '''
    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Reddit API v1.0"}
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    response = requests.get(
        api_url, allow_redirects=False, params=params, headers=headers
        )
    if response.status_code == 200:
        results = response.json().get("data")
        after = results.get("after")
        count += results.get("dist")

        for ch in results.get("children"):
            hot_list.append(ch.get("data").get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)

        return hot_list
    else:
        return None
