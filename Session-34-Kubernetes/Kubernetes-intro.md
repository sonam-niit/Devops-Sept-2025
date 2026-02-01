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

## Setting up a cluster using MiniKube

```bash
curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64

minikube start # start cluster
minikube status
kubectl cluster-info

kubectl get nodes # check connected nodes

kubectl dashboard --url # access Minikube Ip

```

## Create Pods 

```bash
kubectl run my-pod --image=nginx --port=80
kubectl get pods
kubectl describe pod my-pod
```
## Create Service

- Expose an application running in your cluster behind a single outward facing endpoint even when the workload is split across multiple backends.

![Service](service.png)

```bash
kubectl expose pod my-pod --type=NodePort --port=80
kubectl get svc
# if you are using eks you can directly access service by ip and given port
# Here its minukube, my machine is localhost, on top of it cluster running with some ip
# on top of it service is running which is not accessible directly
minikube service my-pod
# see the link try to access in Browser and the exit using ctrl+c
```

## Create Pod and service using YML

1. create my-pod.yml
2. create my-service.yml

```bash
kubectl apply -f my-pod.yml
kubectl get pods
kubectl describe pod nginx

kubectl apply -f my-service.yml
kubectl get svc
minikube service my-service
# check output in browser
```