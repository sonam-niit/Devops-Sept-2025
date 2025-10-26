#!/bin/bash

string="Hello, World!"
echo ${string:7:5}
echo ${string:7:6}

message="This is my simple string"
replaced_string=${message//simple/complex}
echo $replaced_string

echo $string | awk '{gsub(/World/, "Sonam"); print}'

echo $string | sed 's/World/Guest/' # Replace one
echo $string | sed 's/World/Guest/g' # Replace All
# /s substitute String
# /g global replace all

sed -i 's/everyone/Everyone/g' test.txt
# Modify the file