#!/usr/bin/python3
""" Gets the titles of the first 10 hot posts in `Reddit API` """

import requests


def top_ten(subreddit):
    """
    Queries the `Reddit API` and prints the titles of the first 10
    hot posts listed for a given subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    h = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
            'AppleWebKit/537.36 (KHTML, like Gecko)',
            'Chrome/121.0.0.0',
            'Safari/537.36'
        ])
    }
    p = {"limit": 10}
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    response = get(url, headers=h, params=p)
    results = response.json()

    try:
        data = results.get("data").get("children")

        for i in data:
            print(i.get("data").get("title"))

    except Exception:
        print("None")
