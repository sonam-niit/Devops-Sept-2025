# Kubernetes introduction

- Kubernetes is open source container orchestration platform which is designed to automate deployments, scaling and managing containers.
- manage multiple container between multiple environments possible using k8s.

## Features

- self Headling: auto restart, replce and rescheduling of failed containers.
- load balancing: distibute traffic and provide high availability
- auto scaling

### Why Kubernets and not Docker Swarm

**Docker Swarm**
- Docker's native container orchestration tool.
- it helps you to run multiple containers across multiple servers (nodes) and manage as cluster.
- converts multiple host into one cluster
- supports scaling, manage load balancing, handle service scheduling
- provides automatic failover

**Comaprison**
- Docker Swarm : easy, quick setup, good for small req
- Kuberenets: Powerfull, complex orchestration

### Setting Up Kubectl in Ubuntu

```bash
# Download the latest release with the command:
  curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

# Validate 
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"

echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
# you can see Kubectl:OK
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

kubectl version --client
```