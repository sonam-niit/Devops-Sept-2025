#!/bin/bash
# If Statement
num=10
if [ $num -gt 5 ]
then
    echo "Number is Greater than 5"
fi 

#IF ELSE
name="Test"
if [ $name = "Sonam" ]
then
    echo "Hello Sonam"
else 
    echo "Hello Guest"
fi 

# Logical operator
echo "Enter your age"
read age
if [ $age -ge 18 ] && [ $age -lt 60 ]
# (and to check both conditions)
then 
    echo "Eligible Adult"
fi

echo "Enter your user details"
read user
if [ $user = "admin" ] || [ $user = "root" ]
# to check any one condition)
then 
    echo "you have admin access"
fi