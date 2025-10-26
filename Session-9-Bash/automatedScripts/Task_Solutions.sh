## Take two numbers and add them (Simple Calculator)
#!/bin/bash
# Take two numbers as input
read -p "Enter first number: " num1
read -p "Enter second number: " num2

# Calculate sum
sum=$((num1 + num2))

# Display the sum
echo "The sum of $num1 and $num2 is: $sum"

## Check if a number is even or odd

if (( sum % 2 == 0 )); then
    echo "The number is even."
else
    echo "The number is odd."
fi