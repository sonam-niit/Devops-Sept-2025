provider "aws" {
  region = var.region
}

resource "aws_instance" "server1" {
  ami = var.ubuntu_ami
  key_name = var.key_name
  instance_type = var.instance_type
  vpc_security_group_ids = [ aws_security_group.web_sg.id ] # use below sg while creating this instance
  tags = {
    Name: var.name_instance
  }
  user_data = <<-EOF
  #!/bin/bash
  apt update
  apt install nginx -y
  systemctl enable nginx
  systemctl start nginx
  EOF
}

resource "aws_security_group" "web_sg" {
  name="web-_sg"
  description = "Allow HTTP and SSH"
  #inbound rules
  ingress {
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port = 80
    to_port = 80
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  #outbound rule
  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}