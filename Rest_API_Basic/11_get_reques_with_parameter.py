import requests


param={'name':'shubham','city':'noida','mobile':'7355435764'}


response=requests.get('https://httpbin.org/get',params=param)
print(response.text)
