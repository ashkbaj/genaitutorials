import boto3
import os

#AWS Credentials:
CanonicalID = '92dd321c06c5c00d42f3de50af16fdd4b9073bc3171a56844cc12b20b54b9c36'
email='ashishbajpai.jobs@gmail.com'
awsaccountid ='336746913723'
accountname='brohmo'
arn="arn:aws:iam::336746913723:user/ashishbaj"
accesskey='AKIAU4Z5OD65SIW34CNY'
secretaccesskey='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'


os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAU4Z5OD65SIW34CNY'
os.environ['AWS_SECRET_ACCESS_KEY'] = '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'
region='ap-south-1'
dynamodb = boto3.resource('dynamodb', region_name=region)



try:
    response = dynamodb.describe_table(TableName='students')
except dynamodb.exceptions.ResourceNotFoundException:
    # do something here as you require
    print("Table does not exist.")
    pass



try:
    table = dynamodb.create_table(
        TableName = 'students',
        KeySchema = [
            {
                'AttributeName' : 'name',
                'KeyType' : 'HASH'
            },
            {
                'AttributeName' : 'lastname',
                'KeyType' : 'RANGE'
            }
        ],
        AttributeDefinitions = [
            {
                'AttributeName': 'name',
                'AttributeType' : 'S'
            },
            {
                'AttributeName': 'lastname',
                'AttributeType' : 'S'
            }
    ],
            ProvisionedThroughput = {
                'ReadCapacityUnits' : 5,
                'WriteCapacityUnits' : 5
    }

    )
except dynamodb.exceptions.ResourceInUseException:
    print ("Skipping table creation as table already exists")



print (f"Table Status = {table.table_status}")