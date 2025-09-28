# Linux Advanced Commands

## Group Commands

1. Create Group
```bash
sudo groupadd developer # create group
cat /etc/group #list groups
cut -d: -f1 /etc/group # print group names
groups # to check  current users group
sudo usermod -aG developers sonam # add user to group
groups sonam # checking user groups to veify group added or not
sudo  groupmod -n testers developers #renaming group
sudo groupdel testers # delete group
```

## APT (Advanced Package Manager)

- package managing tool provided by linux
- commands for update and install
```bash
sudo apt update # update packages
sudo apt install python3 -y # it will install python
python3 -V # check the version to verify installation
python3 --version # check version
sudo apt remove python3 -y # remove python
#upgrade
sudo apt upgrade
sudo apt full-upgrade # more smarter install or remove packages req for upgrade
```

- update- downloads the latest packages from repositories
- it does not install or upgrade any software
- just like refreshing package-list

- upgrade
- actually install the newest version of the packages that you already have.
- it compares your installed version with updated package list and the upgrade it

```bash
sudo apt update && sudo apt upgrade
```
## purge to remove package + configuration files
```bash
sudo apt purge curl
```
## AutoRemove dependency which are not in use
```bash
sudo apt auto-remove
```

