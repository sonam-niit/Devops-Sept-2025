# SQS Simple Queue Service

- create SQS queue first
- AWS console -> search for SQS -> create queue 
- select type: standard queue
- name: order-queue
- configuration keep default
- keep all options default - create queue

### Setup code to connect with queue

- create producer.py
- create consumer.py

- open wsl run below command
- sudo apt install python3-boto3
- open 2 terminals
- in 1st terminal run producer.py (send order req)
- in 2nd terminal run consumer.py (process order req)

- you can try to stop consumer and produce multiple req
- after sometime try to run consumer.py again and you can see all pending producer req will be processed by consumer.