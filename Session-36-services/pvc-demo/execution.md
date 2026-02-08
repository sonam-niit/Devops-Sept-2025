# Execute How Pv and PVC works

- create pv.yml

```bash
kubectl apply -f pv.yml
kubectl get pv
```

- create pvc.yml

```bash
kubectl apply -f pvc.yml
kubectl get pvc
```

- create pod.yml which using PVC to clain volume on PV

```bash
kubectl apply -f pod.yml
kubectl get pods
kubectl describe pod pvc-demo-pod # you can see Bound details

kubectl exec -it pvc-demo-pod -- bash
# inside bash
echo "Hello From pv" > /usr/share/nginx/html/index.html
exit

# delete pod
kubectl delete pod pvc-demo-pod

# recreate pod
kubectl apply -f pod.yml
kubectl exec -it pvc-demo-pod -- bash

# inside bash
cat /usr/share/nginx/html/index.html # you can see data persisted
exit
```