import boto3, json
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('stock_tracker')

resp = table.query(KeyConditionExpression=Key('Company').eq('AAPL'))

print("The query returned the following items:")
for item in resp['Items']:
    print(json.dumps(item, indent=4, sort_keys=True))