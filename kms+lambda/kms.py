import boto3
import json

client = boto3.client('kms')

response = client.create_key(
    Description='string',
    Tags=[
        {
            'TagKey': 'Key_name',
            'TagValue': 'boto3'
        },
    ]
)

class key_arn():
    meta_data = response.get("KeyMetadata")
    arn = meta_data['Arn']

print(response)