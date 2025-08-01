import boto3
import json
import random

# create an s3-bucket with a random-name in us-west-1 make sure the bucketname is lowercase
s3 = boto3.client('s3', region_name='us-west-1')
bucket_name = 'XXXXXXXXXX' + str(random.randint(100000, 999999))
s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'XXXXXXXXX'})
print('Bucket created: ' + bucket_name)
