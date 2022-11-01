#!/usr/bin/python3
"""
This module is used for scrapping reddit app

Args (cli):
-subreddit: The subreddit information to search

Functions: number_of_subscribers(subreddit)
"""
import json
import requests


def number_of_subscribers(subreddit):
    """This function performs the researches on subreddit's subscribers
    Args:
    -subreddit: The subreddit to search
    """
    response = requests.get("https://reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={'User-agent': 'Chrome'})
    if ('error' in response.json()):
        return 0
    sub = response.json()["data"]["subscribers"]
    return (sub)
