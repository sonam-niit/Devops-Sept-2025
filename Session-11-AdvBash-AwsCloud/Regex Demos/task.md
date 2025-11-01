### 5 min task

- write a code to take IP from user
- create regex to validate IP address
- if valid then print valid else print Invalid

```bash
#!/bin/bash

read -rp "Enter IP" ip

pattern='^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$'
# pattern='^([0-9]{1,3}\.){3}[0-9]{1,3}$'

if [[ $ip =~ $pattern ]]; then
    echo "Valid"
else 
    echo "Invalid"
fi

```

### Match 8 digits in a row

```bash
pattern='[0-9]{8}'
# write code accordingly
```

**Practice Task** 
### Match Single a followed by 0 or more b, followed by c

- ac
- abc
- abbbbbc

- Incorrect
- abba
- aabc
- abbbac 

