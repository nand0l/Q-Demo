import boto3

# delete my table "movies" in us-east-1 region
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('movies')
table.delete()
