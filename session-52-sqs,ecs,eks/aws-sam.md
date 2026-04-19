# AWS SAM (Serverless Application Model)

- AWS SAM is a frameword from AWS which helps to build, test and deploy serverless applications easily.

- whenever we want to setup infra using AWS, we are writing cloudformation templates.

- using SAM write simple yml code and SAM will convert that into cloudformation template automatically.

**How to work with SAM**

- https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html

- download as per your os
- id linux or wsl
- download
- open wsl and move to downloads folder

```bash
unzip aws-sam-cli-linux-x86_64.zip -d sam-installation
sudo ./sam-installation/install
sam --version
```

- for creating simple HelloWorld App
- follow this documentation

[Hello World using SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html)

- create sam Project

```bash
sam init 
# select 1 for inbuilt template
# continue with runtime by selecting any like python,node
sam build
sam local start-api # run locally
sam deploy # deploy on aws
```