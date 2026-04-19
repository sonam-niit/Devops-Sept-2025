# dynamoDB

- DynamoDB is serverless, high performance and no SQL DB service in AWS
- best for app which need fast and scalable data access

### DB creation

- dynamo db dashboard
- create table , name: users
- partition key (Primary Key) - UserID (data type string)
- sort (secondary key) - like emailID
- default settings
- create table

- click on explore table items
- scroll -> create item
- add primary key value, and add some more attribute to create item

### access using CLI

```bash
aws dynamodb get-item --table-name users --key '{"UserID":{"S":"user101"}}'

aws dynamodb put-item --table-name users --item '{
    "UserID":{"S":"user102"},
    "name":{"S":"John Doe"},
    "email":{"S":"john@gmail.com"}
}'
```