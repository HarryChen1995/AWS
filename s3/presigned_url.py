import boto3
import requests

s3 = boto3.client('s3')
url = s3.generate_presigned_url(
    ClientMethod='get_object',
    Params={
        'Bucket': 'bucket.aws.han',
        'Key': 'helloworld.txt'
    }
)
print(url)

