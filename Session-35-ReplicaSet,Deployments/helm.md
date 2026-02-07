# Helm Chart

- It is a package format which is used by Helm, which is package manager or Kubernetes
- just like apt install ubuntu, yum for Linux, Helm install application in kubernetes in repetable, version-controlled and templataized way.

**Without Helm**
- manually create
    - deployment.yml
    - service.yml
    - pvc.yml
    - configmap.yml
    - secrets.yml
    - ingress.yml

- all these files can be managed by Helm chart

[installation Link](https://helm.sh/docs/intro/install/)

```bash
sudo snap install helm --classic
helm version

helm create myapp
# Check Myapp Folder structure

helm install myapp ./myapp/ --debug

# it will create deployment, pod and service
kubectl get deployment
kubectl get pods
kubectl get service

# to remove
helm uninstall myapp
```