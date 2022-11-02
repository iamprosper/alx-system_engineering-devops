#!/usr/bin/python3
"""
This module contain a function that fetch the top ten subreddit
Function: top_ten(subreddit)
"""
import json
import requests


def top_ten(subreddit):
    """
    This function fetches the top ten subreddit
    Args:
        -subreddit
    """
    header = {'User-agent': 'Chrome'}
    query = {'limit': '10'}
    response = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            headers=header,
                            params=query,
                            allow_redirects=False)
    if response.status_code == 302:
        print(None)
        return
    posts = response.json()["data"]["children"]
    for post in posts:
        print(post["data"]["title"])
