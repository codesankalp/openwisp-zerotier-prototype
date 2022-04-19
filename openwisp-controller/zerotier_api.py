import requests
from django.core.exceptions import ValidationError


class ZeroTierAPI:

    api_endpoints = {
        'create_network': '/network',
        'get_network': '/network/{id}',
        'update_network': '/network/{id}',
        'delete_network': '/network/{id}',
    }

    def __init__(self, host, token) -> None:
        self.host = host
        self.url = f'https://{host}/api/v1'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        }

    def create_network(self, name):
        data = {
            'config': {
                'name': name,
                'private': True,
                'enableBroadcast': True,
            }
        }
        post_url = self.url + self.api_endpoints.get('create_network')
        try:
            r = requests.post(post_url, json=data, headers=self.headers, timeout=5)
            return r.json()
        except:
            raise ValidationError({'auth_token': ('Auth token is incorrect')})
