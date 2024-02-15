#!/usr/bin/python3
""" Finds the number of subscribers for a given subreddit """

import requests


def number_of_subscribers(subreddit):
    """
    Queries the `Reddit API` and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """

    if subreddit is None or type(subreddit) is not str:
        return 0
    response = requests.get('http://www.reddit.com/r/{}/about.json'.format(
        subreddit), headers={'User-Agent': 'My-User-Agent'}).json()
    return response.get("data", {}).get("subscribers", 0)
