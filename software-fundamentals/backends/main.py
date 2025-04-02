"""An API for company data."""

import json
from random import choice

from flask import Flask, abort, request

api = Flask(__name__)  # Create an instance of a server/API

@api.get("/")  # Use this function when someone hits the / route with a GET
def index():
    return "Welcome to the Companies API."


@api.route("/company", methods=["GET", "POST"])
def company_index():
    """Returns data on all companies."""
    parameters = request.args

    if request.method == "GET":

        if "country" in parameters:
            return [c for c in companies if c["country"] == parameters["country"]]
        else:
            return companies

    if request.method == "POST":
        new_company = request.json
        if not is_valid_company(new_company):
            return {"error": True, "message": "Not a valid company"}, 400
        
        company_id = get_next_id(companies)

        new_company["id"] = company_id

        companies.append(new_company)

        return new_company, 201


def is_valid_company(company: dict) -> bool:
    """Returns True if a dict has all required keys."""
    return all(key.lower() in company for key in ["name", "country"])


def get_next_id(companies: list[dict]) -> int:
    """Returns the next valid company ID."""
    return max(company.get("id") for company in companies) + 1


@api.route("/company/<int:id>", methods=["GET", "DELETE"])
def company_show(id: int):
    """Returns data on a single company or deletes a company."""
    if request.method == "GET":
        for c in companies:
            if c["id"] == id:
                return c
        return {"error": True, "message": f"Unable to find a company with ID {id}"}, 404
    else:
        companies = [c for c in companies if c["id"] != id]
        return { "success": True }


@api.get("/company/random")
def company_random():
    """Returns a random company's details."""
    return choice(companies)


if __name__ == "__main__":

    with open("companies.json", "r", encoding="utf-8") as f:
        companies = json.load(f)

    api.run(port=8080, debug=True)  # Actually set it listening
