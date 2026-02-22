# Modules in terraform

- a module is a container for multiple resources used together
- reusable, parameterized blue print for infra

### Modules Help

- reuse code (DRY principle)
- organize infra
- maintain consitency across environment
- simplify complex steps
- best practice to follow.

**Let's Implement**

- create folder named project
- create 3 modules under that
- vpc, sec group , ec2
- each folder contains 3 files main.tf, variables.tf and outputs.tf
- at root level also we need 3 root files main.tf, variables.tf and outputs.tf