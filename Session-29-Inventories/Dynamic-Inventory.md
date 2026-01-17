# Dynamic Inventory

- Dynamic Inventory automatically fetches hosts from cloud providers or APIs using static inventory.

- The aws_ec2 dynamic inventory plugin makes API calls to AWS to get a list of inventory hosts from Amazon Web Services EC2 in the run time. It gives the EC2 instance details dynamically to manage the AWS infrastructure.

- for Authentication Let's Do AWS CLI configuration

[Documentation for AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" # Download
sudo apt install unzip # install unzip
unzip awscliv2.zip # unzip the folder
sudo ./aws/install # this will install
aws --version # verify installation
```

- Now go to AWS Console --> Login
- Search For IAM service
- click on the same
- click on Users 
- create User
![Create User](images/create-user.png)
- click on next
![Set Permissions](images/set-permissions.png)
- click on next and create User
![Create User](images/create-user.png)

![User Created](images/created-user.png)

- click on your Username and You can see below Screen
![Next Option](images/next.png)

- click create Access Key

![Create Access Keys](images/create-keys.png)

- click on Next

- Give Description  and click on next

![Add Description Tag](images/desc-tag.png)

- click on create Access Keys
![Access Keys](images/created-keys.png)

- make Sure you download CSV file and Copy Keys
- Because its not visible again once you click on done

## Now Configure AWS CLI in my System

- open wsl

```bash
aws configure
```
![AWS Configure](images/aws-config.png)

### Verify

```bash
aws configure list
aws sts get-caller-identity # You get Account Details
```
