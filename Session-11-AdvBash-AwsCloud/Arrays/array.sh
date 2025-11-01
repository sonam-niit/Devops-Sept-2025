names=("alex" "bob" "catty" "devid" "John")

echo "First Element: ${names[0]}" # 0 is the index
echo "Third Element: ${names[2]}"

# Access Length
echo "Total names: ${#names[@]}" # # for length
echo "All names: ${names[@]}" #@ to print all elements

# change value
names[1]="Sonam Soni"
echo "Updated: ${names[1]}"

# Print all using look
for name in "${names[@]}"; do
    echo $name
done