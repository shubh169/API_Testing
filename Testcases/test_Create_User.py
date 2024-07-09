import requests
import json
import pytest

url = "https://reqres.in/api/users"
a = 100

@pytest.fixture(scope="module")
def start_exec():
    file_path = r"C:\Users\kumarshu\Downloads\data.txt"
    with open(file_path, 'r') as df:
        data = df.read()
    return data

# @pytest.mark.skipif(a > 10, reason="condition is satisfied.")
@pytest.mark.smoke
def test_create_new_user(start_exec):
    json_data = json.loads(start_exec)
    response = requests.post(url, json=json_data)
    # Validate response code
    assert response.status_code == 201
@pytest.mark.sanity
def test_create_other_user(start_exec):
    json_data = json.loads(start_exec)
    response = requests.post(url, json=json_data)
    # Response data to parse into json format.
    response_json_format = response.json()
    print(response_json_format.get('id'))

if __name__ == "__main__":
    pytest.main()
