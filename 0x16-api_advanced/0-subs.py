#!/usr/bin/python3
""" Finds the number of subscribers for a given subreddit """

import requests


def number_of_subscribers(subreddit):
    """
    Queries the `Reddit API` and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    h = {"User-agent": "My-User-Agent"}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=h)
    res = response.json()

    try:
        return res.get("data").get("subscribers")

    except Exception:
        return 0
