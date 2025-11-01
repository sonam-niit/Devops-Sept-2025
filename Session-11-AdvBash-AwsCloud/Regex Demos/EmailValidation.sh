#!/bin/bash
read -rp "Enter EmailId: " email
pattern='^[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$'
if [[ $email =~ $pattern ]]; then
    echo "It is valid email ID"
else
    echo "Not valid Email ID"
fi

# [A-Za-z0-9._-]+ = starting part of email = sonam-soni.12
# @ = @ is fixed
# [A-Za-z0-9.-]+ = outlook
# \. = . is fixed
# [A-Za-z]{2,4} = .in, .com , .org (min 2 max 4)
# $ is end of pattern

