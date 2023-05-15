import json
from json.decoder import JSONDecodeError
import requests

class TestAuthToken:
    #статичные данные
    def setup_method(self):

        self.headers = {'Server': 'nginx',
                        'Date': 'Tue, 21 Mar 2023 09:27:18 GMT',
                        'Transfer-Encoding': 'chunked',
                        'Connection': 'keep-alive',
                        'X-Request-ID': 'N3RID1ca5d4de309a05dc44ee86e18d021758'
        }

        response= requests.get("http://r78-test.zdrav.netrika.ru/authorization/api/newsession", self.headers)
        print(response.json()['content']['token'])
        assert response.status_code == 200, f"Response is not correct"

    # проверить формат ответа
    def test_get_session_token(self):

        response = requests.get("http://r78-test.zdrav.netrika.ru/authorization/api/newsession", self.headers)
        print(response.json()['content']['token'])

        assert response.status_code == 200, f"Response is not correct"
        assert "message" in response.json(), "There is no token in the response"
        print(response.text)

        try:
            parsed_response_text = response.json()
            print(parsed_response_text)
        except JSONDecodeError:
            print("Response is not a JSON format")

        print(f'***** {response.status_code}')
        print(f'***** {response.content}')

    # проверить ключ успешности запроса ("success"), извлекая его из ответа, преобразованного в объект
    def test_get_str_as_json(self):

        response = requests.get("http://r78-test.zdrav.netrika.ru/authorization/api/newsession", self.headers)

        str_as_json_format = '{"success": true}'
        obj = json.loads(str_as_json_format)
        print(obj['success'])
        assert response.status_code == 200, f"Response is not correct"

    # проверить наличие ключа "content" в ответе
    def test_print_content(self):

        response = requests.get("http://r78-test.zdrav.netrika.ru/authorization/api/newsession", self.headers)

        key = 'content'

        if key in response.json():
            print([key])

        else:
            print(f"Ключа {key} нет в ответе")
        assert response.status_code == 200, f"Response is not correct"

    #проверить наличие токена в ответе

    def test_get_token(self):

        response = requests.get(url="http://r78-test.zdrav.netrika.ru/authorization/api/newsession", headers=
                        {
                            'Server': 'nginx',
                                        'Date': 'Tue, 21 Mar 2023 09:27:18 GMT',
                                        'Transfer-Encoding': 'chunked',
                                        'Connection': 'keep-alive',
                                        'X-Request-ID': 'N3RID1ca5d4de309a05dc44ee86e18d021758'
                                        })

        print(response.json()['content']['token'])

        assert response.status_code == 200, f"Response is not correct"

        key = 'token'

        if key in response.json()['content']:
            print([key])

        else:
            print(f"Ключа {key} нет в ответе")
        assert response.status_code == 200, f"Response is not correct"



