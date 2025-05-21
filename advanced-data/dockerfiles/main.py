"""A very basic Python file."""

from os import environ as ENV

from requests import get
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    print(ENV["SECRET"])