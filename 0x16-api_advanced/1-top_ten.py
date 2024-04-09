#!/usr/bin/python3
"""a module to import"""
import requests


def top_ten(subreddit):
    """module to send a requests"""
    headers = {'User-Agent': 'MyBot/1.0'}
    red_api = requests.get(
            f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10",
            headers=headers
            )
    if red_api.status_code == 200:
        data = red_api.json()
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    elif red_api.status_code == 404:
        print(None)
