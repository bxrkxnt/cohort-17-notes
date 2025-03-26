"""Functions that interact with the <BLANK> API."""

import requests as req
import http

def get_user_repo_count(username: str) -> int:
    """Returns the number of public repos a user has."""
    
    if not isinstance(username, str):
        raise TypeError("Function expects a string.")

    res = req.get(f"https://api.github.com/users/{username}")

    if res.status_code >= 500:
        raise Exception("Unable to contact API!")
    elif res.status_code == http.HTTPStatus(404):
        raise ValueError("No such user.")

    data = res.json()

    return data["public_repos"]


if __name__ == "__main__":
    
    print(get_user_repo_count("zertikyle"))
