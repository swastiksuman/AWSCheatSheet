import boto3

cf = boto3.client('cloudformation')
with open('../aws-s3-simple.yaml') as file:
    template = file.read()
print(template)
response = cf.create_stack(StackName='MyStack20210925', TemplateBody=template)
print(response)
