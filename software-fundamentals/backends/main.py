"""An API for company data."""

import json
from random import choice

from flask import Flask, abort, request

api = Flask(__name__)  # Create an instance of a server/API

@api.get("/")  # Use this function when someone hits the / route with a GET
def index():
    return "Welcome to the Companies API."


@api.route("/company", methods=["GET"])
def company_index():
    """Returns data on all companies."""
    parameters = request.args

    if "country" in parameters:
        # return just those matching the country
        # matched_companies = []
        # for company in companies:
        #     if company["country"] == parameters["country"]:
        #         matched_companies.append(company)
        # return matched_companies
        # return [c for c in companies if c["country"] == parameters["country"]]
        return list(filter(lambda x: x["country"] == parameters["country"], companies))
    else:
        return companies


@api.route("/company/<int:id>", methods=["GET"])
def company_show(id: int):
    """Returns data on a single company."""
    for c in companies:
        if c["id"] == id:
            return c
    # return abort(404)  # Standard error message
    return f"Unable to find a company with ID {id}", 404 # Custom


@api.get("/company/random")
def company_random():
    """Returns a random company's details."""
    return choice(companies)   

if __name__ == "__main__":

    with open("companies.json", "r", encoding="utf-8") as f:
        companies = json.load(f)

    api.run(port=8080, debug=True)  # Actually set it listening
