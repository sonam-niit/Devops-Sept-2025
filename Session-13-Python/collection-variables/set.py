my_set={1,2,3,2,4,2,5} # its unordered not maintaining any index
print(my_set)# you cannot see duplicates
my_set.add(10)
print("After add: ",my_set)
my_set.remove(10) # if element not present it will throw an error
print(my_set)

my_set.discard(35)
# if element present remove, if not then leave it, not throwing any error

my_set.pop() # it will remove random element
print(my_set)


