#!/usr/bin/env python3
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
    response = requests.get("https://reddit.com/r/{}/new.json"
                            .format(subreddit),
                            headers=header,
                            params=query)
    if (not response.json()["data"]["after"]):
        print("None")
    posts = response.json()["data"]["children"]
    for post in posts:
        print(post["data"]["title"])
