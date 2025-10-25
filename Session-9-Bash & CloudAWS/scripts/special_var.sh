#Special Variables

# $0 indicates script name (file name)
echo "File Name: $0"
# $1, $2, $3.... arguments which is passed to the script
echo "Argument 1: $1"
echo "Argument 2: $2"
echo "Argument 3: $3"

# $# no of arguments
echo "No of arguments: $#"

# $@ all arguments gives as list
echo "All Arguments $@"

# $$ Process Id which is used to execute that scripts
echo "Process Id: $$"

# $? Exit Status 0-Success, 1-Some Error
echo "Exit Status: $?"

# To run above script use below command
# ./special_var test xyz 111 567 file.txt
# Passed 5 Arguments to this


