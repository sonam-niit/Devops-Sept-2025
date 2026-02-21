output "instance_public_ip" {
  description = "Public IP"
  value = aws_instance.server1.public_ip
}

output "instance_public_dns" {
  description = "Public DNS"
  value = aws_instance.server1.public_dns
}