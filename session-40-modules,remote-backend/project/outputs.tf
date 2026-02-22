output "vpc_id" {
  value = module.vpc.vpc_id # from module vpc id is coming and take it here
}

output "public_ip" {
  value = module.ec2.public_ip
}