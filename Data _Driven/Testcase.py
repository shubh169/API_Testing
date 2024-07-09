import requests
import json
import openpyxl
from library import Comman_Testcases
from datetime import datetime


def add_multiple_students():
    url = "https://thetestingworldapi.com/api/studentsDetails"

    with open('student_data.json', 'r') as data:
        student_data = data.read()

    json_request = json.loads(student_data)

    obj = Comman_Testcases("test_data.xlsx", "Sheet1")
    row = obj.fetch_row_count()
    KeyList = obj.fetch_keys_name()

    for i in range(2, row + 1):
        update_json_request = obj.update_data(i, json_request.copy(), KeyList)
        response = requests.post(url, json=update_json_request)
        print(response.status_code)


if __name__ == "__main__":
    add_multiple_students()
