import re
with open("app.log") as file:
    for line in file:
        if "ERROR" in line or "CRITICAL" in line:
            print(line.strip())
    
print("-------Print using pattern match------")        
# Same above program you an do using regex
pattern=re.compile(r'.* - (ERROR|CRITICAL) - *')
with open("app.log") as f:
    for line in f:
        if pattern.match(line):
            print(line.strip())