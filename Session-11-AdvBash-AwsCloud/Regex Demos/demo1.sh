#!/bin/bash
read -rp "Enter Something: " data
pattern='^[0-9]+$' # pattern you cna store in variable use ''
if [[ $data =~ $pattern ]]; then
    echo "It is an integer number"
else
    echo "Not an integer Number"
fi

# [[ ... ]] Advanced Test command
# powerful to test the patterns
# =~ cannot appear without [[ ]]

