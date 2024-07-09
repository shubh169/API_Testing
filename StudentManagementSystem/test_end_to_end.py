import requests
import json


def test_add_data():
    url="https://thetestingworldapi.com/api/studentsDetails"
    with open('student_data.txt','r') as data:
        student_data=data.read()

    dict_format=json.loads(student_data)
    response=requests.post(url,json=dict_format)
    response_in_dict=json.loads(response.text)
    id=response_in_dict.get('id')

# Add Technical Skills.
    url = "https://thetestingworldapi.com/api/technicalskills"
    with open('technical_skills.json', 'r') as data:
        tech_data = data.read()

    dict_format = json.loads(tech_data)
    dict_format['id']=id
    dict_format['st_id']=str(id)
    response = requests.post(url, json=dict_format)
    response_in_dict = json.loads(response.text)
    # print(response_in_dict)

# Add Address.
    url = "https://thetestingworldapi.com/api/addresses"
    with open('address_data.json', 'r') as data:
        address_data = data.read()

    dict_format = json.loads(address_data)
    dict_format['stId'] = str(id)
    response = requests.post(url, json=dict_format)
    response_in_dict = json.loads(response.text)
    # print(response_in_dict)

# Fetching complete details.
    url = f"https://thetestingworldapi.com/api/FinalStudentDetails/{id}"
    fetch_detail=requests.get(url)
    print(fetch_detail.text)
