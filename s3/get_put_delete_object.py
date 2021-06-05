import boto3
import json
from pprint import pprint

data = {
    "content": "hellworld"
}
s3 = boto3.client("s3")
response = s3.put_object(
    Bucket = "bucket.aws.han",
    Body = json.dumps(data),
    Key = "helloworld.json",
    ServerSideEncryption='AES256'
)
pprint(response)

response = s3.get_object(Bucket = "bucket.aws.han", Key = "helloworld.json")
print(json.loads(response['Body'].read()))

response = s3.delete_object(Bucket = "bucket.aws.han", Key = "helloworld.json")
pprint(response)
