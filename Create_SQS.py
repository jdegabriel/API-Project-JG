# This is a simple script to create an SQS Queue
import boto3

sqs = boto3.resource('sqs')
queue = sqs.create_queue(QueueName='wk-15-project')
print(queue.url)

