# Jenkins with Sonar Qube Integration

- Run Sonar and Jenkins Together
- like in windows then both should run on windows
- if WSL then both app should run in WSL

1. open wsl

```bash
# check Jenkins status
sudo systemctl status jenkins
# incase if its not running then start
sudo systemctl start jenkins
```
- Login to Jenkins Dashboard
- access it in browser http://localhost:8080/

2. Start SonarQube

- Open Sonar folder and start SonarQube
- Access from http://localhost:9000

```bash
# move to the folder sonarqube/linux/bin/
./sonar.sh start
```
3. Go to Jenkins
    - manage Jenkins
    - plugins -> available pulgins
    - Search for SonarQube Scanner
    - click on Install
![Sonar Plugin](images/sonar-plugin.png)

4. Configure SonarQube in Jenkins

- manage Jenkins -> System
- SonarQube Servers
![Sonar Servers](images/sonar-servers.png)

- Check on Environment Variables
- click on add SonarQube

![Configuration](images/configuration1.png)

- in Generate Auth token
- click on Add -> click on Jenkins

![Secret Text](images/secret-text.png)

- Generate Token from Sonar Dashboard
- Account -> My Account -> Security Tab -> Generate User Token

![Token generate](images/generate-token.png)

- Add that token in Jenkins
![token in Jenkins](images/add-token-jenkins.png)

- Click on Add Button and then Click on Save


