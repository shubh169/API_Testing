import requests
import json


url="https://reqres.in/api/users/2"

with open("data.txt","r") as df:
    data=df.read()

# Convert data into dict format.
json_data=json.loads(data)

# Make Put request on server.
response=requests.put(url,json_data)

# Validate response code
assert response.status_code==200

# Response data to parse into dict format.
response_json=json.loads(response.text)
print(response.text)
print(response_json.get('updatedAt'))










