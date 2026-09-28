import boto3

dynamodb = boto3.client("dynamodb")

response = dynamodb.query(
    TableName="flowforge-practice",
    KeyConditionExpression="id = :id",
    ExpressionAttributeValues={":id": {"S": "flow-001"}},
)

print("Count:", response["Count"])

for item in response["Items"]:
    print(item["name"]["S"], "-", item["minutes"]["N"], "minutes")
