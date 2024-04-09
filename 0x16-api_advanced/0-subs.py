#!/usr/bin/python3
'''
    contains the function number_of_subscribers
'''
import requests
import sys


def number_of_subscribers(subreddit):
    '''
        returns the number of subscribers for a given subreddit
    '''
    headers = {'User-Agent': 'Lizzie'}
    url = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit), headers=headers).json()
    try:
        return url.get('data').get('subscribers')
    except Exception:
        return 0


if __name__ == "__main__":
    number_of_subscribers(sys.argv[1])
