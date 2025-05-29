"""A small Lambda example."""

from dotenv import load_dotenv
from boto3 import Session
import awswrangler as wr

def handler(event=None, context=None) -> bool:
    """Returns text."""

    aws_session = Session(region_name="eu-west-2")

    # Can we talk to S3?
    print(" | ".join(wr.s3.list_buckets(boto3_session=aws_session)[:3]))

    # Can we talk to Athena?
    df = wr.athena.read_sql_query(sql="SELECT * FROM truck;", database="c17-james-truck-db", boto3_session=aws_session,
                                  s3_output="s3://c17-james-trucks/output")

    print(df.head())

    return True

if __name__ == "__main__":

    print(handler())