#!/usr/bin/python3
""" This script queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """ queries the Reddit API and returns the number of subscribers"""

    if subreddit is None or type(subreddit) is not str:
        return 0

    res = requests.get("https://www.reddit.com/r/{}/about.json"
                       .format(subreddit),
                       headers={'User-agent': 'custom'},
                       allow_redirects=False)

    if res.status_code == 404:
        return 0

    return res.json().get("data").get("subscribers")
