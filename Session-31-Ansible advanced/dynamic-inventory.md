# Dynamic Inventory

- create project folder: my_project
- move: cd my_project
- create aws_ec2.yml

```yml
plugin: amazon.aws.aws_ec2

regions:
  - us-east-1

filters:
  instance-state-name: running

keyed_groups:
  - key: tags.Name
    prefix: name
  - key: tags.Role
    prefix: role

hostnames:
  - public-ip-address

compose:
  ansible_host: public_ip_address

strict: False
```

- create ansible.cfg

```cfg
[defaults]
inventory = aws_ec2.yml
host_key_checking = False
remote_user = ec2-user
private_key_file = ~/.ssh/ansiblekey.pem
```

- save both files 

```bash
ansible-inventory --list
ansible-inventory --graph

# Test connection
ansible all -m ping

# to run playbook
ansible-playbook playbook.yml 
```

**Note**

- if you guyz using wsl them make sure you are running the commnads under root folder
- If you try to run /mnt/d or any mounted location 
- WSL is unable to read that ansible.cfg file