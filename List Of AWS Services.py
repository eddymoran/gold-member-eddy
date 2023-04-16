#Mini-Project

#Create a list of AWS services
print("Mini-Project - List Of AWS Services")

#The list should be empty at first
services_list = []
print("Empty list")

#Populate the list using append function, print the list
services_list.append("DynamoDB, RDS, VPC, S3, EC2, CodeDeploy, IAM, Cloudwatch")
print(services_list)

#Create a filled list
services_list = ['DynamoDB', 'RDS', 'VPC', 'S3', 'EC2', 'CodeDeploy', 'IAM', 'CloudWatch']
print(services_list)

#Print the length of the list
print("List Length: ",len(services_list))

#Remove two specific AWS services
#item 1 - list printed
services_list.remove('RDS')
print(services_list)

#Item 2 - list printed
services_list.remove('S3')
print(services_list)

#Print updated length of the list
print("List Length: ",len(services_list))