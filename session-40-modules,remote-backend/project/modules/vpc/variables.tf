variable "cidr_block" {
  description = "CIDR Block Values"
}
variable "subnet_cidr" {
  description = "Subnet CIDR Values"
}
variable "availability_zone" {
  description = "Availability Zone for VPC"
  # this we will pass from root file
}