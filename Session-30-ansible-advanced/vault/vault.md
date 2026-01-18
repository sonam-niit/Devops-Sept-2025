# Encryption for Secret Data

- EDITOR=nano ansible-vault create secret.yml
- enter secret password, reenter
- it will open yml file enter your data

```yml
db_user: admin
db_password: mysecretpassword
```

- save file, exit

- try to read data
- cat secret.yml (not redable)

- Read it using Vault
- ansible-vault view secrets.yml (enter password and you can see the content)


- to read the same let's create playbook
- my-playbook.yml
```yml
- name: Valut Demo playbook
  hosts: localhost
  gather_facts: no

  vars_files:
    - secret.yml
  tasks:
    - name: Print DB username
      debug:
        msg: "DB UserName is {{ db_user }}"
```

```bash
ansible-playbook my-playbook.yml --ask-vault-pass
# enter password and playbook able to access vault data
```