#Array Operations
nums=(1 2 3 4 5)
echo "All Elements: ${nums[@]}"
#Append
nums+=(6)
echo "After append: ${nums[@]}"
#Append Multiple
nums+=(7 8 9 10)
echo "After append Multiple: ${nums[@]}"
# Insert at specific Index
nums[3]=20
echo "After Insert ${nums[@]}" #Replace
# delete
unset nums[3]
echo "After Delete ${nums[@]}"
# insert number between 3 & 4
index=3
nums=("${nums[@]:0:$index}" 4 "${nums[@]:$index}")
echo "After Insert ${nums[@]}"