#!/usr/bin/python3
"""Recursively count requested words in a subreddit's hot-post titles."""

import requests


BASE_URL = "https://www.reddit.com"
HEADERS = {
    "User-Agent": "alu-scripting-api-advanced/1.0 (educational project)"
}


def count_words(subreddit, word_list, after=None, counts=None):
    """Print keyword occurrence counts in hot-post titles, sorted by count."""
    if counts is None:
        counts = {}
        for word in word_list:
            normalized = word.lower()
            if normalized not in counts:
                counts[normalized] = [0, 0]
            counts[normalized][1] += 1

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
        return

    data = response.json().get("data")
    if not isinstance(data, dict):
        return

    for post in data.get("children", []):
        title = post.get("data", {}).get("title", "")
        for token in title.lower().split():
            if token in counts:
                counts[token][0] += counts[token][1]

    next_after = data.get("after")
    if next_after:
        count_words(subreddit, word_list, next_after, counts)
        return

    results = [
        (word, values[0])
        for word, values in counts.items()
        if values[0]
    ]
    results.sort(key=lambda item: (-item[1], item[0]))
    for word, count in results:
        print("{}: {}".format(word, count))
