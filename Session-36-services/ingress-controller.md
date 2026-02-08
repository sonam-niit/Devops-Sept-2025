# Ingress 

- its a small entry gate for kubernetes cluster
- uses external IP
- route traffic based on URL paths or hostnames
- work with some ingress controllers (NGINX)

- Work Flow
- User --> Ingress Controller --> Service --> Pod

*Ingress is just a rule*
*ingress controller is actual worker*

## Let's Implement

```bash
minikube start
# enable ingress addon 
minikube addons enable ingress
# verify nginx-controller is running
kubectl get pods -n ingress-nginx
# deploy 2 apps
kubectl apply -f app1.yml
kubectl apply -f app2.yml
kubectl get pods
# create service.yml
kubectl apply -f service.yml
kubectl get svc
# create ingress resource (ingress.yml)
kubectl apply -f ingress.yml

# Configure Local DNS
minikube ip
# copy ip and then edit file sudo nano /etc/hosts
# add ip and then name like 192.168.49.2    demo.local

ping demo.local # if its configured correctly you can see its working
## access using curl
curl http://demo.local/app1
curl http://demo.local/app2

# Check Nginx Controller Logs
kubectl logs -n ingress-nginx deployment/ingress-nginx-controller
# here you can see your request is passing through nginx controller
```
- We are achieving same host, different Path --> diffrent Apps

## How its workin

- App serving path /
- ingress receive path /app1
- regex capture remaining path
- rewrite convert /app1 -> /
- now backend app running


### Practice Task (Host Based - SIMPLE way of routing)

- create another ingress.yml
```yml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: test-ingress
spec:
  rules:
  - host: app1.demo.local
    http:
      paths:
      - pathType: Prefix
        path: "/"
        backend:
          service:
            name: app1-service
            port:
              number: 80
  - host: app2.demo.local
    http:
      paths:
      - pathType: Prefix
        path: "/"
        backend:
          service:
            name: app2-service
            port:
              number: 80

```

- apply it
- edit your host file

- use same minikube it and register 2 host: 
    + 192.169.49.2 app1.demo.local
    + 192.169.49.2 app2.demo.local
- save file

- curl http://app1.demo.local
- curl http://app2.demo.local