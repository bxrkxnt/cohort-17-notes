import requests as req

BASE_URL = "https://sigma-micro-blogging.herokuapp.com/"

def update_message(username: str, new_message: str, message_id: str) -> None:
    """Updates a message with new content."""
    url = f"{BASE_URL}{username}/{message_id}"
    body = {
        "message": new_message,
        "from": username
    }

    res = req.patch(url, json=body)

    if res.status_code != 200:
        raise Exception("Posting Failed!")
    
    print(res.content)


def post_message(username: str, message: str) -> None:
    """Posts a message to the microblog."""

    url = f"{BASE_URL}{username}"
    body = {
        "message": message,
        "from": username
    }

    res = req.post(url, json=body)

    if res.status_code != 200:
        raise Exception("Posting Failed!")


if __name__ == "__main__":
    update_message("marios", "CHANGES", "6ff0c084-1d94-424e-b96f-ff635a0df0b6")