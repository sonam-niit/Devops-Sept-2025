output "public_ip" {
  value = aws_instance.server1.public_ip
}
output "public_dns" {
  value = aws_instance.server1.public_dns
}