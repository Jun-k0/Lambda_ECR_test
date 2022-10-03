import json


def my_handler(event, context):
    print("Hello, lambda")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
