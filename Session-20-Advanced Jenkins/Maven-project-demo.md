# Build Maven Project

## Using Free Style Project

- Item --> New Item --> Project Name (MavenProjectFreeStyle)
- Select Free Style Project option --> Ok
- give some description
- configure discard old builds
- Source Code Management -> select Git
- put repo link: [Repo Link](https://github.com/sonam-niit/SampleJavaMevan-Jenkins.git)
- type branch name: main
- In Build steps: Invoke top-level Maven targets
- select MyMaven (We created yesterday under jenkins tools)
- Goals: clean test package (clean project, run tests, build JAR)
- Post Build Action: Archive the artifacts
- Files to archive: target/*.jar
- save

- Build Now
- click on #1 -> check console output
- see logs and see jar file is getting generated or not
- check Archive on Project Screen only (download it from here)


### Above process using Maven Project

- New Item -> name (MavenProject) -> select Maven Project
- ok 
- add description and discard builds configuration
- Git Repo Link with branch name main
- directly jump to maven goals: clean install package
- Post step select: run only if build succeed
- Post Build Action: Archive the artifacts
- Files to archive: target/*.jar
- save

- Build Now