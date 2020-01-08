import json
import requests

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/updates/"


def get_list(id=None):
    data = json.dumps({})
    if id is not None:
        data = json.dumps({'id': id})
    r = requests.get(BASE_URL+ENDPOINT, data=data)
    if r.status_code != 404:
        print('probably good sign')
    data = r.json()
    # print(type(json.dumps(data)))
    # data = json.dumps({'id':id})
    # for obj in data:
    #     if obj['id'] == 1:
    #         r = requests.get(BASE_URL+ENDPOINT+str(obj['id']))
    #         print(r.json())
    return data


def create_update():
    new_data = {
        'user': 1,
        'content': 'My last update'
    }

    r = requests.post(BASE_URL+ENDPOINT, data=new_data)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text


def do_obj_update():
    new_data = {
        'id': 3,
        'content': 'other more cool  update'
    }

    # r = requests.put(BASE_URL+ENDPOINT+"1/", data=new_data)
    # r = requests.put(BASE_URL+ENDPOINT+"1/", data=json.dumps(new_data))
    r = requests.put(BASE_URL+ENDPOINT, data=json.dumps(new_data))
    print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text


def do_obj_delete():
    new_data = {
        'id': 3
    }

    # r = requests.put(BASE_URL+ENDPOINT+"1/", data=new_data)
    # r = requests.delete(BASE_URL+ENDPOINT+"1/")
    r = requests.delete(BASE_URL+ENDPOINT, data=json.dumps(new_data))
    print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text


print(get_list())
# print(create_update())
# print(do_obj_update())
# print(do_obj_delete())
