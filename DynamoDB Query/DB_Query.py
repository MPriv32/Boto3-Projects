import boto3

client = boto3.client('dynamodb')

response = client.query(
    ExpressionAttributeValues={
        ':GME': {
            'S': 'GME',
        },
    },
    KeyConditionExpression='Company = :GME',
    TableName='stock_tracker',
)
number_of_days = response['Count']


print(number_of_days)