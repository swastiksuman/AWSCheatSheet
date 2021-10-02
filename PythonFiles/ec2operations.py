import boto3

ec2 = boto3.resource('ec2', region_name="us-east-1")
tags = [
   {
       'Key':'environment',
       'Value':'personal'
   },
]
instances = ec2.create_instances(ImageId='ami-087c17d1fe0178315',
     MinCount=1,
     MaxCount=1,
     InstanceType='t2.micro',
     KeyName='my-ubuntu',
     TagSpecifications=[
        {'ResourceType': 'instance', 'Tags':tags},
     ]
)

print(instances)
