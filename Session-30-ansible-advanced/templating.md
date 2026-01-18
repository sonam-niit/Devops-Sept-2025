## Jinja 2 templating

- create sepearte project
- create role frontend
- tasks/main.yml

```yml
---
- name: Install Nginx
  apt: 
    name: nginx 
    state: present
    update_cache: yes

- name: Copy Custom HTML
  template:
    src: index.html.j2
    dest: /var/www/html/index.html
  notify: restart nginx

```

- template create index.html.j2

```j2
<!DOCTYPE html>
<html lang="en">
<head>
    <title> {{ nginx_title }} </title>
</head>
<body>
    <h1>{{ nginx_msg }}</h1>
</body>
</html>
```

- variables under default/main.yml
```yml
---
# defaults file for roles/frontend

nginx_title: "Welcome to my Website"
nginx_msg: "Deploying this using ansible role"
```

- handler/main.yml

```yml
---
# handlers file for roles/frontend

- name: restart nginx
  service:
    name: nginx
    state: restarted
```