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

    if request.method == "POST":
        new_company = json.loads(request.data)
        if not is_valid_company(new_company):
            return {"Error": True, "message": "Not a valid company"}, 400
        company_id = max(company.get("id") for company in companies) + 1
        company_to_add = {"id": company_id}
        company_to_add["name"] = new_company.get("name")
        company_to_add["country"] = new_company.get("country")
        company_to_add["domain"] = new_company.get("domain")
        company_to_add["stock"] = new_company.get("stock")
        company_to_add["email"] = new_company.get("email")
        companies.append(company_to_add)
        return company_to_add, 201

def is_valid_company(company: dict) -> bool:
    return all(key.lower() in company for key in ["name", "country"])

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

"""
Write an endpoint that will let the user delete a company. 
The data is of type list.

For example, the query:

http://127.0.0.1:5000/companies/212

should delete the company with the id equal to 212
"""
...

if __name__ == "__main__":

    with open("companies.json", "r", encoding="utf-8") as f:
        companies = json.load(f)

    api.run(port=8080, debug=True)  # Actually set it listening
