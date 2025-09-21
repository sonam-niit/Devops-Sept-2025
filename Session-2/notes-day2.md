## Swapping memory

- basic Idea to control swap memory

1. Check Current Swap
```bash
free -h
swapon --show
```
2. Disable Swap (temporary)
```bash
sudo swapoff -a
```
3. Enable Swap
```bash
sudo swapon -a
```
## File System
1. check file details (list all disks and partition)
```bash
lsblk  #mac (diskutil list)
df -h # show you all mounted file system 
lsblk -f # to see file system types
df -T # see details with file types
```

## Ip address

```bash
ip a # show allnetwork interfaces and its IP Addresses
hostname # to see hostname
hostname -I # to see IP Address
```

subnets

192.168.1.0/26 -> 192.168.1.1 - 192.168.1.62
192.168.1.64/26 -> 192.168.1.65 - 192.168.1.126
192.168.1.128/26 -> 192.168.1.129 - 192.168.1.190
192.168.1.192/26 -> 192.168.1.193 - 192.168.1.254

CIDR   SubnetMask   No_OF_Subnest     No_Of_Host
/24  255.255.255.0    1               254 (host)
/25  255.255.255.128  2               126 (host)
/26  255.255.255.192  4               62 (host)
/27  255.255.255.224  8               30 (host)
/28 (try to calulate for this by your own)
/29
/30
