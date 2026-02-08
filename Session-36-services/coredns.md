# CoreDNS in kubernetes

- Convert Service names: into IP addresses
- let pods talk to each other using name instead of IP

```bash
kubectl get pods -n kube-system
# check code-dns already running
kubectl get svc  -n kube-system # check running service

# Check DNS config inside a pod
kubectl run testpod --image=busybox --restart=Never -- sleep 3600

kubectl exec -it testpod -- sh
# inside pod run below command
cat /etc/resolv.conf
exit

```

## Create Deployment

```bash
kubectl create deployment nginx --image=nginx # deployment
kubectl expose deployment nginx --port=80 # expose service
kubectl get svc

kubectl exec -it testpod -- sh
# inside shell
nslookup nginx # name of service
ping nginx 
wget -qO- http://nginx # you can see HTML Response

```