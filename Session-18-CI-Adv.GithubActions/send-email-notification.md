# Send Email Once App build Successfully

- used one send-email-action 
[Reference Link](https://github.com/dawidd6/action-send-mail)

- update your Existing React WorkFlow

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
            - name: Send Email Notification
              uses: dawidd6/action-send-mail@v6
              with:
                server_address: smtp.gmail.com
                server_port: 465
                username: ${{secrets.MAIL_USERNAME}}
                password: ${{secrets.MAIL_PASSWORD}}
                subject: React App Build Successfully
                to: ${{secrets.RECEIVER_EMAIL}}
                from: ${{secrets.MAIL_USERNAME}}
                body: "Build job of ${{github.repository}} for Branch: ${{ github.ref_name }} completed successfully!"
```

- Now you need to set Secrets in Github Repository
- Go to Repo -> Setting
- Secrets and Variables
- Actions -> click on New Repo Secret
- add name of secret and value

![Repo Secret](images/Repo-sec.png)

- Now push your code and you will receive an email once app build successfully.
