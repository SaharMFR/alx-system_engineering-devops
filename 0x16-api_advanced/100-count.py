#!/usr/bin/python3
""" Queries the `Reddit API` recursively """

import requests


def count_words(subreddit, word_list, after='', word_dict={}):
    """
    Recursive function that queries the `Reddit API`,
    parses the title of all hot articles, and prints a sorted count
    of given keywords (case-insensitive, delimited by spaces.
    `Javascript` should count as `javascript`, but `java` should not).
    """

    if not word_dict:
        for word in word_list:
            if word.lower() not in word_dict:
                word_dict[word.lower()] = 0

    if after is None:
        dictionary = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word in dictionary:
            if word[1]:
                print("{}: {}".format(word[0], word[1]))
        return None

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    h = {"User-Agent": "My-User-Agent"}
    p = {"limit": 100, "after": after}
    response = requests.get(url, headers=h, params=p, allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        hot_posts = response.json()["data"]["children"]
        aftr = response.json()["data"]["after"]
        for post in hot_posts:
            title = post["data"]["title"]
            lower = [word.lower() for word in title.split(' ')]

            for word in word_dict.keys():
                word_dict[word] += lower.count(word)

    except Exception:
        return None

    count_words(subreddit, word_list, aftr, word_dict)
