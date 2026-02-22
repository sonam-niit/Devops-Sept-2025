resource "aws_vpc" "main" {
  cidr_block       = var.cidr_block
  instance_tenancy = "default"

  tags = {
    Name = "main"
  }
}
resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main.id
}

resource "aws_subnet" "main" {
  vpc_id     = aws_vpc.main.id # take vpc ref from above created resource
  cidr_block = var.subnet_cidr
  availability_zone = var.availability_zone
  map_public_ip_on_launch = true
  tags = {
    Name = "Main"
  }
}
resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.main.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }
}
resource "aws_route_table_association" "public_assoc" {
  subnet_id = aws_subnet.main.id
  route_table_id = aws_route_table.public_rt.id
}