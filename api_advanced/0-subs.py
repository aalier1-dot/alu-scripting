#!/usr/bin/python3
"""Return the subscriber count for a subreddit."""

import requests


BASE_URL = "https://www.reddit.com"
HEADERS = {
    "User-Agent": "alu-scripting-api-advanced/1.0 (educational project)"
}


def number_of_subscribers(subreddit):
    """Return a subreddit's subscriber count, or 0 if it does not exist."""
    url = "{}/r/{}/about.json".format(
        BASE_URL, requests.utils.quote(subreddit, safe="")
    )
    response = requests.get(
        url, headers=HEADERS, allow_redirects=False, timeout=10
    )
    if response.status_code != 200:
        return 0

    data = response.json().get("data")
    if not isinstance(data, dict):
        return 0
    return data.get("subscribers", 0)
