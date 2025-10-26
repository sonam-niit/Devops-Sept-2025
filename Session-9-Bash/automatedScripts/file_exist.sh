#!/bin/bash
FILE="backup.txt"

if [ -f "$FILE" ]; then
    echo "$FILE exist"
else
    echo "$FILE not exist"
fi


