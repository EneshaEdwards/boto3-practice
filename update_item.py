import boto3

dynamodb = boto3.client("dynamodb")

dynamodb.update_item(
    TableName="flowforge-practice",
    Key={"id": {"S": "flow-001"}},
    UpdateExpression="SET minutes = :m",
    ExpressionAttributeValues={":m": {"N": "30"}},
)
print("Item updated")
