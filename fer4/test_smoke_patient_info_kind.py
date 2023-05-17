import requests
from lib.base_case import BaseCase
from lxml import etree as et
from lxml.builder import ElementMaker

class TestFirstSmoke(BaseCase):
    def test_get_token(self, get_token):

        assert get_token.status_code == 200, f"Response is not correct"

    def test_get_patient_info(self, get_patient_info_referral):

        assert get_patient_info_referral.status_code == 200, 'Wrong response status code'

    def test_get_mo_resource_info(self, get_mo_info_extended):

        assert get_mo_info_extended.status_code == 200, 'Wrong response status code'

    def test_get_schedule_info(self, get_schedule_info_referral):

        assert get_schedule_info_referral.status_code == 200, 'Wrong response status code'

    def test_create_appointment(self, create_appointment):

        assert create_appointment.status_code == 200, 'Wrong response status code'
