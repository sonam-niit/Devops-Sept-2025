resource "aws_instance" "web" {
  ami = var.ami
  instance_type = var.instance_type
  vpc_security_group_ids = [var.security_group_id]
  key_name = var.key_name # update for Key Pair
  subnet_id = var.subnet_id
  tags = {
    Name: var.instance_name
  }

  connection {
    type = "ssh"
    user = "ubuntu"
    host = self.public_ip
    private_key = file("~/.ssh/pwskills.pem")
  }

  provisioner "remote-exec" {
    inline = [ 
      "sudo apt update",
      "sudo apt install -y nginx",
      "sudo systemctl start nginx"
     ]
  }
}
# use of Remote Provisioner Completed