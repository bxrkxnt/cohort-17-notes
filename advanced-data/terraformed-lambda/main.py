"""A small Lambda example."""

def handler(event=None, context=None) -> str:
    """Returns text."""

    return "All happy families are alike; each unhappy family is unhappy in their own way."

if __name__ == "__main__":

    print(handler())