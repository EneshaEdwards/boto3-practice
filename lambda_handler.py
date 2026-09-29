import json
import boto3

dynamodb = boto3.client("dynamodb")

def lambda_handler(event, context):
  response = dynamodb.get_item(
    TableName="flowforge-practice",
    Key={"id": {"S": "flow-002"}},
)
  print(response["Item"])
  print(response["Item"]["name"]["S"])


  return {
        "statusCode": 200,
        "body": json.dumps(response["Item"]["name"]["S"])
    }