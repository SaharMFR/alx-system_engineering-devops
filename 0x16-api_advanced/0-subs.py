#!/usr/bin/python3
""" Finds the number of subscribers for a given subreddit """

import requests


def number_of_subscribers(subreddit):
    """
    Queries the `Reddit API` and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    h = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, headers=h, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    return 0
