# Taint and Toleration

- A Taint is apppplied to a node and it repels pods that do not have a matching tolerance.
- Effects for Taints:
    + NoSchedule: Pod will not schedule on that node
    + PreferNoSchedule: Kubernetes tries to avoid that node
    + NoExecute: Pod is Evicted if running + new Pod won't schedule


## How to apply taint?
```bash
kubectl taint nodes minikube app=backend:NoSchedule
# Means only the pod with tolerance for app=backend can run on node1
# after running this command
kubectl run nginx --image=nginx
kubectl describe pod nginx
kubectl get pods # status is pending
```

## What is Tolerance
- This needs to be added on your pod
- means your perticular pod is allowed to run on node.

- tolerance-pod.yml
```yml
apiVersion: v1
kind: Pod
metadata:
  name: tolerated-pod
spec:
  containers:
  - name: nginx
    image: nginx
  tolerations:
  - key: "app"
    operator: "Equal"
    value: "backend"
    effect: "NoSchedule"
# this file will create a pod that can run on tainted node
```
```bash
kubectl apply -f tolerated-pod.yml
kubectl get pods
# you can app=backend pod is runningbut still above nginx is pending
```

## Remove Taint
```bash
kubectl taint nodes minikube app=backend:NoSchedule-
# - symbol indicating removal

kubectl get pods # pending pod is showing status contanerCreating or running
```