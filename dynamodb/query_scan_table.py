from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Movies")
response = table.query(
    KeyConditionExpression = Key("year").eq(1992)

)
print(response['Items'])

response = table.query(
    ProjectionExpression = "#yr, title, info.genres, info.actors[0]",
    ExpressionAttributeNames = {"#yr": "year"},
    KeyConditionExpression = Key("year").eq(1992) & Key("title").between('A', 'L')
)
print(response['Items'])

response = table.scan(
    ProjectionExpression = "#yr, title, info.genres, info.actors[0]",
    ExpressionAttributeNames = {"#yr": "year"},
    FilterExpression = Key("year").between(1950, 1959)
)


print(response['Items'])


