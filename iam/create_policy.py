import boto3
import json
from pprint import pprint
managed_s3_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
                  "Action": "s3:*",
                  "Effect": "Allow",
                  "Resource": "*"
        }

    ]
}


iam = boto3.client("iam")
response = iam.create_policy(
    PolicyName = "my_s3_policy",
    PolicyDocument = json.dumps(managed_s3_policy)
)

pprint(response)
