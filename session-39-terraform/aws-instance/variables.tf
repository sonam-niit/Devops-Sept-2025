variable "region" {
  type = string
  default = "us-east-1"
}

variable "ubuntu_ami" {
  type = string
}

variable "key_name" {
  type = string
}
variable "name_instance" {
  type = string
  default = "web_server"
}
variable "instance_type" {
  type = string
  default = "t2.micro"
}