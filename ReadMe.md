# AWS Cheatsheet

## Deploying CFTs
- aws cloudformation deploy --template-file aws-ec2-security-group-with-storage.yml --stack-name MyCFT12DecTest
- aws cloudformation delete-stack --stack-name MyCFT12DecTest

## S3 Operations
aws s3 ls
aws s3 cp response.json s3://swastik-personal-bucket/response.json
aws s3 cp s3://swastik-personal-bucket/response.json .
aws s3 sync . s3://swastik-personal-bucket/
