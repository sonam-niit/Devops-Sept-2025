#!/bin/bash
add() {
    local num1=$1
    local num2=$2
    local sum=$((num1+num2))
    echo "the Sum of $num1 and $num2 is $sum"
}
sub() {
    local num1=$1
    local num2=$2
    local sub=$((num1-num2))
    echo "the diffrence of $num1 and $num2 is $sub"
}

# Call function
add 5 3 # 5 and 3 are arguments
sub 10 8 