# API advanced

These Python scripts query Reddit's public JSON API. Each request supplies a
custom User-Agent and disables redirects so invalid subreddit names are not
mistaken for search-result pages.

## Requirements

- Python 3
- `requests`
- Network access to `https://www.reddit.com`

## Usage

```sh
python3 0-main.py programming
python3 1-main.py programming
python3 2-main.py programming
python3 3-main.py programming "python java javascript"
```

The `0-main.py` through `3-main.py` files shown in the assignment are test
drivers; the implementations in this project are `0-subs.py`, `1-top_ten.py`,
`2-recurse.py`, and `3-count.py`.
