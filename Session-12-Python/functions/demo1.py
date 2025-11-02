def greetings():
    print("Hello Everyone!")
    
def welcome(name):
    if name=='':
        print(f"Welcome Guest")
    else:
        print(f"Welcome {name}")
        
def add(num1,num2):
    return num1+num2

greetings() # call directly
welcome('')
welcome("Sonam Soni")
result = add(10,20) # catch return result
print("Result: ",result)
print("Result: ",add(3,4)) # call function directly from print