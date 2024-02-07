import json
from decimal import Decimal
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('resume-challenge')

def lambda_handler(event, context):
    try:
        response = table.get_item(Key={'id': '1'})
        views = response.get('Item', {}).get('views', Decimal('0'))
        views += 1
        table.put_item(Item={'id': '1', 'views': views})

        return {
            'statusCode': 200,
            'body': json.dumps({'views': int(views)})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
