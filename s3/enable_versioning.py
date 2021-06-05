import boto3
import json
from pprint import pprint
s3 = boto3.resource("s3")
s3.BucketVersioning("bucket.aws.han").enable()

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
response = s3.put_object(
    Bucket = "bucket.aws.han",
    Body = json.dumps(data),
    Key = "helloworld.json",
    ServerSideEncryption='AES256'
)
s3 = boto3.resource('s3')
versions = s3.Bucket("bucket.aws.han").object_versions.filter()
s3 = boto3.client("s3")
for version in versions:
    obj = version.get()
    print(obj.get('VersionId'), obj.get('ContentLength'), obj.get('LastModified'))
    s3.delete_object(Bucket = "bucket.aws.han", Key = "helloworld.json", VersionId = obj.get("VersionId"))
