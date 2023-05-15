from requests import Response

class BaseCase:
    def get_headers (self, response: Response, headers_name):
        assert headers_name in response.headers, f'Cannot find headers with name {headers_name} in the last response'
        return response.headers[headers_name]

    def get_token (self, response: Response, token):
        assert token in response.json()['content'], f"Cannot find token in the last response"
        return response.json()['content']['token']

    def get_response_statuse_code (self, response: Response, response_status_code):
        assert response_status_code in response.status_code, f"Wrong response status code"
        return response.status_code

    def get_json_value (self, response: Response, message):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is {response.text}"
        assert message in response_as_dict, f"Response JSON doesn't have key{message}"
        return response_as_dict[message]





