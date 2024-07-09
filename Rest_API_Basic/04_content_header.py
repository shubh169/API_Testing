import requests



# URL.
url="https://reqres.in/api/users?page=2"

# Send GET request.
response=requests.get(url)

print(response.headers)
print(response.headers.get('Date'))
print(response.headers.get('server'))

# Fetch cookies
print(response.cookies)

# Fetch elapsed time.
print(response.elapsed)