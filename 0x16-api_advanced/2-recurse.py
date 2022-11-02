#!/usr/bin/python3
"""
This module contain a single function for checking all subreddits posts'title
Function: recurse(subreddit, hot_list=[])
"""
import requests


def recurse(subreddit):
    """This function gets all hot posts title  and returns them as a list
    Arg:
        -subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    header = {'User-agent': 'Chrome'}
    h_list = []

    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code >= 300:
        return None

    return paginate(subreddit, url, None, header, h_list)


def paginate(subreddit, url, after, header, hot_list):
    """This function paginates throught the results to catch each post'title
    Args:
        -subreddit: The subreddit
        -url: The url of the endpoint
        -header: The header complementary
        -hot_list: The list of hot posts
    """
    params = {'after': after}
    response = requests.get(url, headers=header,
                            params=params,
                            allow_redirects=False)
    next_page = response.json().get("data").get("after")
    posts = response.json().get("data").get("children")
    for post in posts:
        title = post.get("data").get("title")
        # print(title)
        hot_list.append(title)
    if next_page:
        return paginate(subreddit, url, next_page, header, hot_list)
    return hot_list
