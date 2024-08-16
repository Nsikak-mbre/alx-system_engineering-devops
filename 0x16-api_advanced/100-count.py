#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and counts
given keywords in the titles of hot articles.
"""
import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """
    Recursively queries the Reddit API, parses the titles of hot articles,
    and counts the occurrences of specified keywords.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of keywords to count in the titles.
        word_count (dict): A dictionary to store the count of keywords.
        after (str): The pagination token for the next set of results.

    Returns:
        None: The function prints the result and returns None.
    """
    # Normalize word_list to lowercase
    word_list = [word.lower() for word in word_list]

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'wordcount/1.0'}
    params = {'after': after, 'limit': 100}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            articles = data.get('data', {}).get('children', [])
            after = data.get('data', {}).get('after', None)

            for article in articles:
                title = article['data']['title'].lower().split()
                for word in word_list:
                    word_count[word] = word_count.get(
                        word, 0) + title.count(word)

            if after is not None:
                return count_words(subreddit, word_list, word_count, after)
            else:
                if word_count:
                    sorted_counts = sorted(
                        word_count.items(), key=lambda x: (-x[1], x[0]))
                    for word, count in sorted_counts:
                        if count > 0:
                            print(f"{word}: {count}")
        else:
            return None
    except requests.RequestException:
        return None
