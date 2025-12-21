# Project For Sonar

- create folder node-project
- move to that folder
- create package.json file (npm init -y)
- npm i express (set dependency)
- create file index.js file
- create sonar-project.properties file for scan

- Download the scanner for Scanning Project

[Download Scanner from here](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/sonarscanner)

- extract the scanner and you can set path for your scanner
- or else run it with entire location

```bash
c://sonar-scanner/bin/sonar-scanner --help # for windows
/downloads/sonar-scanner --help # for mac
/mnt/c/Users/user-name/Downloads/sonar-scanner/bin/sonar-scanner --help
# for linux/ubuntu
```

# Let's Scan project using Sonar-Scanner

```bash
/mnt/c/sonar-scanner-linux/bin/sonar-scanner \
-Dsonar.host.url=http://localhost:9000 \
-Dsonar.token=<add_your_generated_token_from_sonarqube>

# here i have used the sonar token 
# generate it from sonarqube portal
# click on Account -> MyAccount -> Security Tab 
# Generate Token -> Global Analysis Token 
# pass that token here
```

- again update code using below values and run scan again

```js
//Security problem
const dbUser='admin'
const dbPassword='admin123'
```

- this time quality gate will fail due to hardcoded password.
