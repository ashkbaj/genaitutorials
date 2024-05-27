print('Testing')

import requests

url = "https://reqres.in/api/users"

response = requests.get(url)

print(response.text)

url1 = "https://reqres.in/api/users"

payload1 = {
    "name": "morpheus",
    "job": "leader"
}

response1 = requests.post(url=url1, json=payload1)

print(response1.text)