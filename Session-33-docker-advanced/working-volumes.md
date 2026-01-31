# Volumes in Docker

- Docker container is not having any persistent volume
- once container stopped or removed data will be lost
- to manage the data after deleting container as well you can use docker volume.

```bash
sudo docker volume --help
sudo docker volume create storage
docker volume ls

docker run -d --name app1 -v stoarge:/usr/share/nginx/html -p 8081:80 nginx
docker exec -it app1 bash
# update index.html content
echo "<h1>Hello Form Docker Volume</h1>" > /usr/share/nginx/html/index.html
exit

# updated: check localhost:8081

sudo docker rm -f app1 
# to check data persist or not create one more container and use the same volume
docker run -d --name app1 -v stoarge:/usr/share/nginx/html -p 8081:80 nginx
docker inspect app1 # check bind mount storage
# also check in browser localhost:8081 # you can see index.html content

# to just access data you can also use simple busybox images
docker run --name test1 -v storage:/data -it busybox
# this time storage is mounted on data lcoation
ls /data # you can see index.html
cat /data/index.html # you can see the same content

# try without volume and it will show you default nginx page because of data lost
```

## bind Mounts

- Bind Mounts directly maps your local system folder into container
- whatever changes on host -> instant chnages in container
- Whenever container writes --> appears on host
- perfect for development

```bash
cd ~ # go to root location
mkdir myapp
echo "Hello from Host machine"> myapp/index.html
docker run -d --name myapp -v ~/myapp:/usr/share/nginx/html -p 8081:80 nginx
# check localhost:8081 you can see the host machine content
docker inspect myapp # check data binds
# try to make some changes in index.html
nano ~/myapp/index.html
# add some content, save it and check browser again
# changes reflect directly without restrating a container
```