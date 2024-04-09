#!/usr/bin/python3
"""a module to import"""
import requests
import sys


def number_of_subscribers(subreddit):
    """module to send a requests"""
    headers = {'User-Agent': 'MyBot/1.0'}
    red_api = requests.get(
            f"https://www.reddit.com/r/{subreddit}/about.json",
            headers=headers
            )
    if red_api.status_code == 200:
        data = red_api.json()
        subscribers = data.get("data").get("subscribers")
        return subscribers
    elif red_api.status_code == 404:
        return 0


if __name__ == "__main__":
    number_of_subscribers(sys.argv[1])
