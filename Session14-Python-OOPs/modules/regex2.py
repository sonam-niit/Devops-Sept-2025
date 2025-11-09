import re

text = "contact me at dev@pw.live or admin@pw.org or sonam.soni@pw.live"

pattern= r"[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,4}"

emails= re.findall(pattern,text)

print(emails)