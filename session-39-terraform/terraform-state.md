# Terraform State

- track resource infra details
- once you have created aws-instance folder with main.tf, variables.tf,outputs.tf and terraform.tfvars

```bash
terraform init

terraform apply --auto-approve

teraform state list

terraform state show aws_security_group.web_sg
terraform state show aws_security_group.aws_instance.server1

terraform destroy --auto-approve
```