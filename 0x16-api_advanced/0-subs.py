#!/usr/bin/python3
"""function that queries the Reddit API and returns the
number of subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """method to return the number of suscribers"""
    url = "https://reddit.com/r/" + subreddit + ".json"
    headers = {
        'user-agent': 'Chrome/81.0.4044.129'
    }
    reddit = requests.get(url, headers=headers).json()
    if 'error' in reddit:
        return 0
    if type(reddit['data']['children'][0]['data']
            ['subreddit_subscribers']) == int:
        return reddit['data']['children'][0]['data']['subreddit_subscribers']
    return 0
