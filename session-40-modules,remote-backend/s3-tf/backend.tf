terraform {
  backend "s3" {
    bucket = "remote-backend-s3-sonam"
    key = "terraform.tfstate"
    region = "us-east-1"
    encrypt = true
    # dynamodb_table = "table_name" # used for Locking state when multiple users using
  }
}