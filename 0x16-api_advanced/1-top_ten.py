#!/usr/bin/python3
"""a module to import"""
import requests
import sys


def top_ten(subreddit):
    """module to send a requests"""
    headers = {'User-Agent': 'MyBot/1.0'}
    red_api = requests.get(
            f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10",
            headers=headers,
            allow_redirects=False
            )
    if red_api.status_code == 200:
        data = red_api.json()
        for post in data.get("data").get("children"):
            print(post.get("data").get("title"))
    elif red_api.status_code == 404:
        print(None)


if __name__ == "__main__":
    top_ten(sys.argv[1])
