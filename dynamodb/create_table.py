import boto3
import botocore
dynamodb = boto3.resource("dynamodb")
try:
    table  = dynamodb.Table("Movies")
    print(table.table_status)
except botocore.exceptions.ClientError:
    dynamodb.create_table(
        TableName = "Movies",
        KeySchema = [
            {"AttributeName": 'year', "KeyType":"HASH"},
            {"AttributeName": 'title', "KeyType":"RANGE"}
        ],
        AttributeDefinitions = [
            {"AttributeName":"year", "AttributeType":"N"},
            {"AttributeName":"title", "AttributeType":"S"}
         ],
        ProvisionedThroughput = {
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits":5
     })





