# AWS lambda

- run functions without managing any servers
- called serverless computing

## Let's Create

- aws console -> search for lambda -> click on lambda -> create function
- name (MyFirstLambda) -> runtime (python) -> arch (x86_64) default
- automatically to run lambda it will create default required role
- incase if you are creating multiple lambda functions them make sure not to create new role everytime you can reuse.

- create function (click)
- it will open code editor where you can edit your code.

- you can see default handler code which you can edit

```py

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello From My Lambda (Sonam Soni)'
    }

```

- when code changes done click on deploy
- click on test from Test tab
- click on details and check response received from Lambda

- check logs in cloudwatch
- check for log management -> log groups -> mylambda -> check logs

### Trigger this function from API

- in lambda function click on Add trigger button
- select API Gateway
- REST API
- Auth (Open)
- create (you will get one endpoint)
- just paste it in browser and then you can see response in JSON

