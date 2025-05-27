"""Lambda function example"""

from unittest.mock import MagicMock
import awswrangler as wr
import pandas as pd
from boto3 import Session
from dotenv import load_dotenv
from os import environ as ENV


def pandler(event=None, context=None) -> tuple:
    """Handler for the lambda function"""
    load_dotenv()
    boto_session = Session(aws_access_key_id=ENV["ACCESS_KEY"], 
                                  aws_secret_access_key=ENV["SECRET_ACCESS_KEY"], 
                                  region_name="eu-west-2")
    return {
        "status code": 200,
        "body": wr.athena.read_sql_query("SELECT * FROM trucks", database="ruy-pipeline-2", boto3_session=boto_session).to_json(orient="records")
    }


if __name__ == "__main__":
    fake_context = MagicMock()
    fake_context.get_remaining_time_in_millis.return_value = 8000000
    print(handler({"name": "Pigcasso"}, fake_context))