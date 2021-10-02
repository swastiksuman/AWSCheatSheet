import boto3

ec2 = boto3.resource('ec2', region_name="us-east-1")
for instance in ec2.instances.all():
    for tag in instance.tags:
        if 'environment' in tag['Key']:
            if tag['Value'] == 'personal':
                print(instance.public_ip_address)
