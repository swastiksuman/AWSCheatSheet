import boto3
import os

try:

    s3 = boto3.client('s3', aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID'), aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY'))
    response = s3.list_objects(Bucket="swastik-personal-bucket")
    print(os.environ.get('AWS_ACCESS_KEY_ID') + ' ' + os.environ.get('AWS_SECRET_ACCESS_KEY'))
    for content in response.get('Contents', []):
        print(content.get('Key'))

except Exception as e:
    print(e)
    print("error")
