#!/usr/bin/python3
"""
Function retrieves data from the Reddit API 
and provides the total number of subscribers (excluding active users)
for a specified subreddit. 
In case an invalid subreddit is provided, the function will output a value of 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function retrieves data from the Reddit API
    - If not a valid subreddit, return 0.
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
