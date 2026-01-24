# How Ansible Executes Tasks

1. Rule1
    - Tasks Run Sequentially (one task at a time)
    - Hosts Run in Parrellel (multiple servers at once)

- Ansible thinks: run task1 on all hosts --> then move to run task2 on all hosts

2. Default parrellelism

    - Ansible uses forks 
    - which helps to control how many hosts it manages at the same time
    - Default Forks: 5

```bash
ansible-config dump | grep DEFAULT_FORKS

# at the time of executing playbook change forks
ansible-playbook playbook.yml -f 10
```
3. incase if you have 100 servers then it will executes in batch mode
    - batch1: server1-5
    - batch2: server6-10
    - batch3: server11-15
    - batch4: server16-20
    - batch5: server21-25

4. Incase if you wnat to change entire forks value then
    - edit ansible.cfg
    - put forks = 20


## Limiting

- e.g. inventory

```ini
[web]
server1
server2
server3

[db]
db1
db2
```

- playbook is restrating nginx
- mentioned run it on all hosts
- ansible-playbook playbook.yml --limit server1,server2,server3

### Conditional based Limiting

```yml
- hosts: all
  tasks:
    - name: Restart Nginx
      service:
        name: nginx
        state: restrated
      when: "'web' in group_names"
```
## Tag Based Limiting

```yml
- hosts: all
  tasks:
    - name: Restart Nginx
      service:
        name: nginx
        state: restrated
      tags: web
    - name: Restart MySQL
      service:
        name: mysql
        state: restrated
      tags: db
```