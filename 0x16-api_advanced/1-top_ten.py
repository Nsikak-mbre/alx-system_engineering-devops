#!/usr/bin/python3
"""
Queries the Reddit API.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the 10 hot posts from a Reddit API query.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': '1-top_ten/top_ten_posts'}

    try:
        # Make GET request to Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the response was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            
            # Check if there are any posts
            if posts:
                # Print the titles of the posts
                for post in posts:
                    print(post['data']['title'])
            else:
                print(None)
        else:
            # If subreddit is invalid or doesn't exist
            print(None)
    except requests.RequestException:
        # In case of a request failure
        print(None)
