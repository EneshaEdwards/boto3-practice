import boto3

dynamodb = boto3.client("dynamodb")

dynamodb.put_item(
    TableName="flowforge-practice",
    Item={
        "id": {"S": "flow-001"},
        "name": {"S": "Morning Stretch"},
        "minutes": {"N": "20"},
    },
)
print("Item saved")
