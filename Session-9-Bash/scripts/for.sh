#!/bin/bash
for i in {1..5} # range
do
    echo "Number $i"
done

echo "Another Way of iteration"
for i in 2 4 6 8 10
do
    echo "Iteration $i"
done

## loop Through all files in current folder
for file in *.*
do
    echo "Processing $file"
done