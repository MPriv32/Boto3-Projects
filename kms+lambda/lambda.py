import boto3
import kms
import os

if os.path.isfile('.env'):
    from dotenv import load_dotenv
    load_dotenv()

#Function creation variables
bucket_name = os.getenv('bucket_name')
bucket_arn = os.getenv('bucket_arn')
file_path = os.getenv('file_path')
handler = "app.handler"
kms_key_arn = 
runtime = ""

#Lambda Environment Variables
email_user = os.getenv('email_user')
email_password = os.getenv('email_password')

client = boto3.client('lambda')

response = client.create_function(
    Code={
        'S3Bucket': f'{bucket_name}',
        'S3Key': f'{file_path}',
    },
    Description='Sends an email with a weather update',
    Environment={
        'Variables': {
            'BUCKET': f'{bucket_name}',
            'PREFIX': 'inbound',
            'EMAIL_USER': f'{email_user}',
            'EMAIL_PASSWORD': f'{email_password}',
        },
    },
    FunctionName='weather-function',
    Handler=f'{handler}',
    KMSKeyArn=f'{kms_key_arn}',
    MemorySize=256,
    Publish=True,
    Role='arn:aws:iam::123456789012:role/lambda-role',
    Runtime=f'{runtime}',
    Tags={
        'Environment': 'Dev',
    },
    Timeout=15,
    TracingConfig={
        'Mode': 'Active',
    },
)

print(response)