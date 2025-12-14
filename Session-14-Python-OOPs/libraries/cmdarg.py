import sys

print("Script name: ", sys.argv[0])
print("All Arguments: ", sys.argv[1:])

# How to run
# python3 cmdarg.py sonam 12 true hello.txt
# here i have passed 4 arguments

#iterate using loop
for i in sys.argv[1:]:
    print(i)