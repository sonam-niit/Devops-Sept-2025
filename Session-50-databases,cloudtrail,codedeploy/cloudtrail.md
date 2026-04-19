# CloudTrail

- records every API call and actions made in your account
- like who did, what, When and from which region 

## how to use it

- aws console -> cloud trail (search)
- create trail: name: my-security-trail
- create new s3-bucket to store logs
- management events -> check on that
- choose event: check on management events
- check on read and write
- check summary and create cloud trail

### Once this done

- create instance
- stop instance
- terminate instance
- open train and check event history
- it will take time around 5-8 minutes
- then check on s3 bucket you can see logs

## Execute the same as task

- delete cloud trail created after the activity completed.