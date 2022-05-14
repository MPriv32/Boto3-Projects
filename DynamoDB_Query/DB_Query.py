import boto3, json
from boto3.dynamodb.conditions import Key


#Calling DynamoDB module and assigning the table name
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('stock_tracker')

#Querying the primary key of the table
resp = table.query(KeyConditionExpression=Key('Company').eq('AAPL'))

#Assigning the item count and total price to a variable in order to find the average daily price
numItems = resp['Count']
total_price = 0

for item in resp['Items']:
    # print(json.dumps(item, indent=4, sort_keys=True))
    price_per_day = float(item['DailyPrice'])
    total_price += price_per_day

average_price = total_price / numItems

print(format(average_price, '.2f'))