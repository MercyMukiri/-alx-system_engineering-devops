#!/usr/bin/python3
"""
Script that prints a list of titles for all hot articles for a
given subreddit
"""
import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """
    Recursively queries Reddit API and returns a list of titles of
    all hot articles for a given subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    try:
        res = requests(url,
                       params={'after': after},
                       headers={'User-agent': 'linux:0x16.api.advanced'},
                       allow_redirects=False).json()

        hot_list = [child.get("data").get("title")
                    for child in res.get("data").get("children")]

        if not hot_list:
            return None

        word_list = list(dict.fromkeys(word_list))

        if word_count == {}:
            word_count = {word: 0 for word in word_list}

        for title in hot_list:
            split_words = title.split(' ')
            for word in word_list:
                for s_word in split_words:
                    if s_word.lower() == word.lower():
                        word_count[word] += 1

        if not res.get("data").get("after"):
            sorted_counts = sorted(word_count.items(), key=lambda kv: kv[0])
            sorted_counts = sorted(word_count.items(),
                                   key=lambda kv: kv[1], reverse=True)
            [print(f"{k}: {v}") for k, v in sorted_counts if v != 0]
        else:
            return count_words(subreddit, word_list, word_count,
                               res.get("data").get("after"))

    except Exception:
        return None
