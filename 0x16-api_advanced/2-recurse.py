#!/usr/bin/python3
""" Queries the `Reddit API` and get the title's list recursively """

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Recursive function that queries the `Reddit API` and returns a list
    containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, the function should
    return None.
    """

    if after is None:
        return hot_list
    
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    h = {"User-Agent": "My-User-Agent"}
    p = {"after": after}
    
    response = requests.get(url, headers=h, params=p, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json().get("data")
        children = data.get("children")
        aftr = data.get("after")
        for child in children:
            hot_list.append(child.get("data").get("title"))
    else:
        return None

    return recurse(subreddit, hot_list, aftr)
