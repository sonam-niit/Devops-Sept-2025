# Approval in Github Actions

- Create Github Repo
- Create Workflow directly by clicking on Actions and configure workflow

- Add Below mentioned code

```yml
name: CI

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

  workflow_dispatch:
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build
        run: echo "Building Application"
  
  test:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Test
        run: echo "Running TestCases"

  deploy:
    runs-on: ubuntu-latest
    needs: test
    environment: production # Ask for Approval
    steps:
      - name: Deploy
        run: echo "Deploying app to production"

```
- Commit and check Actions but it stages executed without approval

- Now go to repo --> Settings --> Environment
- Check required reviewers , add members
- now again try to run workflow from browser itself
- after that you can see approval req is comming
- confirm approval and then deploy will execute 