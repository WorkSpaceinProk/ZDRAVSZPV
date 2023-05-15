import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestReferralSetappointment(BaseCase):

    def setup_method(self):
        self.data = {
            'resourceType': 'Parameters',
            'parameter': [
                {
                    'name': 'organizationId',
                    'valueString': '1'
                },
                {
                    'name': 'patientId',
                    'valueString': '8928'
                },
                {
                    'name': 'slotId',
                    'valueString': 'bd00420f-7913-4069-92e5-b55c97d04904'
                },
                {
                    'name': 'referralId',
                    'valueString': '78214000000471'
                }
            ]
        }

        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': '01537F8F-B6F2-483D-9C10-A2A0D0DBAA01',
            'Version': '1.0.0'
        }

        response = requests.post(url="http://r78-test.zdrav.netrika.ru/hub3/api/appointment/referral/fhir/$setappointment", data=self.data)

        print(response.json())

        self.url = "http://r78-test.zdrav.netrika.ru/hub3/api/appointment/referral/fhir/$setappointment"

        # проверка работоспособности сервиса

    def test_referral_setappointment(self):

        response = requests.post(
            url=self.url,
            headers=self.headers, data=str(self.data).encode('utf-8'))

        Assertions.assert_json_value_by_name(
            response,
            self.data,
            "Response is not in JSON format"
        )
