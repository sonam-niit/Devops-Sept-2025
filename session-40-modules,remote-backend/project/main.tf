provider "aws" {
  region = "us-east-1"
}

module "vpc" {
  source = "./modules/vpc"
  cidr_block = "10.0.0.0/16" # 10.0.0.0 to 10.0.255.255
  subnet_cidr = "10.0.1.0/24"
  availability_zone = "us-east-1a"
}

module "sg" {
  source = "./modules/sg"
  vpc_id = module.vpc.vpc_id
}
module "ec2" {
  source = "./modules/ec2"
  subnet_id = module.vpc.subnet_id
  security_group_id = module.sg.sec_group_id
  instance_name = "webserver1"
  instance_type = "t2.micro"
  ami = "ami-0b6c6ebed2801a5cb"
}