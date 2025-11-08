my_list=[1,2,3,4,5,6,7,8]
print(my_list)
print("Element at index 1: ", my_list[1])
my_list.append(9) # add new item
my_list[2]=33 # update item
print("after update: ",my_list)
my_list.insert(0,20)
print("after insertion: ",my_list)
my_list.pop() # remove last element
my_list.pop(3) # remove element from index 3

print("after removal: ",my_list)

length= len(my_list)
print("Length: ", length)