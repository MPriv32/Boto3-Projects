import boto3
import kms

#Function creation variables
kms_key_arn = kms.key_arn.arn

client = boto3.client('lambda')

response = client.create_function(
    Code={
        'S3Bucket': 'weather-update-project-bucket',
        'S3Key': 'app.zip',
    },
    Description='Sends an email with a weather update',
    Environment={
        'Variables': {
            'BUCKET': 'weather-update-project-bucket',
            'PREFIX': 'inbound',
            'EMAIL_USER': '<insert email address>',
            'EMAIL_PASSWORD': '<insert gmail api key>',
            'WEATHER_API_KEY': '<insert weather api key>',
        },
    },
    FunctionName='weather-function',
    Handler='app.handler',
    KMSKeyArn=f'{kms_key_arn}',
    MemorySize=256,
    Publish=True,
    Role='<insert IAM role for lambda>',
    Runtime='python3.7',
    Tags={
        'Environment': 'Dev',
    },
    Timeout=15,
    TracingConfig={
        'Mode': 'Active',
    },
)

print(response)