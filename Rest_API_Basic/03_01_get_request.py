import requests
import json
import jsonpath
from pprint import pprint

# URL of the API endpoint
url = "https://reqres.in/api/users?page=2"

try:
    # Send a GET request to the specified URL.
    response = requests.get(url)

    # Raise an exception if the request was unsuccessful.
    response.raise_for_status()

    # Parse the response content as JSON.
    response_json =response.json()
    print(response_json)

#     # Pretty print the JSON response
#     pretty_response = json.dumps(response_json, indent=4)
#     print("Response JSON content:\n", pretty_response)
# #
# #     # Extract and print specific data using JSONPath or direct access.
# #     users = response_json.get('data', [])
# #
# #     print("\nList of users:")
# #     for user in users:
# #         print(f"ID: {user['id']}, Name: {user['first_name']} {user['last_name']}, Email: {user['email']}")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"Other error occurred: {err}")
