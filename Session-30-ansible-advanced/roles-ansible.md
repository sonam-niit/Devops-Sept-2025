# Roles in Ansible

- roles are way to organize, reuse and manage automation code in a clean and standard structure.

**Uses**

- Reusability
- clean folder structure
- easy to maintain
- best practice to follow for large projects

- create folder named full-stack-project
- move to that folder and create roles

```bash
ansible-galaxy role init roles/webserver 
# you can see folder named webserver under roles
```

## Give main Logic

- tasks/main.yml (edit this)

```yml
- name: install nginx
  apt:
    name: nginx
    state: present
```

## Handlers: triggered by notify, used for restart/reload

- handlers/main.yml (edit this)

```yml
- name: restart nginx
  service:
    name: nginx
    state: restarted
```

## vars: variables with high priority

- vars/main.yml (edit this)

```yml
nginx_port: 80
```

## Defaults

- variables with low priority
- easy to override

- defaults/main.yml (edit this)

```yml
nginx_port: 8080
```

*Defaults < Vars*

## Files

- here you can keep files which is the source code of your app
- like create index.html
- the edit tasks/main.yml 

```yml
- name: install nginx
  apt:
    name: nginx
    state: present
# ADD THIS CODE
- name: Copy File
  copy:
    src: index.html # this lookup for file in files
    dest: /var/www/html/index.html
```

## templates

- you can add templating code like jija2 templates
- under templates create nginx.conf.j2

```j2
server {
    listen {{ nginx_port  }};
}
```

## meta

- Role Dependencies & metadata
- edit meta/main.yml

```yml
dependencies:
    - role: common
```

## How to use Role under playbook

- create playbook.yml

```yml
---
- name: Demo for Roles
  hosts: server1
  become: true

  roles:
    - webserver
```

- Also create inventory.yml for ubuntu instance
- run ansible-playbook -i inventory.yml playbook.yml
- check ip and everything will work in browser

- Now to work with hanlder
- change var port to 8080
- update tasks/main.yml

```yml
- name: Configure Nginx
  template:
    src: nginx.conf.j2 # search under template folder
    dest: /etc/nginx/sites-enabled/default

  notify: restart nginx
```

- so now when you run playbook it will update default port to 8080 based on configuration
- then notify restart handler which will run the handler code
- server will restarted and now you can see the default page of nginx on public_ip:8080


## Static Inclusion
```yml
roles:
    - frontend
    - backend
```

## Dynamic Inclusion of Roles in Ansible

- Ansible will decide at runtime which role to run based on condition or variable

```yml
- include_role:
    name: backend
  when app_type == "backend"
```