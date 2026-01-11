# Ansible Adhoc Commands

- Adhoc commands are one line ansible commands used to perform quick task on managed nodes without running entire playbook

- Used for
- check connectivity
- Install packages
- Restart service
- copy file
- gathering system info

```bash
# check connectivity
ansible all -i inventory.yml -m ping
# runn command
ansible all -i inventory.yml -m command -a "uptime"
# shell with piping
ansible all -i inventory.yml -m shell -a "df -h | grep /dev"
# simple command using disk usage
ansible all -i inventory.yml -m command -a "df -h"
# install package
ansible all -i inventory.yml -m apt -a "name=nginx state=present" -b
# Service
ansible all -i inventory.yml -m service -a "name=nginx state=started" -b
```