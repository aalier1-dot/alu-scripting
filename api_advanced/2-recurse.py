#!/usr/bin/python3
"""Recursively retrieve hot-post titles from a subreddit."""

import requests


BASE_URL = "https://www.reddit.com"
HEADERS = {
    "User-Agent": "alu-scripting-api-advanced/1.0 (educational project)"
}


def recurse(subreddit, hot_list=None, after=None):
    """Return all available hot-post titles using Reddit listing pagination."""
    if hot_list is None:
        hot_list = []

    url = "{}/r/{}/hot.json".format(
        BASE_URL, requests.utils.quote(subreddit, safe="")
    )
    params = {"limit": 100}
    if after is not None:
        params["after"] = after

    response = requests.get(
        url,
        headers=HEADERS,
        params=params,
        allow_redirects=False,
        timeout=10,
    )
    if response.status_code != 200:
        return None

    data = response.json().get("data")
    if not isinstance(data, dict):
        return None

    for post in data.get("children", []):
        title = post.get("data", {}).get("title")
        if title is not None:
            hot_list.append(title)

    next_after = data.get("after")
    if next_after:
        return recurse(subreddit, hot_list, next_after)
    if hot_list:
        return hot_list
    return None
