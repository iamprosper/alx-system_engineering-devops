#!/usr/bin/python3
import requests
import json


"""
This module is used for scrapping reddit app

Args (cli):
-subreddit: The subreddit information to search

Functions: number_of_subscribers(subreddit)
"""


def number_of_subscribers(subreddit):
    """This function performs the researches on subreddit's subscribers
    Args:
    -subreddit: The subreddit to search
    """
    response = requests.get("https://reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={'User-agent': 'Chrome'})
    sub = response.json()["data"]["subscribers"]
    return (sub)


number_of_subscribers("programming")
