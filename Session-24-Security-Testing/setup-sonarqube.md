# Setup SonarQube

- Download SonarQube From Below Link
[Download SonarQube](https://www.sonarsource.com/products/sonarqube/downloads/)

- Download Community Edition which is free

- once download is completed
- extract the entire sonarqube
- go to bin --> windows -> open this in CMD
- startSonar.bat (run this)

- for mac / linux or ubuntu users go to its respective folder
- run sonar.sh 

- then check localhost:9000 in browser
- wait for sometime to load login screen
- default credentials admin/admin
- change password later

## Start Sonar in WSL

- open sonarqube folder in wsl 
- move to linux folder

```bash
./sonar.sh start
./sonar.sh status
./sonar.sh console

# for checking logs
cd /opt/sonarqube/logs
# ls and check diffent log files
car sonar.logs
# here if you see sonar is operational means you can acces
# in browser using localhost:9000
# make sure you are using jdk 17
sudo apt update
sudo apt install openjdk-17-jdk -y
java -version

# logs you can check under the logs folder of sonarqube

cd /mnt/c/Users/<username>/Downloads/sonarqube/sonarqube/logs
cat sonar.log
``` 
