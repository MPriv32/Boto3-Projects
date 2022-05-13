import boto3

def create_presigned_url(bucket_name, object_name, expiration=86400):

    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3')

    response = s3_client.generate_presigned_url(
        'get_object',
        Params={'Bucket': "weather-update-project-bucket",
                'Key': "app.py"},
        ExpiresIn=expiration)

    # The response contains the presigned URL
    return response

print(create_presigned_url("weather-update-project-bucket", "app.py", expiration=86400))