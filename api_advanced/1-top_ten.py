#!/usr/bin/python3
"""Print the titles of a subreddit's ten hottest posts."""

import requests


BASE_URL = "https://www.reddit.com"
HEADERS = {
    "User-Agent": "python:alu-scripting:1.0 (by /u/aalier1-dot)"
}


def top_ten(subreddit):
    """Print up to ten hot-post titles, or None if the subreddit is invalid."""
    url = "{}/r/{}/hot.json?limit=10".format(BASE_URL, subreddit)
    response = requests.get(
        url,
        headers=HEADERS,
        allow_redirects=False,
    )
    if response.status_code != 200:
        print(None)
        return

    try:
        payload = response.json()
    except ValueError:
        print(None)
        return

    if not isinstance(payload, dict):
        print(None)
        return
    data = payload.get("data")
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
