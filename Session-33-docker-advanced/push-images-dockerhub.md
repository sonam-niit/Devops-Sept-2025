# Push Images to Docker Hub

1. Create Account on Docker Hub
2. Once Account created Successfully open terminal/wsl

```bash
docker login
# enter username
# enter password , not visible just type and enter
# you can see login succeded
# if it will ask you to register device then open given link in browser
# copy shell code and register your device.
```

3. Let's create image and push

```bash
# move to nodeapp location
docker build -t mynodeapp .
docker images # verify image created
docker tag mynodeapp:latest sonamsoni/mynodeapp:v1
# mynodeapp:latest my local images
# sonamsoni/mynodeapp:v1 --> sonamsoni is my username on dockerhub
# mynodeapp is the name i want to give for my image
# v1: is the version
docker push sonamsoni/mynodeapp:v1 # push image
```