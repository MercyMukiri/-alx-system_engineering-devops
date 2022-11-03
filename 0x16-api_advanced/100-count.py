#!/usr/bin/python3
"""
Script that prints a list of titles for all hot articles for a
given subreddit
"""
import requests


def count_words(subreddit, word_list, word_count=[], after=None):
    """
    Recursively queries Reddit API and returns a list of titles of
    all hot articles for a given subreddit
    """

    user_agent = {'User-agent': 'test45'}
    posts = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                         .format(subreddit, after), headers=user_agent)

    if after is None:
        word_list = [word.lower() for word in word_list]

    if posts.status_code == 200:
        posts = posts.json()['data']
        aft = posts['after']
        posts = posts['children']

        for post in posts:
            title = post['data']['title'].lower()

            for word in title.split(' '):
                if word in word_list:
                    word_count.append(word)

        if aft is not None:
            count_words(subreddit, word_list, word_count, aft)
        else:
            result = {}

            for word in word_count:
                if word.lower() in result.keys():
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1

            for key, value in sorted(result.items(), key=lambda item: item[1],
                                     reverse=True):
                print('{}: {}'.format(key, value))

    else:
        return
