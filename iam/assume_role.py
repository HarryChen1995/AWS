import boto3
from pprint import pprint

sts = boto3.client("sts")
iam = boto3.client("iam")
arn = iam.get_role(RoleName = "my_s3_role")['Role']['Arn']
assumed_role = sts.assume_role(
    RoleArn = arn,
    RoleSessionName = "AssumeRoleSession1"
)

credentials=assumed_role['Credentials']

s3_resource=boto3.resource(
        's3',
        aws_access_key_id=credentials['AccessKeyId'],
        aws_secret_access_key=credentials['SecretAccessKey'],
        aws_session_token=credentials['SessionToken'],

)

for bucket in s3_resource.buckets.all():
        print(bucket.name)
