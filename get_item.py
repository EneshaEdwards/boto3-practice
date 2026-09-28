import boto3

dynamodb = boto3.client("dynamodb")

response = dynamodb.get_item(
    TableName="flowforge-practice",
    Key={"id": {"S": "flow-001"}},
)

print(response["Item"])
print(response["Item"]["name"]["S"])
