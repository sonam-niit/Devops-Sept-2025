#!/bin/bash
current_time=$(date +"%Y%m%d_%H%M%S") # %sign for format

# Repeat below step 5 times do to done steps needs to repeat
# for is the loop
for i in {1..5}
do 
    filename="File_${current_time}_$i.txt" # giving file name unique
    touch "$filename" # creating file

    echo "this is file number $i created on $current_time." > "$filename"
    # $ is used to access variables name
    echo "Created: $filename"

done
