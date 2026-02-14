# Config Map

- to store non confidential information 
- store values in Key-Value Pair

- Lab

1. Create Config Map
2. Use it in Pod
3. Verify

- create configmap.yml

```bash
kubectl apply -f config.yml
kubectl describe configmap app-config
```

- create pod.yml

```bash
kubectl apply -f pod.yml
kubectl describe pod config-demo-pod
kubectl get pods # once it is running

kubectl exec -it config-demo-pod -- /bin/sh
# inside the shell run below commands
echo $APP_COLOR
echo $APP_MODE
exit
```
## Use Config Map As Volume

- create demo-pod.yml
```bash
kubectl apply -f demo-pod.yml
kubectl describe pod mypod
kubectl get pods # once it is running

kubectl exec -it mypod -- sh
# inside the shell run below commands
cd /etc/config
ls
cat APP_COLOR
cat APP_MODE
exit
```
# here its reading data as File