import json

my_dict='{"name":"shubham","age":27,"city":["Noida","Muzaffarnagar"],"address":{"house no":"CC 49","city":"Ghaziabad","contact Number":{"Mobile":"7355435764","landline":"0123-789"} }}'


json_result=json.loads(my_dict)
print(json_result['city'])
