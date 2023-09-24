import unittest
import requests


class TestTokenGeneration(unittest.TestCase):
    def test_get_token(self):
        token = self.get_access_token()

        self.assertTrue(token)
        self.assertTrue(isinstance(token, str))

    def get_access_token(self):
        url = '"http://91.210.171.73:8080/api/token/"'
        data = {
            'grant_type': 'client_credentials',
            'client_id': 'your_client_id',
            'client_secret': 'your_client_secret'
        }
        response = requests.post(url, data=data)

        if response.status_code == 200:
            return response.json().get('access_token')
        else:
            raise Exception(f"Failed to get access token. Status code: {response.status_code}")


if __name__ == '__main__':
    unittest.main()