count=1
while [ $count -le 5 ]
do
    echo "Count: $count"
    ((count++))
done

##Until Loop
num=1
until [ $num -gt 5 ]
do
    echo "Number: $num"
    ((num++))
done

