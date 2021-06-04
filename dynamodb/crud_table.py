import boto3
from  pprint import pprint
from decimal import Decimal
from botocore.exceptions import ClientError
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Movies")

# adding new item
response = table.put_item(
    Item = {
        'year': 2015,
        'title':"The Big New Movie",
        "info":{
            "plot":"Nothing happens at all.",
            "rating":0
        }
    }
)

print(response)
#get item
try:
    response = table.get_item(Key = {"year":2015, "title":"The Big New Movie"})
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    pprint(response['Item'], sort_dicts = False )


# update item
response = table.update_item(
    Key = {
        "year": 2015,
        "title": "The Big New Movie"
    },
    UpdateExpression = "set info.rating=:r, info.plot=:p, info.actors=:a",
    ExpressionAttributeValues = {
        ":r": Decimal(5.5),
        ":p": "Everything happens all at once.",
        ":a":  ["Larry", "Moe", "Curly"]
    },
    ReturnValues = "UPDATED_NEW"
)

pprint(response, sort_dicts = False)

# increment an Atomic Counter

response = table.update_item (
    Key = {
        "year": 2015,
        "title": "The Big New Movie"
    },
    UpdateExpression = "set info.rating = info.rating + :val",
    ExpressionAttributeValues = {
        ":val": Decimal(1)
    },
    ReturnValues = "UPDATED_NEW"
)

pprint(response, sort_dicts = False)

#update an item conditionally
try:
    response = table.update_item(
        Key = {
        "year":2015,
        "title":"The Big New Movie"
        },
        UpdateExpression = "remove info.actors[0]",
        ConditionExpression = "size(info.actors) >= :num",
        ExpressionAttributeValues = {
            ":num": 3
        },
        ReturnValues = "UPDATED_NEW"
    )
except ClientError as e:
    if e.response['Error']['Code'] == "ConditionalCheckFailedException":
            print(e.response['Error']['Message'])
    else:
        raise
else:
    pprint(response, sort_dicts = False)
#delete item
response = table.delete_item(
    Key = {
        "year":2015,
        "title":"The Big New Movie"
    }
)
pprint(response, sort_dicts = False)
