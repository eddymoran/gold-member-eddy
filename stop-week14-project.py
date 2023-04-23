import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Stop instances
response = ec2.stop_instances(
    InstanceIds=['i-0a55cba81944190f6', 'i-0a9448f148561b830', 'i-0171ea8fd1fbdc956']
)

# Print response
print(response)