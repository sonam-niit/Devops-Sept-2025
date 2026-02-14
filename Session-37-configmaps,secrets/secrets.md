# Secrets in Kubernetes

- A secret is used to store sensitive Data
- like Passwords, API Keys, Database credentials, Certificates

- Secrerets can be encoded with base64 
- store in etcd storage
- we can use in pod using volumes(files) / environment variables

## Create Secret

```bash
# encode values
echo -n "admin" | base64
echo -n "password123" | base64
```

- create secret.yml
```bash
kubectl apply -f secret.yml
kubectl describe secret db-secret
```

- create pod.yml
```bash
kubectl apply -f pod.yml
kubectl get pods
kubectl exec -it secret-demo-pod -- sh
# inside shell
echo $DB_USER
echo $DB_PASSWORD
exit
```

- Similar to this you can try with volume as well

## Activity 
- create pod access secrets using volume
- check data