#!/usr/bin/python3
"""
This module contain a single function for checking all subreddits posts'title
Function: recurse(subreddit, hot_list=[]
"""
import requests


def recurse(subreddit, hot_lists=[]):
    """This function gets all hot posts title  and returns them as a list
    Arg:
        -subreddit
        -host_lists
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {'User-agent': 'Chrome'}
    h_list = []
    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code >= 300:
        return None
    data = response.json()
    posts = data["data"]["children"]
    for post in posts:
        title = post["data"]["title"]
        h_list.append(title)
    return h_list
