import boto3
from pprint import pprint
s3 = boto3.client("s3")
response = s3.list_buckets()
pprint(response)
