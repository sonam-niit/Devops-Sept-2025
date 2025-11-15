import requests

BASE_URL='https://jsonplaceholder.typicode.com/users/1'
response = requests.get(BASE_URL) # trigger get method

data = response.json() # convert repsonse into json

print('Name: ', data['name'])
print('UserName: ', data['username'])
print('Address: ', data['address']['street'],
      data['address']['suite'],
      data['address']['city'])

# to run this program in windows
# setup venv: python -m venv myenv
# activate: myenv\Scripts\activate
# pip install requests
# python get-method.py 

# to run this program in Linux and mac
# setup venv: python3 -m venv myenv
# activate: source myenv/bin/activate
# pip install requests
# python3 get-method.py 