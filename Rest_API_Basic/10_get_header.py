import requests
import json

headerdata={'T1':'first header','T2':'second header'}

response=requests.get('https://httpbin.org/get',headers=headerdata)
print(response.text)
