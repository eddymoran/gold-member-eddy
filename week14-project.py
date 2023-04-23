import boto3

ec2 = boto3.resource('ec2')

# Create 3 instances
instances = ec2.create_instances(
        ImageId="ami-06f952cb496a0dec8",
        MinCount=3,
        MaxCount=3,
        InstanceType="t2.micro",
        SubnetId='subnet-0fd7e8b1585be0a8d'
    )

# Print instance IDs
for instance in instances:
    print(instance.id)
    