#  This is a 3rd party app we use this for where to send a requent and recieve a response from frontend

# pyrefly: ignore [missing-import]
from wsgiref import headers
import requests
import json


URL = "http://127.0.0.1:8000/studentapi/"


def get_data(id = None):
    Data = {}
    if id is not None:
        data ={'id':id}
        json_data = json.dumps(data)
        r = requests.get(url=URL, data=json_data)
        data = r.json()
        print(data)

get_data()


# ====================>> POST DATA INTO DATABASE
def post_data():
    data = {'name':'John', 'roll':101, 'city':'New York'}  #python dict
    json_data = json.dumps(data)                            # convert python dict to json data
    r = requests.post(url=URL, data=json_data)              # send json data to the API
    data = r.json()                                         # convert json data to python dict
    print(data)                                             # print python dict
# Goto >>> views.py >>> and write code for POST data

# post_data()



# ====================>> Update DATA INTO DATABASE
def update_data():
    data = { 'id':5,'name':'John', 'roll':106, 'city':'New Jersy'}  #python dict

    json_data = json.dumps(data)                            # convert python dict to json data
    r = requests.put(url=URL, data=json_data)               # send json data to the API
    data = r.json()                                         # convert json data to python dict
    print(data) 

# update_data()




# ====================>> delete DATA FROM DATABASE
def delete_data():
    data = { 'id':4,}  #python dict

    headers = {'content-type': 'appliction/json'}

    json_data = json.dumps(data)                            # convert python dict to json data
    r = requests.delete(url=URL, data=json_data, headers=headers)            # send json data to the API
    data = r.json()                                         # convert json data to python dict
    print(data) 

# delete_data()