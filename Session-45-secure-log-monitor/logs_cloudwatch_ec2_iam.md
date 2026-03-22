# Add logs to cloudwatch using Agent 

- we are using amazom-cloudwatch-agent 
[Documentation](https://github.com/aws/amazon-cloudwatch-agent?tab=readme-ov-file)

# step 1: create EC2 instance

- create aws linux instance

# step 2 create Role: EC2-Cloudwatch-Role

- IAM -> Roles -> Create Role
- Service EC2 -> attach policy (CloudWatchAgentServcerPolicy)
- create

# attach this role to ec2

- EC2 -> select -> action -> security -> modify the role
- attach 

# Connect with EC2

- install amazon-cloudwatch-agent

```bash
sudo yum install amazon-cloudwatch-agent

sudo mkdir /var/log/myapp
sudo touch /var/log/myapp/app.log
# generate Simple Log
echo "Test Log" | sudo tee -a /var/log/myapp/app.log
cat /var/log/myapp/app.log # verify

# configuration for agent to collect log
sudo nano  /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json
```
- add below code

```json
{
    "logs": {
        "logs_collected": {
            "files": {
                "collect_list": [
                    {
                        "file_path": "/var/log/myapp/app.log",
                        "log_group_name": "/demo/ec2/myapp",
                        "log_stream_name": "{instance_id}"
                    }
                ]
            }
        }
    }
}
```
- save and verify

```bash
-cat /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json

# Validate
python3 -m json.tool /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json

# start agent
sudo  /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl \
-a start \
-c file:/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json \
-m ec2

# check status
amazon-cloudwatch-agent-ctl -a status

# Generate Some Logs 
echo "FINAL SUCCESS TEST $(date)" | sudo tee -a /var/log/myapp/app.log 

# check CLoudwatch
# Log Management -> Loggroups -> LogStream
# Check your logs genearted
# also you can try to send some more logs and refresh in cloudwatch

# incase configuration not loaded or you are changing them stop the agent and run it again
amazon-cloudwatch-agent-ctl -a stop

# start agent again
sudo  /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl \
-a start \
-c file:/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json \
-m ec2
```

