#!usr/bin/python3

import requests
import json

API_ENDPOINT = "http://172.20.10.13:8080/postjson"



#data = '{"first_name": "Guido", "last_name": "Rossum", "titles": ["BDFL", "Developer"]}'

#data = "{'name' : ['Bryan', 'Sana', 'Bijan', 'Troy', 'Meredith', 'Arash', 'Ramesh', 'Ramin', 'Hemanth'],'gender' : ['male', 'female', 'male', 'male', 'female', 'male', 'female', 'male', 'male'],'age' : [0, 0, 24, 0, 25, 0, 24, 0, 0]}"

toSend = [[1, 3, 2], [1, 2, 1], [1, 1, 1], [1, 0, 0], [1, 1, 7], [1, 2, 7], [1, 3, 6]]

data = json.dumps(toSend)

r = requests.post (url = API_ENDPOINT, data = data)

print(r.text)
