import boto3

dynamodb = boto3.client("dynamodb")

dynamodb.delete_item(
    TableName="flowforge-practice",
    Key={"id": {"S": "flow-001"}},
)
print("Item deleted")
