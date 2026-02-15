# IaaC: infrastructure as Code

- its a morden approach for provisioning infra (servers, databases, storages, load balancers, networks) create using machine redable configurations files rather than manual process.

- when we do traditional setup it must be:
    + time consuming
    + error prune (human errors)
    + difficult to replicate

- using IaaC it makes developers life easier.

## IaaC follow 2 approaches

1. Declarative (What)
    - define what you want (desired state)
    - the tool will figure out how to achieve that
    - Terraform 

2. Imperative (How)
    - define how the infra should be created
    - write shell scripts
    - AWS CLI

### Popular Tools for IaaC

1. Terraform: multi cloud, declarative, state based
2. Chef/puppet: CM tools which is having capacity of creating infra
3. Ansible: CM + IaaC

### terraform vs Ansible

- terraform is more focused on provisioning servers and infra
- creating instances, create S3 buckets, VPC, load balancers etc

- Ansible is more focused on set up of softwares inside server
- installing packages with ansible