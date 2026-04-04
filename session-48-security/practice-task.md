# implement ALB using terraform

- creat2 2 instance resporces
    - count will be 2
    - give seperate use2data for both instance
    - instance name you can use like instance-1, instance-2 based on index

- create target group
    - attach these instances to target group

- create Load Balancer
    - attach target group to this load balancer

- also output will be loadbalancer DNS value