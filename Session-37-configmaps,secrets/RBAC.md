# RBAC: Role Based Authentication Control

- create role.yml
- cretae service-account.yml
- create role-binding.yml

```bash
kubectl apply -f role.yml
kubectl get role
kubectl apply -f service-account.yml
kubectl get sa
kubectl apply -f role-binding.yml
kubectl get rolebinding

kubectl auth can-i list pods --as=system:serviceaccount:default:dev-user
kubectl auth can-i get pods --as=system:serviceaccount:default:dev-user
kubectl auth can-i get secrets --as=system:serviceaccount:default:dev-user
kubectl auth can-i watch pods --as=system:serviceaccount:default:dev-user
kubectl auth can-i list deployment --as=system:serviceaccount:default:dev-user

## Delete 
kubectl delete rolebinding dev-user-binding
kubectl delete role dev-user
kubectl delete sa dev-user
```