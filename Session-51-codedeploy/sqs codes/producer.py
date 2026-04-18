import boto3
import json
import uuid 


# Create SQS client
sqs = boto3.client('sqs',region_name='us-east-1')

# queue_url = 'SQS_QUEUE_URL'
queue_url = 'https://sqs.us-east-1.amazonaws.com/277707128105/order-queue'

order = {
    "orderId":str(uuid.uuid4()),
    "user":"Sonam",
    "amount":2500,
    "status":"CREATED"
}
# Send message to SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody=json.dumps(order)
)

print("Order sent to queue",response['MessageId'])