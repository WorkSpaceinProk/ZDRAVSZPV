import json
from json import JSONDecodeError
import requests

class TestSearchSlots:

    def setup_method(self):
        self.data = {
            'resourceType': 'Parameters',
            'parameter': [
                {
                    'name': 'organizationId',
                    'valueString': '1'
                },
                {
                    'name': 'referralId',
                    'valueString': '78214000000471'
                },
                {
                    'name': 'patientSurname',
                    'valueString': 'Ящеркин'
                }
            ]
        }

        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': '01537F8F-B6F2-483D-9C10-A2A0D0DBAA01',
            'Version': '1.0.0'
        }
        self.url = 'http://r78-test.zdrav.netrika.ru/hub3/api/appointment/referral/fhir/$searchslots'

    def test_searchslots_resource_type(self):
        response = requests.post(url=self.url, headers=self.headers, data=str(self.data).encode('utf-8'))
        string_as_json_format = response.text
        obj = json.loads(string_as_json_format)
        print(obj['resourceType'])

        key = 'resourceType'

        if key in response.text:
                print(obj[key])

        else:
                print(f"There is no {key} in the response")

    def test_searchslots_entry(self):
        response = requests.post(url=self.url, headers=self.headers, data=str(self.data).encode('utf-8'))
        string_as_json_format = response.text
        obj = json.loads(string_as_json_format)

        key = 'entry'

        if key in response.text:
            print(json.dumps(obj[key], indent=4, sort_keys=True))

        else:
            print(f"There is no {key} in the response")


    def test_searchslots_keyinfo(self):

        response = requests.post(url=self.url, headers=self.headers, data=str(self.data).encode('utf-8'))
        string_as_json_format = response.content
        obj = json.loads(string_as_json_format)

        key = 'fullUrl'

        if key in str(['entry'][0]):
            print(obj[key])

        else:
            print(f"There is no {key} in the response")

