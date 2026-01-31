# Working with Networks

- using network containers can communicate with each other

```bash
docker network --help # check command 
docker network create sonam
docker network ls # sonam driver type must be bridge

docker run -d --name app1 -p 8081:80 --network=sonam nginx 
docker run -d --name app2 -p 8082:80 --network=sonam nginx 

docker ps

# see the connectivity between containers
docker exex -it app1 sh
# in shell execute below command
curl http://app2 # see html response
exit
# same you can check from app2 as well
# if you want to check the connenctivity from anyother shell then
# run one busybox image under the same network and try to ping both containers

docker run --name test --network=sonam -it busybox
ping app1 # exit
ping app2 # exit
```