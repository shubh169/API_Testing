import requests
import jsonpath
import json


# URL.
url="https://reqres.in/api/users?page=2"

# Send GET request.
response=requests.get(url)

# parse response to dict format.
dict_format=json.loads(response.text)
print(dict_format)

# print(dict_format['page'])

# Fetch value using jsonpath.
pages=jsonpath.jsonpath(dict_format,"data")
# Gives values in list format.
print(pages)

# print(pages[0])
#
# assert pages[0]==2