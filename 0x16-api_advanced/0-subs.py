#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    try:
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        headers = {
            "User-Agent": "Mozilla/10.0/API"
        }
        response = requests.get(url, headers=headers, allow_redirects=False, verify=False)
        if response.status_code == 404:
            return 0

        print(response.status_code)
        results = response.json().get("data")
        return results.get("subscribers")
              
    except requests.exceptions as e:
        print(e)

