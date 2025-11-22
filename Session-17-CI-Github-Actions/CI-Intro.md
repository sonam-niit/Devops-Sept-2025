# CI Fundamentals

## What is CI?

- CI is a development process where developers regularly merge code into shared repo and automated pipelines run tests and check to ensure the code is always in deployable state.

### What CI?

- detect bugs early
- improve your code quality
- reduce integration issues
- automate repetitive checks
- faster feedback for developer

### How to implement

- there are many tools available for CI/CD process
- Github Actions
- Jenkins
- Travis CI
- Circle CI

### Let's talk about Github Actions

- Github Actions is an automation platform built inside Github which alloes you to create workflows (pipelines) to build, test, deply your code automatically

- Simply I can say its CI/CD engine directly inside your Github Repo.
- to implement this we need to write YML file

#### What is YAML/YML ?

- Its human readable configuration language used to define settings, workflows, pipelines and structured data.
- it is using extentions like
    - .yml
    - .yaml (both are same)

**YML Rules**

- Indentation matters (use space and not tabs)
- Key-Value Format
    - key: value
- Lists
    fruits:
        - apple
        - banana
        - mango
- no curly {} needed

