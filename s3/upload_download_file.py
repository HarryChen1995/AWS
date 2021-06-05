import boto3
from pprint import pprint
s3 = boto3.client("s3")
s3.upload_file("helloworld.txt", "bucket.aws.han", "helloworld.txt")
# use upload_fileobj for readable file like object

s3.download_file("bucket.aws.han", "helloworld.txt",  "test.txt")
#user download_fileob to write file like object

