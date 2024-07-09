import requests
import json
from requests.auth import HTTPBasicAuth

def test_with_basic_auth():
    response=requests.get(url="https://api.github.com/user",auth=HTTPBasicAuth('abc','xyz'))
    print(response.text)