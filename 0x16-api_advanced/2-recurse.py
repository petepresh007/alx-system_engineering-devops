#!/usr/bin/python3
"""A module to send a request"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """function to send the request"""
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'MyBot/1.0'}
    if after:
        url += f"&after={after}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])
        if data['data']['after']:
            return recurse(subreddit, hot_list, data['data']['after'])
        else:
            return hot_list
    elif response.status_code == 404:
        return None
