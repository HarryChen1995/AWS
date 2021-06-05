import boto3
from pprint import pprint

iam = boto3.client("iam")
response = iam.list_policies()
Arn = response['Policies'][0]['Arn']
iam.delete_policy(
        PolicyArn = Arn,
)
