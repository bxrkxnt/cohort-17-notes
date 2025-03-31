"""A CLI tool for searching anime."""

from pprint import pp
from argparse import ArgumentParser, Namespace

import requests as req


db = {
    "user": {
        "name": "My name",
        "API_KEY": "aldsjkfhasdfhiuhl235qfdg0sv-cxz-vz-cxwefj",
        "usage": {
            "number of calls": 455,
            "call_log": [{"call_1": {"response": "404 not found", "at": "May"}}],
        },
    }
}

BASE_URL = "https://api.jikan.moe/v4/anime?"
TIMEOUT = 5000
DEFAULT_RESULTS = 5
NO_MATCHING_ANIME_MSG = "No matching anime found."
NETWORK_ERROR_MSG = "Network error occurred: "
JSON_ERROR_MSG = "Error parsing JSON response: "
UNEXPECTED_ERROR_MSG = "An unexpected error occurred: "


def generate_url(query: str, max_results: int, include_nsfw: bool) -> str:
    """Returns a formatted URL based on CLI arguments."""

    url = (
        BASE_URL
        + f"&limit={max_results}&q={query}"
        + ("&sfw" if not include_nsfw else "")
    )
    return url


def display_anime_data(anime_data: dict):
    """Displays key details about an anime from a dict."""
    title = anime_data["titles"][0]["title"]
    score = anime_data["score"]
    scored_by = anime_data["scored_by"]
    rating = anime_data["rating"].split(" - ")[0]

    print(f"{title} ({rating}) ~ {score}/10 ({scored_by})")


def display_results(results: list[dict]) -> None:
    """Displays each anime result in sequence."""

    for r in results:
        display_anime_data(r)


def get_anime_data(url: str) -> list[dict]:
    response = req.get(url)
    if response.status_code == 200:
        shows = response.json().get("data", [])
        return [show for show in shows if show.get("rating") and show.get("score")]


def collect_arguments() -> Namespace:
    """Returns parsed arguments from the command line."""
    description = "Returns the name and rating of anime for a given search term."
    parser = ArgumentParser(description=description)
    parser.add_argument(
        "--number",
        "-n",
        default=DEFAULT_RESULTS,
        type=int,
        help="the number of results to return",
    )
    parser.add_argument("--nsfw", action="store_true", help="include NSFW shows")
    parser.add_argument("query", help="the query to search for")
    return parser.parse_args()


if __name__ == "__main__":
    # Users can search for relevant anime by providing a query argument
    # Users can pass an argument to control the number of results returned (default 5)
    # Users can use a flag to include adult content in the results (default to not including it)

    args = collect_arguments()
    search_url = generate_url(args.query, args.number, args.nsfw)
    anime_data = get_anime_data(search_url)
    if anime_data:
        display_results(anime_data)

    # response = {}
    # for key in response.keys():
    #     pp(key, response[key])
