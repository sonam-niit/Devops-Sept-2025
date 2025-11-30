# Jenkins file inside project

- file is not having any extension
- use Jenkinsfile as name of your file
- inside that you can write entire pipeline code and push it on Github

- in jenkins dashboard
- new-item --> name (pipeline-demo1) --> select pipeline --> OK
- description -> discard configuration
- pipeline option -> select pipeline script from SCM
- select Git: [Project Link](https://github.com/sonam-niit/SampleJavaMevan-Jenkins.git)
- give repository link
- branch name: main
- file name: Jenkinsfile

- save

- Build Now and check console