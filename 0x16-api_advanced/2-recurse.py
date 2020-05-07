#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """recursive method"""
    url = "https://reddit.com/r/" + subreddit + "/hot.json?&after=" + after
    headers = {'user-agent': 'Chrome/81.0.4044.129'}
    reddit = requests.get(url, headers=headers).json()
    if 'error' in reddit or len(reddit['data']['children']) == 0:
        return None
    children = reddit['data']['children']
    for child in children:
        hot_list.append(child['data']['title'])
    after = reddit['data']['after']
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
