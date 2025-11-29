# Publish an artifact for App

- Let's Set up React application

```shell
npm create vite@latest

# it will ask for app name: react-app1
# select React
# Select Javascript
# just enter with default inputs
# you app will be ready and you can see running URL
# exit from it using CTRL+C enter Y
# move to that folder

cd react-app1
code . # to open folder in VS Code and check structure
```
- inside vs code 
- create folder .github under that
- create another folder workflows
- under that create file react-workflow.yml

```yml
name: React Project Artifact
on:
    push:
        branches:
            - main
jobs:
    build:
        runs-on: ubuntu-latest
        steps:
            - name: Checkout code
              uses: actions/checkout@v5

            - name: Set up Node Js Environment
              uses: actions/setup-node@v6

            - name: Install Dependencies
              run: npm install 

            # - name: Run tests
            #   run: npm test

            - name: Build React App
              run: npm run build
              
            # Upload Build Artifacts
            - name: Upload Build Artifacts
              uses: actions/upload-artifact@v4
              with:
                name: react-build
                path: dist

```
- push it on github
- check actions
- build --> upload artufact stage 
- here you can see the link for download artifacts

- refer this react project
[Reference Link Project](https://github.com/sonam-niit/React-Artifact-Workflow)