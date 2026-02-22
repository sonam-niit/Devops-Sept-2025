resource "aws_vpc" "main" {
  cidr_block       = var.cidr_block
  instance_tenancy = "default"

  tags = {
    Name = "main"
  }
}

resource "aws_subnet" "main" {
  vpc_id     = aws_vpc.main.id # take vpc ref from above created resource
  cidr_block = var.cidr_block
  availability_zone = var.availability_zone

  tags = {
    Name = "Main"
  }
}