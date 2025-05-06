"""A small example of accessing S3 buckets using Python."""

from os import environ as ENV, _Environ

from dotenv import load_dotenv
from boto3 import client


def get_bucket_names(s3_client: client) -> list[str]:
    """Returns a list of S3 bucket names."""
    buckets = s3_client.list_buckets()["Buckets"]

    return [b["Name"] for b in buckets]


def get_object_names_from_bucket(s3_client: client, bucket_name: str) -> list[str]:
    """Returns a list of all object names in a given bucket."""

    objects = s3_client.list_objects(Bucket=bucket_name)["Contents"]

    return [o["Key"] for o in objects]


if __name__ == "__main__":

    load_dotenv()  # Reads variables from .env into the environment

    s3 = client("s3", aws_access_key_id=ENV["AWS_ACCESS_KEY_ID"],
                aws_secret_access_key=ENV["AWS_SECRET_ACCESS_KEY"])

    objects = get_object_names_from_bucket(s3, ENV["S3_BUCKET_NAME"])

    for o in objects:
        s3.download_file(ENV["S3_BUCKET_NAME"], o, f"data/{o}")

    s3.close()