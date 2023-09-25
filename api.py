import json
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

class PetCategories:
    def __init__(self):
        self.base_url = "http://91.210.171.73:8080/api/category/"

    def get_api_key(self, user: str, passwd: str) -> json:
        headers = {
            'username': user,
            'password': passwd,
        }
        res = requests.get(self.base_url + 'api/key', headers=headers)
        status = res.status_code
        result = ""

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_category(self, limit: json, offset: str = "") -> json:

        headers = {'limit': limit}
        filter = {'offset': offset}

        res = requests.get(self.base_url + 'api/category', headers=headers, params=filter)
        status = res.status_code
        result = ""

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def add_new_category(self, limit: json, name: str, category: str) -> json:
        data = MultipartEncoder(
            fields={
                'name': name,
                'category': category,
            })
        headers = {'limit': limit, 'Content-Type': data.content_type}

        res = requests.post(self.base_url + 'api/pet', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

    def get_category_of_pets(self, pet_id: json, category: str = "") -> json:

        headers = {'pet_id': pet_id}
        filter = {'category': category}

        res = requests.get(self.base_url + 'api/pat/{id}', headers=headers, params=filter)
        status = res.status_code
        result = ""

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result


    def update_categories_pet_info(self, id: json, name: str,
            photo_url: str, category: str, available: str) -> json:
        headers = {'id': id}
        data = {
            "name": name,
            "photo_url": photo_url,
            "category": category,
            "status": available
             }

        res = requests.put(self.base_url + 'api/pet/{id}/', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def delete_category(self, auth_key: json, pet_id: str) -> json:
        headers = {'auth_key': auth_key['key']}

        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)
        status = res.status_code
        result = ""

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key: json, filter: str = "") -> json:

        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url + 'api/pet', headers=headers, params=filter)
        status = res.status_code
        result = ""

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def add_new_pet(self, auth_key: json, name: str, category: str, pet_photo: str, status: str) -> json:

        data = MultipartEncoder(
        fields={
            'name': name,
            'category': category,
            'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
    headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

    res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
    status = res.status_code
    result = ""
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    print(result)
    return status, result

    def update_pet_info(self, auth_key: json, pet_id: str, name: str) -> json:

    headers = {'auth_key': auth_key['key']}
            data = {
                'name': name,
            '   pet_id': id,

                }

        res = requests.put(self.base_url + 'api/pet/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result


    def delete_pet(self, auth_key: json, pet_id: str) -> json:

    headers = {'auth_key': auth_key['key']}

    res = requests.delete(self.base_url + 'api/pet/' + pet_id, headers=headers)
    status = res.status_code
    result = ""
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    return status, result