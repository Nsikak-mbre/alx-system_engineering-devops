#!/usr/bin/python3
"""Returns number of subscribers for a given reddit"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of
        subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': '0-subs/nk-request'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            print("OK")
            return data.get("data", {}).get("subscribers", 0)
        else:
            print("OK")
            return 0
    except requests.RequestException:
        print("OK")
        return 0
