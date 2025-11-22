# let's Create one workflow to understand

- create a folder named Github-Workflow-demo
- move to that folder
- create .github folder
- under that create workflows folder 
- under that create print.yml file

- now add below code in your print.yml file

```yml
name: Print Message
on:
    push:
jobs:
    say-hello:
        runs-on: ubuntu-latest

        steps:
            - name: Print a Message
              run: echo "Hello! A push detected in repo"
```

- save your file and push it on github repo
- when push done check actions tab in github and see the workflow execution steps

## Print commit message

- create one more file named commit-message.yml
- include below code

```yml
name: Show commit message
on:
    push:
        branches:
            - main
            - mastesr
jobs:
    print-message:
        runs-on: ubuntu-latest

        steps:
            - name: Checkout code
              uses: actions/checkout@v5

            - name: Print Commit message
              run: |
                echo "Commit Message"
                echo "${{ github.event.head_commit.message }}"
 
```

- save and push on repo
- check actions this time your can see both workflow executed
- previous flow build can be num 2 and newly created workflow build you can see num 1

*Reference Repo Link*
[GitHub Workflow Examples](https://github.com/sonam-niit/github-workflow-example.git)