"""
Request chaining refers to the process of making multiple API requests sequentially,
where each request depends on the data returned from the previous one
"""

import requests
import json


def test_add_new_student():
    url="https://thetestingworldapi.com/api/studentsDetails"
    with open('student_data.txt','r') as data:
        student_data=data.read()

    dict_format=json.loads(student_data)
    response=requests.post(url,json=dict_format)
    response_in_dict=json.loads(response.text)
    id=response_in_dict.get('id')

def test_get_student_detail():
    url = f"https://thetestingworldapi.com/api/studentsDetails/{id}"
    fetch_detail=requests.get(url)
    if fetch_detail.status_code == 200:
        print("Complete Details:", fetch_detail.text)
    else:
        print(f"Error fetching details: {fetch_detail.status_code}")
        print(fetch_detail.text)