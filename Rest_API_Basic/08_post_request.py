import requests
import json
import jsonpath

url="https://reqres.in/api/users"

with open("data.txt","r") as df:
    data=df.read()

json_data=json.loads(data)

response=requests.post(url,json_data)

# Validate response code
assert response.status_code==201


# Header data
print(response.content.decode())
print(response.headers.values())


# Response data to parse into json format.
response_json_format=json.loads(response.text)
print(response_json_format.get('id'))


# print(jsonpath.jsonpath(response_json_format,'id'))





