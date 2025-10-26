substitute() {
    echo "$1" | sed "s/$2/$3/g"
}

input="Hello World"
search="World"
replace="Bash"
result=$(substitute "$input" "$search" "$replace")
echo $result

echo $(substitute "Good Morning" "Morning" "Evening")

