#!/usr/bin/python3
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    '''
    returns the number of subscribers
    (not active users, total subscribers) for a given subreddit
    '''
    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "Reddit API v1.0"}
    
    params = {}
    if after:
        params["after"] = after

    response = requests.get(api_url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    respons_json = response.json()
    children = respons_json["data"]["children"]

    for posts in children:
        title = posts["data"]["title"].lower()
        for w in word_list:
            if w.lower() in title:
                counts[w] = counts.get(w, 0) + title.count(w.lower())

    after = respons_json["data"]["after"]
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_count = sorted(counts.items(),
                               key=lambda x: (-x[1], x[0].lower()))
        for w, count in sorted_count:
            print(f"{w.lower()}: {count}")
