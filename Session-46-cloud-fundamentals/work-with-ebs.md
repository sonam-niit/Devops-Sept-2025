# EBS (Elastic Block Store)

- block level storage
- to attach extra space to instance we can use it.
- used for backup, persistence storage

# step by step execution

- cretae instance Linux
- check instance zone (us-east-1b)
- then connect with instance, check about storage details
- using lsblk command

- create volume (general purpose volume)
- make sure volume needs to created in same zone where instance created
- in tags:
    - Name : extra-space
- create volume

- refresh: select volume : actions -> attach volume
- select instance
- check volume is attached to your instance, inside storage tab

- for detailed one go to terminal
- lsblk
- you can see 2 disk space attached to instance

```bash
sudo mkfs -t ext4 /dev/xvdf
mkdir data
# mount this directory to xvdf disk
sudo mount /dev/xvdf data
# lsblk (verify mounted or not)
# unmount
sudo umount /dev/xvdf
lsblk # verify 
```

# Practice Task

- create snapshot (Backup)
- select volume (extra-space)
- give description
- tags: Name : backup_exra_volume

# Restore Volume From Backup

- create new volume
- select snapshot (backup)
- give details (create)
- later on you can attach this volume to your instance