# Create Maven Project using FreeStyle

**Configure Maven Inside Jenkins**

- Manage Jenkins --> Tools --> scroll down
- select Maven installation
- type name: MyMaven
- install automatically from apache
- default version 3.9.11
- save

**Create free Style Project**

- Item --> New Item --> Free Style Project
- set Discard old builds etcc..
- under the build step
- select Invoke Top Level Maven targets
- select the MyMaven that you have created
- in Goals type: --version
- save and  build project
- you can see success also check console output to see version

**If selected Execute shell**

- then your command will be: mvn -version
- for this execute in your system maven must be installed
- sudo apt install maven -y
- otherwise build get failed