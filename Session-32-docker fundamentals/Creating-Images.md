# Creating images with Docker

- for your any app or project, I want to create Docker image

**How?**
- create Dcokerfile 
- file name is Dockerfile only, no extension
- in this file we need to set some configurations like what os what dependency, how to run applcation, which port you want to expose.

## Basic Components to write in Dockerfile

1. FROM: Base Image(starting point)
2. WORKDIR: set working directory inside container
3. COPY: copy your codes from host to container
4. RUN: Execute command to build an image
5. CMD: Default command when container starts
6. ENV: set environment variables
7. ENTRYPOINT: Main command that always run
8. EXPOSE: inform container to listen which port

## Create NodeAPP for Docker Image creation

- create folder node-app
- move to the folder: cd node-app
- create package.json file

```json
{
  "name": "app",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "type": "commonjs",
  "dependencies": {
    "express": "^5.2.1"
  }
}

```
- Create Docker file
```dockerfile
# Base Image
FROM node:22-alpine 
# Set working directory
WORKDIR /app
# copy package.json
COPY package.json .
# install dependencies
RUN npm install
# Copy other files and folders
COPY . .
# EXPOSE port
EXPOSE 3000

# RUN app
CMD [ "node" , "index.js" ]
```

**Build Image**

```bash
docker build -t mynodeapp .
# build to build an image
# -t target name of images
# . indicates location of fockerfile which is root location
docker images
# run in container
docker run -d --name myapp -p 3000:3000 mynodeapp
docker ps # if up then access localhost:3000
docker logs myapp
```
# if you change your code
- then build images again
- stop old container and run new one.