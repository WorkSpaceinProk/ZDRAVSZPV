import pytest
import requests

@pytest.fixture
def get_token():
    headers = {'Server': 'nginx',
                    'Date': 'Tue, 21 Mar 2023 09:27:18 GMT',
                    'Transfer-Encoding': 'chunked',
                    'Connection': 'keep-alive',
                    'X-Request-ID': 'N3RID1ca5d4de309a05dc44ee86e18d021758'
                    }

    response = requests.get("http://r78-test.zdrav.netrika.ru/authorization/api/newsession", headers=headers)
    return response.json()
