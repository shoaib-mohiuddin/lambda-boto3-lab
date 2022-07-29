import boto3
import json

# Initialize boto3 client
s3_client = boto3.client('s3')
ec2_client = boto3.client('ec2')

# List buckets function
# response = s3_client.list_buckets()
# print(response)
# print(response["Buckets"])
# print(json.dumps(response, default=str))

# List all buckets from response
# for buc in response["Buckets"]:
#     print(buc["Name"])
#     print(buc["CreationDate"])

# List all instances
# response = ec2_client.describe_instances()
# print(json.dumps(response, default=str))
# for instance in response["Reservations"][0]["Instances"]:
#     print(instance)
#     print(instance["InstanceId"])

response = ec2_client.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]
)


for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        print(f"Instance Id: {instance['InstanceId']} - State: {instance['State']['Name']}")
        # print(f"Instance Id: {instance['InstanceId']} - State: {instance['State']}")