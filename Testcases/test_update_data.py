import requests
import json
import pytest

url="https://reqres.in/api/users/2"


@pytest.mark.smoke
def test_update_user_data():
    with open("C:\\Users\\kumarshu\\Downloads\\data.txt","r") as df:
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










