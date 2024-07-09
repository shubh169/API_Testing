import requests
import pytest

# URL.
url="https://reqres.in/api/users?page=2"

@pytest.mark.sanity
def test_get_data():
    response=requests.get(url)

    # Validate status code.
    assert response.status_code==200
    # Display response.
    print(response)
    print(response.content)
    print(response.headers)