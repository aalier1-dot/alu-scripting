#!/usr/bin/python3
"""Print the titles of a subreddit's ten hottest posts."""

import requests


BASE_URL = "https://www.reddit.com"
HEADERS = {
    "User-Agent": "My-User-Agent"
}


def top_ten(subreddit):
    """Print up to ten hot-post titles, or None if the subreddit is invalid."""
    url = "{}/r/{}/hot.json".format(BASE_URL, subreddit)
    response = requests.get(
        url,
        headers=HEADERS,
        allow_redirects=False,
    )
    if response.status_code != 200:
        print(None)
        return

    data = response.json().get("data")
    if not isinstance(data, dict):
        print(None)
        return
    children = data.get("children")
    if not children:
        print(None)
        return

    for post in children[:10]:
        title = post.get("data", {}).get("title")
        if title is not None:
            print(title)
