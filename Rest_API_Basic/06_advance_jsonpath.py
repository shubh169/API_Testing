import requests
import jsonpath
import json


url="https://reqres.in/api/users?page=2"

response=requests.get(url)
dict_format=response.json()
# response_json=json.loads(response.text)
# print(response_json)
print(dict_format)
"""Data store in json format."""
pretty_json_format=json.dumps(dict_format,indent=4)
with open("result.txt",'w') as data_file:
    data_file.write(pretty_json_format)

"""Using dict_format.get('data', []) with an empty list as the default value is a common practice to ensure that the variable users is 
always assigned a list, even if the key 'data' is not present in the dictionary dict_format. 
This helps prevent potential errors and makes the code more robust."""

users = dict_format.get('data', [])
print("\nList of users:")
for user in users:
    print(f"ID: {user['id']}, Name: {user['first_name']} {user['last_name']}, Email: {user['email']},Avatar:{user['avatar']}")


# Fetch value using jsonpath.
# for i in range(0,6):
#     first_name = jsonpath.jsonpath(json_format, f"data[{i}].first_name")
#     print(first_name[0])

# support=jsonpath.jsonpath(json_format,'support.text')
# print(support[0])
# for i in range(0,6):
#     avatar=jsonpath.jsonpath(json_format,f'data[{i}].avatar')
#     print(avatar[0])
