#python programme for VPC lists
import boto3
import json
client = boto3.client('ec2')
aws_access_key_id="AKIAXZS5FWNSM7VYCZRU"
aws_secret_access_key="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"
vpcs = client.describe_vpcs()
print(vpcs)

