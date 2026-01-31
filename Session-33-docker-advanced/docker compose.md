# How to work with Docker Compose

- Basically docker compose will help to run multiple services
- manages shared network and shared volume in structured way

## Steps to execute

- create folder named docker-compose
- move to that and create folder named backend
- run below commands

```bash
cd backend
npm init -y 
npm i express mysql2
# delete node_modules folder because be want to manage using docker image
```
- create server.js file and add code as shown here
- create Dockerfile as shown here

### Creating Frontend

```bash
# come out from backend folder
cd ..
npm create vite@latest
# project name: frontend
# select framework: React
# lang: javascript
# use rolldown vite: no
# install npm: no
```
- once app is ready now create Dockerfile for frontend here

### Create docker-compose.yml

- add the code as shown here

```bash
docker compose version
docker compose up -d --build
# you can see image created, containers and network created
docker ps
docker logs mysql_container
docker logs backend # here if you see DB connected means 2 containers are communicating
docker logs frontend
```

- check in browser localhost:3000
- check in browser localhost:5173

- All services deployed successfully using Docker Compose

```bash
docker compose down # to stop all services
```