# Practice Task for Roles

- in existing Project of roles
- create 2 roles 1 for backend and 1 for frontend

- deploy application on instance
- write frontend task to frontend main.yml
- write backend task to backend main.yml

- edit playbook for adding roles
- also make sure you open required port from security groups so you can see output.

**After Completing above task you know how to divide ansible playbook in reusable modules**

## Create Multiple role using requirements.yml file

- create requirements.yml file
    - mention all roles name which you want to create

- run below command

    - ansible-galaxy role install -r requirements.yml

*Refer PPT notes to get idea*

- ansible-galaxy list --roles-path=./roles
- List created roles under ansible project
