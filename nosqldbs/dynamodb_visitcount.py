
import boto3

def lambda_handler(event: any, context: any):
    username = event['user']

    visitcount: int = 0

    #Create dynamo db client
    client = boto3.resource('dynamodb')
    table_name = 'visitcount'
    table = client.Table(table_name)

    #get visitor count
    response = table.get_item(Key={"user" : username})

    #Featch the visit count from dynamo db
    if "Item" in response:
        visitcount = response['Item']['count']

    #Update the visitor count
    visitcount+= 1

    #update the table in dynamodb
    table.put_item(Item={'user' : username, "count": visitcount})


    message = f'Hello {username}, you have visited this page {visitcount} times.'
    return {'message': message}

if __name__ == "__main__":
    event = {'user': 'ChatGpt 3.5'}
    print(lambda_handler(event, None))

