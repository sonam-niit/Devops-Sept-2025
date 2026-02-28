provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "example" {
  ami = "ami-0f3caa1cf4417e51b"
  instance_type= "t2.micro"

  tags = {
    Name = "myapp-${var.env}"
    # TTL = "2h"
  }
}

#  TTL not directly works from Terraform
# but you can use lambda or script so it will check creation time'
# if that time is more than 2h then terraform destroy resources