import boto3

try:

    s3 = boto3.client('s3', aws_access_key_id = '', aws_secret_access_key = '')
    bucket = s3.get_bucket('swastik-personal-bucket')
    print(bucket.get_available_subresources())

except Exception,e:
    print str(e)
    print "error"
