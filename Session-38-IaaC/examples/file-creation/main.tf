provider "local" {}

resource "local_file" "sample" {
  filename = "hello.txt"
  content = "Hello From terraform"
}

# terraform is having its own lifecycle
# do terrafrom init: 
# it will create .terraform folder and .terraform.lock.hcl file

# terraform plan: show you the plan for resource creation
# terraform apply: it will create resource
# before create resource it will ask your permisson and when you yes will create

# if you want to by pass
# terraform apply --auto-approve
# directly create resources.

# entire file state managed under terraform.tfstate
# to destroy the created resources
# terraform destroy (manually say yes)
# terraform destroy --auto-approve
