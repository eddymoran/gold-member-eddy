#import boto3 library
import boto3

#Connect to SQS
sqs = boto3.resource('sqs')

#Create and name queue
queue = sqs.create_queue(QueueName='orders_week15_project')

#Print queue URL
print(queue.url)