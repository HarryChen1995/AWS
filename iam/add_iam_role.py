import boto3
from pprint import pprint
import json
trust_relationship_policy = {
      "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": { "AWS": "arn:aws:iam::##############:user/####"  },
            "Action": "sts:AssumeRole",
        }

    ]

}

iam = boto3.client("iam")
iam.create_role(
    RoleName = "my_s3_role",
    AssumeRolePolicyDocument = json.dumps(trust_relationship_policy)
)
response = iam.list_policies()
Arn = response['Policies'][0]['Arn']
response = iam.attach_role_policy(
    RoleName = "my_s3_role",
    PolicyArn = Arn
)
pprint(response)

