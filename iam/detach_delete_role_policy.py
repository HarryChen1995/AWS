import boto3
from pprint import pprint

iam = boto3.client("iam")
response = iam.list_policies()
Arn = response['Policies'][0]['Arn']
iam.detach_role_policy(
    PolicyArn = Arn,
    RoleName = "my_s3_role"
)
iam.delete_role(
    RoleName = "my_s3_role"
)
