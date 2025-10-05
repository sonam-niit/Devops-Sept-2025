# Network Interfaces How to check?

- ifconfig (shows network inreface, MAC Address, ip address)
- you can configure as well
- ifconfig eth0

- to run ifconfig: sudo apt install net-tool (install this)

- Alternative of this command 
- ip addr show (ip a)


## Network Statistics

- sudo apt install net-tools
- netstat -a (all networks)

## Iptables

- which is haelping you to create firewall rule for the system
- List available rules: sudo iptables -L -v -n --line-numbers

- may be you can see Input, Forward and Output with blank means no rule.

- to create one rule:
- sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT (Allow SSH Protocol)
- sudo iptables -A INPUT -s 192.168.1.100 -j DROP (Block some IP)

- sudo iptables -L -v -n --line-numbers (check rules)

- Remove rule
- sudo iptables -D INPUT 1 (run this twice so it will delete both rules)

**INPUT**
- handle incoming traffic for your local system

**FORWARD Chain**
- Handling traffic passing through your system to another network

**OUTPUT Chain**
- Handles all Outgoing Traffic actually orginating from your system

## Firewalld

- Iptables : manage packet level transmission
- firewalld : higher level firewall management
- configure at zone level 

- sudo apt update && sudo apt install firewalld

- sudo systemctl enable firewalld
- sudo systemctl start firewalld
- sudo systemctl status firewalld
- firewall-cmd --state

- you can run all the commands mentioned in your presentation

## UFW (ubuntu firewall)

- sudo apt install ufw -y
- sudo ufw enable
- sudo ufw allow 22/tcp
- sudo ufw allow 80/tcp
- sudo ufw deny from 192.168.1.100
- sudo ufw status numbered

- sudo ufw delete deny from 192.168.1.100
- sudo ufw disable
- sudo ufw status




