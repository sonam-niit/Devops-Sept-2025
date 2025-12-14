# Creating Strings
str1 = 'Hello'
str2 = "World!"
str3 = '''
        This is multiline
        String
'''

print(str3)
print(f"{str1} {str2}") # f"string"

greeting= str1+" "+str2
print(greeting)

# Repeat String
print((str1+" ")*4)

# String Slicing
print(greeting[0:5]) # Hello
print(greeting[-6:]) # World!

# String length
print("Length: ",len(greeting))

# Upper case Lower Case
print(f"UpperCase: {greeting.upper()}")
print(f"LowerCase: {greeting.lower()}")

#Replace
print("Replace: ",str1.replace("H","W"))

# Split and join
statement="my name is sonam soni and I am a content creator"
words=statement.split()
print(words)# list of words
print("-".join(words))

# Check strings starts with ends with
print("Python".startswith("Py"))
print("Python".endswith("on"))