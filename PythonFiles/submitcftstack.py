import boto3
import sys

cf = boto3.client('cloudformation')
with open('../aws-s3-simple.yaml') as file:
    template = file.read()
print(template)
print("Creating New Stack: "+sys.argv[1]+ " Bucket Name: "+ sys.argv[2])
response = cf.create_stack(StackName=sys.argv[1], TemplateBody=template, Parameters=[{"ParameterKey":"BucketNameParam", "ParameterValue": sys.argv[2]}])
print(response)
