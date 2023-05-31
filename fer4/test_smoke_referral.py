import requests
from lib.base_case import BaseCase
from lxml import etree as et
from lxml.builder import ElementMaker


class TestSmokeReferral(BaseCase):
    def test_get_token(self, get_token):
        assert get_token.status_code == 200, f"Response is not correct"

    def test_get_patient_info_referral(self, get_patient_info_referral):
        assert get_patient_info_referral.status_code == 200, 'Wrong response status code'

    def test_get_mo_resource_info_referral(self, get_mo_resource_info_referral):
        assert get_mo_resource_info_referral.status_code == 200, 'Wrong response status code'

    def test_get_schedule_info_referral(self, get_schedule_info_referral):
        assert get_schedule_info_referral.status_code == 200, 'Wrong response status code'

    def test_create_appointment_referral(self, create_appointment_referral):
        assert create_appointment_referral.status_code == 200, 'Wrong response status code'
