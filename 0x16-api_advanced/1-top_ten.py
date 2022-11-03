#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
    """

    if subreddit is None or type(subreddit) is not str:
        print('None')

    res = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                       .format(subreddit),
                       headers={'User-agent': 'custom'},
                       allow_redirects=False,
                       params={'limit': 10})

    if res.status_code == 400:
        print('None')
    else:
        for child in res.json().get("data").get("children"):
            print(child.get('data').get('title'))
