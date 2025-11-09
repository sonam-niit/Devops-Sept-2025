import re

text="Hello World"
#check from start
pattern=r"Hello"
match = re.match(pattern,text)
if match:
    print("Text started with Hello")
else:
    print("Text is not started with hello")
    
# check in entire string    
search= re.search(r"World",text)
if search:
    print("text includes world")
else:
    print("text not includes world")