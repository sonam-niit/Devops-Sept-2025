# Setting node project and Pipeline using Github Actions

- create package.json file
- run this command in terminal
```bash
npm init -y
npm install jest # jest is dependency provided for testing node code
```

- create index.js file as below
```js
function sum(a,b){
    return a+b;
}
module.exports = sum;
```
- create folder named test and under that create file
- sum.test.js
```js
const sum = require('../index')

test(' adds 2 + 3 equals to 5 ',()=>{
    expect(sum(2,3)).toBe(5)
})

test(' add negative numbers ',()=>{
    expect(sum(-2,-3)).toBe(-5)
})
```
- edit package.json file and add below line under script

```json
"scripts": {
    "test": "jest"
  },
```

- also create .gitignore file to ignore node_modules folder from git push

- to check is locally you can run command
- npm test (check test cases passed or not)

- to make CI now create new file under workflows folder
- node-pipeline.yml

```yml
name: Node Js CI
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

            - name: Run tests
              run: npm test
 
```

- push your code on Github and check for Actions