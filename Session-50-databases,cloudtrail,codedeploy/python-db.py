import boto3

dynamodb= boto3.resource('dynamodb',region_name='us-east-1')

table = dynamodb.Table('users')

response=table.scan()
print('All items', response['Items'])


# explore other method from documentation and atleast do CRUD
# Create, Retrive, Update and Delete

# response = table.get_item(
#     Key={
#         'UserID': {
#             'S': 'user102',
#         }
#     }
# )

# print(response)

# python3 -m venv myenv
# source myenv/bin/activate
# pip install boto3
# python3 python-db.py

# Task: Scan with filter Projection value
# filter whose age is greater than 30
# show only name,age and Id (Projection)

# Hint: query written in PPT slide