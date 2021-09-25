import boto3

ec2 = boto3.resource('ec2', region_name="us-east-1")
for instance in ec2.instances.all():
    print("ID: {0}\nPlatform: {1}\nPublic IPv4: {2}\nState: {3}".format(instance.id, instance.platform, instance.public_ip_address, instance.state))
