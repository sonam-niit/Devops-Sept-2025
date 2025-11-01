# AWS : Amazon Web Services

- Provide infrastructures, services, storage

[AWS Console](https://aws.amazon.com/console/)

## What is EC2 - Elastic Compute Cloud

- It is a service provided by AWS which provides service for creating VM (virtual machines) which is called an instance.

- If i want to deploy my application on linux machine I can create linux instance.

- instance means creating VM / server

**How to create?**

- Before start creating instance check region
- select region
![region selection](/images/region.png)

1. go to aws console, login and search for EC2 and click on it.
2. you can see below type of screen.
![EC2 Dashboard](/images/ec21.png)
3. click on Launch Instance Button.
4. Give name of Instance
![Name of Instance](/images/step1.png)
5. select Image (machine OS) like ubuntu, linux
![select OS](/images/step2.png)
6. instance type t2.micro (free ware)
![Instance Type](/images/step3.png)
7. Key pair is required to connect from Local machine to this live server. click on create new key pair
![Key-Pair](/images/step4.png)
8. once you create that, it will download to your system as well that you need to keep it secretly.
9. select that created key pair
![Key-Pair](/images/step5.png)
10. this same key pair you can use for multiple servers as well.
11. Network settings very important to configure firewall of your server.
12. whatever ports and protocol you want to access you can configure here.
13. click on edit button.
![Network Settings](/images/step6.png)
14. Keep the VPC default as shown
![VPC](/images/step7.png)
15. Firewall Settings
![Firewall](/images/step8.png)
16. SSH rule keep as it is.
![SSH](/images/step9.png)
17. If you want to add more click on *Add Security Group Rule* 
18. Let's add HTTP Rule
![HTTP Rule](/images/step10.png)
19. Add One more Rule
![Port 8080 for Jenkins](/images/step11.png)
20. Keep the storage size 8GB only
![Storage Size](/images/step12.png)
21. click on Launch Instance
22. It will create your Instance.
![Success](/images/success.png)

- once instance created then we want to connect with this instance from my local system.

![Check all instance](/images/instances.png)
- click on instance Id
![instance-details](/images/instance-details.png)
- Here you can see your instance public Ip address and DNS - Domain Name service.

- here you can see the connect option
- click on that 
![connect-vm](/images/connect-vm.png)
- again click on bottom right connect button

![connect-done](/images/connect-done.png)

- run below command to simply deploy nginx

```bash
sudo apt update
sudo apt install nginx -y
sudo systemctl start nginx
```

- try to open your public Ip or public DNS in browser you can see the default page is deployed successfully.

- final result in browser
![deployed Nginx](/images/deploy-nginx.png)

- make sure you access using http://<public_ip>
- if its https it won't work.