# Practice Task

- Centralized logging service using SQS

**Producer Code-producing logs**
- create one python code that generates log
- that logs parse to sqs for process

**Consumer Code-processing logs**
- process logs 
- store in s3 bucket /elastic search

- stop consumer for sometime
- continue processing logs 
- again start and verify old logs from sqs will be processed.
