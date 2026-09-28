
import boto3

dynamodb = boto3.client("dynamodb")

dynamodb.create_table(
    TableName="flowforge-practice",
    KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
    AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
    BillingMode="PAY_PER_REQUEST",
)
print("Table creating...")
