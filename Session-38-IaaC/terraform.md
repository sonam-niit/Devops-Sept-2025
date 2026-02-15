# Terraform

- It is an IaaC tool
- which manages all infra in declarative approach using HCL
- download extension: HashiCorp Terraform
- to get syntax highlighting in VS Code

## How to install terraform

[reference link](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)

```bash
# HashiCorp's GPG signature and install HashiCorp's Debian package repository
sudo apt-get update && sudo apt-get install -y gnupg software-properties-common

# Install HashiCorp's GPG key.
wget -O- https://apt.releases.hashicorp.com/gpg | \
gpg --dearmor | \
sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null

# Verify the GPG key's fingerprint.
gpg --no-default-keyring \
--keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg \
--fingerprint

# Add the official HashiCorp repository to your system.
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(grep -oP '(?<=UBUNTU_CODENAME=).*' /etc/os-release || lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list


sudo apt update && sudo apt-get install terraform

terraform -version

```

### How to create files in Terraform

- files have extension .tf
- writtens in HCL (hashicorp Configuration management)

### Core Coponents

1. Providers:
    - allows terraform to interact with cloud providers like aws, azure, gcp

```tf
provider "aws" {
  region = "us-east-1"
}
```

2. Resources:
    - infra component instance, s3 bucket, vpc
```tf
resource "aws_instance" "server1" {
  ami = "ami-08a6efd148b1f7504"
  instance_type = "t2.micro"
  key_name = "ansiblekey"
}
```

3. Variables:
    - sepearte variables in variables.tf files
    - we can use them in main.tf files

4. Outputs:
    - when resource created if you need to check resource Id
    - public IP and DNS
    - we can take it via outputs.tf


## Terraform Lifecycle

1. terraform init
2. terraform plan
3. terraform apply
4. terraform destroy


## Terraform Workflow for Usage

- create folder 
- under that create file named main.tf
- manage version control using Git 
- Review and Test
- Plan and apply
- deploy using CI/CD

## Check Aws Configuration

- aws configuration already done before ansible
- aws cli setup

[SetUp AWSCLI](https://github.com/sonam-niit/Devops-Sept-2025/blob/main/Session-29-Inventories/Dynamic-Inventory.md)

```bash
aws sts get-caller-identity
aws configure list
# if it is configured you can see the account details
```

## now Let's Create AWS instance using terraform

- create folder ec2
- create file main.tf

```tf
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "server1" {
  ami = "ami-08a6efd148b1f7504"
  instance_type = "t2.micro"
  key_name = "ansiblekey"
  tags = {
    Name: "sonam-linux-vm"
  }
}
```

```bash
terraform init
terraform plan
terraform apply --auto-approve
terraform destroy --auto-approve
```

- here you can see instance created
- to check output and variables you can create variables and output in same main.tf
- code will work as well but it becomes complex and not redable
- to make it redable create
- providers.tf

```tf
provider "aws" {
  region = "us-east-1"
}
```

- variables.tf

```tf
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
```

- main.tf

```tf
resource "aws_instance" "server1" {
  ami = var.ami
  instance_type = var.instance_type
  key_name = var.key_name
  tags = {
    Name: "sonam-linux-vm"
  }
}
```

- outputs.tf

```tf
output "public_ip" {
  value = aws_instance.server1.public_ip
}
output "public_dns" {
  value = aws_instance.server1.public_dns
}
```

*Now resource will be created you can see the output*

- these files create with the same name mentioned and they connected automatically no need to do any manual imports