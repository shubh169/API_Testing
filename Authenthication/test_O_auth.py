import requests
import json


def test_with_O_auth():
    id=10292748
    url = f"https://thetestingworldapi.com/api/studentsDetails/{id}"
    fetch_detail = requests.get(url)
    print(fetch_detail.text)