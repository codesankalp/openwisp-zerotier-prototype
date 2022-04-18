import requests


class RequestFactory:

    api_endpoints = {
        'create_network': '/network',
        'get_network': '/network/{id}',
        'update_network': '/network/{id}',
        'delete_network': '/network/{id}',
    }

    def create_network(self, host):
        url = host + self.api_endpoints.get('create_network')
        response = requests.post(url, timeout=5)
        return response.json()


class ZerotierRestAPI:
    def __init__(self, host):
        self.host = host  # https://my.zerotier.com
        self.request = RequestFactory()

    def create_network(self):
        return self.request.create_network(self.host)
