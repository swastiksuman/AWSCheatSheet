# AWS Cheatsheet

## Deploying CFTs
- aws cloudformation deploy --template-file aws-ec2-security-group-with-storage.yml --stack-name MyCFT12DecTest
- aws cloudformation delete-stack --stack-name MyCFT12DecTest
- aws cloudformation deploy --template aws-serverless-amplify-react-webapp.yaml --stack-name MyAmplify13Sep --parameter-overrides Repository=https://github.com/swastiksuman/AWSCheatSheet OauthToken=<OAUTHTOKEN>

## S3 Operations
- aws s3 ls
- aws s3 cp response.json s3://swastik-personal-bucket/response.json
- aws s3 cp s3://swastik-personal-bucket/response.json .
- aws s3 sync . s3://swastik-personal-bucket/

## Amplify
- aws amplify list-apps
- aws amplify start-job --app-id dgh57ty0q1ndf --branch-name master --job-type RELEASE

## EKS
- aws eks update-kubeconfig --name MyEKSCluster
- kubectl get svc  
- kubectl apply -f https://docs.projectcalico.org/v3.14/manifests/calico.yaml
- kubectl get pods -n kube-system -o wide
- kubectl apply -f client-pod.yaml
- docker exec -it container_id /bin/bash
