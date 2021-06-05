import boto3
from pprint import pprint
iam = boto3.client("iam")
response = iam.list_policies()
Arn = response['Policies'][0]['Arn']
response = iam.get_policy(PolicyArn = Arn)
pprint(response['Policy'])
