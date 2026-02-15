variable "ami" {
  default = "ami-08a6efd148b1f7504"
  type = string
  description = "Image ID for VM"
}
variable "instance_type" {
  default = "t2.micro"
}
variable "key_name" {
  default = "ansiblekey" # already created in EC2
}