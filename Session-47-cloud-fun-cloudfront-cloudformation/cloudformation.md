# cloud Formation

- IaaC
- instead of manually creating S3, EC2, ALB, VPC create using code
- create template (YAML / JSON)
- cloud formation creates all automatically

1. Template:
    - a file written in YAML
    - define resources: s3, EC2, IAM roles

2. Stack:
    - Its a running instance of your template
    - when we deploy this cloud formation file -> it creates stack

3. Resources:
    - aws services: s3, EC2, iam, RDS etc..

4. Parameters:
    - Inputs which you can pass dynamically (variables)
    - instance-type: t2.micro

5. Outputs:
    - values returned after stack creation successfully
    - Public IP of EC2 instance

## Let's Implement

- Let's create an EC2 instance

