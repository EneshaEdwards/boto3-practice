import boto3

s3 = boto3.client("s3")
response = s3.list_buckets()

for bucket in response["Buckets"]:
    print(bucket["Name"])


import boto3

s3 = boto3.client("s3")
bucket_name = "flowforge-practice-enesha-4821"

response = s3.get_object(Bucket=bucket_name, Key="notes.txt")
content = response["Body"].read().decode("utf-8")
print(content)
