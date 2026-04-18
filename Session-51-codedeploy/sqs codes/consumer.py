import boto3
import json
import time

# Create SQS client
sqs = boto3.client('sqs')

# queue_url = 'SQS_QUEUE_URL'
queue_url = 'https://sqs.us-east-1.amazonaws.com/277707128105/order-queue'

while True:
    messages = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=10
    )
    if "Messages" in messages:
        for msg in messages["Messages"]:
            order = json.loads(msg["Body"])
            print("Processing order: ",order)
            
            print(f"Email send for order {order['orderId']}")
            
            # Delete received message from queue
            sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=msg["ReceiptHandle"]
            )
    else:
        print("No messages.....")
        time.sleep(5)