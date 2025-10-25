#!/bin/bash
my_name="Sonam Soni"
echo "My Name is $my_name"
echo "Enter your age"
read age # age is the variable where your entered value get stored
echo "I am $age years old"

## Arithmetic operations
a=10
b=20
sum=$((a+b)) # $(()) for Math
echo "Sum = $sum"

user="John Doe"
today=$(date +%Y/%m/%d_%H:%M:%S)

echo "Hello $user, today is $today"