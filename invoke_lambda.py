import boto3
import json

lambda_client = boto3.client("lambda")

response = lambda_client.invoke(
    FunctionName="flowforge-hello",
)

result = json.loads(response["Payload"].read())
print(result)
print(result["body"])
