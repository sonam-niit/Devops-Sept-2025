# Vault for Secret Management in Terraform

- Vault is a tool for securely stroing and accessing secrets like API Keys, DB passwords, SSL certificates and encryption keys.
- for secret management we can use environment variables as well
- export AWS_SECRET_KEY="your_secret_access_key"

- use in terraform like this

```tf
provider "aws"{
    access_key = var.AWS_SECRET_KEY
}
```

## Why vault instead of .env ?

- manage leaks (git commit)
- accidently sharing data
- provide centralized access
- secure storage for encryption
- supports for dynamic secrets

## Let's use Vault Locally

```bash
sudo snap install vault
vault help
vault server -dev
```

- After setting up your Vault Server 
- Open Another WSL to understand how to create secrets and access them

```bash
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='your_server_token'

# create secret
vault kv put secret/db-pass password="sonam123"

# get secret
vault kv get secret/db-pass
```

# Same if you want to access in Terraform 

- create main.tf

```tf
provider "vault" {
  
}
data "vault_kv_secret" "db"{
    path = "secret/db-pass"
}
```
- create outputs.tf

```tf
output "database_password" {
  value = data.vault_kv_secret.db.data
  sensitive = true
}
```

- open this location where you executed previous commands for secret creation and retrival
- if you are opening any other terminal then make sure you export Address and Token Both

```bash
terraform init
terraform apply -auto-approve
```

- you can see here I can access secrets directly

## access vault with login then follow belo steps

- start vault server in one wsl terminal: vault server -dev
- open another terminal and make sure to export address:
- export VAULT_ADDR='http://127.0.0.1:8200'
- then run: vault login: enter token (its not visible just paste)

```bash
vault kv put secret/cred username="admin" pass="admin123"
vault kv get -format=json secret/cred
```

- another way to access is Terraform

- use main.tf
```tf
provider "vault" {
  
}
data "vault_kv_secret" "db"{
    path = "secret/cred"
}
```

- create outputs.tf

```tf
output "database_password" {
  value = data.vault_kv_secret.db.data["pass"]
  sensitive = true
}
output "database_username" {
  value = data.vault_kv_secret.db.data["username"]
  sensitive = true
}
```

```bash
terraform init
terraform apply -auto-approve
# in output you can see
```