#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """method to print the top 10"""
    url = "https://reddit.com/r/" + subreddit + "/hot.json"
    headers = {'user-agent': 'Chrome/81.0.4044.129'}
    reddit = requests.get(url, headers=headers).json()
    if 'error' in reddit or len(reddit['data']['children']) == 0:
        print(None)
        return
    children = reddit['data']['children']
    count = 0
    for child in children:
        if count == 10:
            return
        print(child['data']['title'])
        count += 1
