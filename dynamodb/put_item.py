import json
import boto3
import random
from decimal import Decimal
with open("moviedata.json", "r") as file:
    data = json.load(file, parse_float =Decimal )
    file.close()

# read only first 500 entry data
random.shuffle(data)
data = data[:100]
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Movies")
for movie in data:
    table.put_item(Item = movie)

