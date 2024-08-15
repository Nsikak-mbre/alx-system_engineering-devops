#!/usr/bin/python3
"""
Querries the redit API.
"""
import requests


def top_ten(subreddit):
    """
    Returns the 10 hot posts from reddit api querries.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': '1-top_ten/top_ten_posts'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            for post in posts:
                print(post['data']['title'])
            else:
                print(None)
    except requests.RequestException:
        print(None)
