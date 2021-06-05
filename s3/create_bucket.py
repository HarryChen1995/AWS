import boto3
from pprint import pprint
from botocore.exceptions import ClientError
import uuid
try:
    s3 = boto3.client("s3")
    location = {"LocationConstraint":"us-east-2"}
    response = s3.create_bucket(Bucket = "bucket.aws.han", CreateBucketConfiguration = location)
    pprint(response)
except ClientError as e:
    print(e["Error"]["Message"])

