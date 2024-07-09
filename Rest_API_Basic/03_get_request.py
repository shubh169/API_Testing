import requests
import jsonpath
import json
from pprint import pprint

# URL.
url="https://reqres.in/api/users?page=2"

# Send GET request.
response=requests.get(url)


# Validate status code.
# print(response.status_code)
assert response.status_code==200

# Display response.
print(response)
print(response.content)
print(response.headers)