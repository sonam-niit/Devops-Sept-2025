import requests

BASE_URL='https://jsonplaceholder.typicode.com/users'

data= {
    "name": "Sonam Soni",
    "username": "soni123",
    "email": "sonam.skills@pw.live"
  }
response = requests.post(BASE_URL,json=data) # trigger post method with data

print("Entire response: ",response.json())
print("Status Code: ",response.status_code)

response = requests.delete(BASE_URL+"/2") # delete user with id=2
print("----Response after delete ---")
print("Entire response: ",response.json())
print("Status Code: ",response.status_code)