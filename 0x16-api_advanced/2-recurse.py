#!/usr/bin/python3
"""
Recursive function that querries a reddit API
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive queires the Reddit API and returns hot articles for a
    given subreddit. returns None if no results are found

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): A list to store the titles of hot articles.
        after (str): The pagination token for the next set of results.

        Returns:
            List: A list containing the titles of all hot articles, or
            None if the subreddit is invalid or has no hot articles.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': '2-recurse/titles'}
    params = {'after': after, 'limit': 100}
    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            articles = data.get('data', {}).get('children', [])
            after = data.get('data', {}).get('after', None)

            for article in articles:
                hot_list.append(article['data']['title'])
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None
