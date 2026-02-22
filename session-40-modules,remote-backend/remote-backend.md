# Remote Backend

- for creating Remote Backend
- create one bucket in s3: remote-backend-s3-sonam

- once bucket created go to your terraform code and add new file
- backend.tf

```tf
terraform {
  backend "s3" {
    bucket = "remote-backend-s3-sonam"
    key = "terraform.tfstate"
    region = "us-east-1"
    encrypt = true
    # dynamodb_table = "table_name" # used for Locking state when multiple users using
  }
}
```

- once its update init required

```bash
terraform init # it will use remote backend 
# incase if tfstate file is already exist locally it will ask do you want to use remote backend
# you can say yes 
# also it will ask that do you want to copy locat tfstate file to s3 bucket
# if you say yes it will get copied there.
terraform apply --auto-approve
# this time it will use s3 backend not local one
```