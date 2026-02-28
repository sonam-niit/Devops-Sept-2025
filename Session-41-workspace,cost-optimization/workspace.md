# Creating Workspace

```bash
mkdir workspace-demo
cd workspace-demo

terraform init
terraform workspace new dev
terraform workspace new prod

terraform workspace list # * showing current workspace

terraform workspace select dev # change Workspace
# here if i run terraform apply it will create instance under dev
terraform plan -var-file="tfvars/dev.tfvars"
# create file prod.tfvars and dev.tafvars under tfvars folder
terraform apply -var-file="tfvars/dev.tfvars" --auto-approve

terraform workspace select prod # change Workspace
terraform plan -var-file="tfvars/prod.tfvars"
terraform apply -var-file="tfvars/prod.tfvars" --auto-approve
```

- For Above Commands 2 seperate state files maintained for both environments
- you can use same code in 2 isolated environments

