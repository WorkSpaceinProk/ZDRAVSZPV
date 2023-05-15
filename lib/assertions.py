import requests
from requests import Response
import json

class Assertions():
    @staticmethod
    def _send(url:str, data:dict, headers:dict, cookies:dict, method: str):
        url = f"http://r78-test.zdrav.netrika.ru{url}"

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        if method == 'GET':
            response = requests.get(url, params=data, headers=headers, cookies=cookies)
        elif method == 'POST':
            response = requests.post(url, data=data, headers=headers, cookies=cookies)

        else:
            raise Exception(f"Bad HTTP method '{method}' was received")

        return response


