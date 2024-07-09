import pytest
import requests
import json
from pprint import pprint

def test_add_student():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails"
    with open("D:\\shubham\\API_Testing\\StudentManagementSystem\\student_data.txt", 'r') as data:
        dict_data = json.loads(data.read())
    post_response = requests.post(API_URL, json=dict_data)
    print(post_response.text)

def test_update_student_data():
    student_id = 10292327  # Replace with the actual student ID you want to update
    API_URL = f"https://thetestingworldapi.com/api/studentsDetails/{student_id}"
    with open("D:\\shubham\\API_Testing\\StudentManagementSystem\\student_data.txt", 'r') as data:
        dict_data = json.loads(data.read())
    update_response = requests.put(API_URL, json=dict_data)
    assert update_response.status_code == 200  # Assuming 200 means successful update
    print(update_response.text)

def test_delete_student_data():
    student_id = 10292348  # Replace with the actual student ID you want to delete
    API_URL = f"https://thetestingworldapi.com/api/studentsDetails/{student_id}"
    delete_response = requests.delete(API_URL)
    pprint(delete_response.text)

def test_fetch_student_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails"
    get_response = requests.get(API_URL)
    dict_format = json.loads(get_response.text)
    # print(get_response.text)
    filtered_data = [{'id': d['id'], 'first_name': d['first_name']} for d in dict_format]
    pprint(filtered_data)
