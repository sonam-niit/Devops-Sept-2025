# pipelines in CI

- Jenkins Pipeline is a way to define your entire CI/CD process as code
- you can create pipeline inside jenkins as well
- you can also create pipeline in your project as well. 
- file name is Jenkinsfile

## Why to use

- pipeline as code
- easy to review
- more stable than free style projects
- supports complex CI/CD workflows
- Better for Deops automation

## 2 types of Pipeline

1. Declarative pipeline:
    - most common and easy
    - structured with simple syntax

```groovy
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "Building the project"
            }
        }
        stage('test') {
            steps {
                echo "Testing the project"
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying the project"
            }
        }
    }
}
```
2. Scripted Pipeline
    - more on groovy syntax
    - more flexible
    - more complex 
    
```groovy
node {
    stage('build'){
        echo "Building...."
    }
    stage('test'){
        echo "testing...."
    }
    stage('deploy'){
        echo "deploying...."
    }
}
```
### let's Create one simple Pipeline

- New-Item -> name(pipeline1) -> select pipeline
- click on Ok
- write description, discard build configure
- scroll down and directly go to pipeline option
- defination - pipeline scription (option)
- from right cornet select HelloWorld pipeline
- save -> Build Now
- check console Output
- check pipeline stages , check pipeline oevrview

### Create Java Project Pipeline

```groovy
pipeline {
    agent any

    tools {
        maven "MyMaven"
    }
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/sonam-niit/SampleJavaMevan-Jenkins.git'
            }
        }
        stage('Build') {
            steps {
                sh 'mvn clean install'
                stash name: 'jar-artifacts', includes: 'target/*.jar'
            }
        }
        stage('test') {
            steps {
                sh 'mvn test'
            }
        }
        stage('archive') {
            steps {
                unstash 'jar-artifacts'
                archiveArtifacts artifacts: 'target/*.jar'
            }
        }
    }
}
```

- save
- CLick Build now