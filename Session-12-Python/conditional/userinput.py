data= input("Enter Something: ")

if data.isdigit(): # isdigit() is inbuilt fun to check input is whole number
    print("It is Number")
    print(type(data)) # by default all inputs in string
    num= int(data) # convert string to number
    print(num, "datatype: ",type(num))
else:
    print("Not a Number")