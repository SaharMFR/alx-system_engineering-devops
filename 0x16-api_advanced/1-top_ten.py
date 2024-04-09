#!/usr/bin/python3
""" Gets the titles of the first 10 hot posts in `Reddit API` """

import requests


def top_ten(subreddit):
    """
    Queries the `Reddit API` and prints the titles of the first 10
    hot posts listed for a given subreddit
    """

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    h = {"User-Agent": "My-User-Agent"}
    p = {"limit": 9}

    response = requests.get(url, headers=h, params=p)

    if response.status_code == 200:
        data = response.json().get("data").get("children")
        for d in data:
            print(d.get("data").get("title"))
    else:
        print("None")
