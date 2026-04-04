# Security using IAM

- create Pocilcy
    - create using JSON
    - give policy: s3:GetObject , s3:PutObject
    - resources: give bucket arn /* (based on object access)
    - create Policy

- create User
    - attach created policy

- create Role
    - attach created Policy

- upload one image to s3 bucket and try to access via public URL
- you can see access denied

- how to see that because this pucket read permission is given to dev user
- iam -> user -> create access key

- wsl -> aws configure -> change access key and secret key
- then try to copy image from s3 bucket

```bash
cd /mnt/e
aws s3 cp s3://amzn-sonam-demo-basket/pwskills.png .
# give your bucket
# if image downloded that means permission given correctly
aws s3 presign s3://amzn-sonam-demo-basket/pwskills.png

# generate presigned URL for temporary access 
```