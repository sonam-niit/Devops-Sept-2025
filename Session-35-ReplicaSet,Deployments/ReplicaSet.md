# What is Pod?

- Pod is the smallest unit in Kubernetes

- Pod:  one running container or sometimes few tightly couples containers running
        - sharing Same IP, storage amd network.

*If Pod Dies, kubernets does not automatically bring it back*

# ReplicaSet

- ensures that specified number of identical Pods are always running
- I want 3 copies of pod running at same times.

- If one pod crash - replicaset create new one
- if one pod is deleted - replicaset recreates it.

## How to create Replicaset

- create file replicaset.yml as shown here
```bash
kubectl apply -f replicaset.yml
kubectl get rs
kubectl get pods # 3 running

# copy any pod name and try to delete
kubectl delete pod <pod_name>
kubectl get pods # you can see new pod is getting created

kubectl delete replicaset nginx-rs
```

# What is Deployment?

- Deployment is higher level contoller which manages
    - Replicasets
    - Pods
    - Updates(rollouts)
    - Rollbacks
    - Scaling

** Deployment manages Replicaset and Replicaset manages pods**

```yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80

```
```bash
# create deploymentyml
kubectl apply -f deployment.yml
kubectl get deployment
kubectl get pods
kubectl describe deployment nginx-deployment

# Let's update the nginx Pods to use the nginx:1.16.1 image instead of the nginx:1.14.2 image
kubectl set image deployment/nginx-deployment nginx=nginx:1.16.1
kubectl rollout status deployment/nginx-deployment

kubectl describe deployment/nginx-deployment 

kubectl rollout history deployment/nginx-deployment # see rollout history

kubectl rollout history deployment/nginx-deployment --revision=1 # Check version
kubectl rollout history deployment/nginx-deployment --revision=2 # Check Version

## Rollback
kubectl rollout undo deployment/nginx-deployment

kubectl rollout history deployment/nginx-deployment # see rollout history

kubectl rollout history deployment/nginx-deployment --revision=3 # Check version
kubectl rollout history deployment/nginx-deployment --revision=2 # Check Version

kubectl describe deployment/nginx-deployment

kubectl scale deployment/nginx-deployment --replicas=10
kubectl get pods

kubectl scale deployment/nginx-deployment --replicas=3
kubectl get pods

## AutoScalling
kubectl autoscale deployment/nginx-deployment --min=3 --max=7 --cpu=70% # real executio we will do  with EKS Cluster
kubectl get hpa

kubectl describe hpa nginx-deployment

kubectl delete hpa nginx-deployment
kubectl delete deployment nginx-deployment

```

[Reference For Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)

## Maintain Rollout using YML with Annotations

```yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
  annotations:
    kubernetes.io/change-cause: Created with Version 1.14.2
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80

```

```bash
kubectl apply -f deployment.yml
kubectl get deployment
kubectl get pods

# Change Code with version 1.16.1 add updated annotation
# change Cause message and version 1.16.1
kubectl apply -f deployment.yml
kubectl rollout history deployment/nginx-deployment

```