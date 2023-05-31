from lib.base_case import BaseCase


class TestSmokeDisp(BaseCase):
    def test_get_token(self, get_token):
        assert get_token.status_code == 200, f"Response is not correct"

    def test_get_patient_info(self, get_patient_info):
        assert get_patient_info.status_code == 200, 'Wrong response status code'

    def test_get_mo_info_extended_d(self, get_mo_info_extended_d):
        assert get_mo_info_extended_d.status_code == 200, 'Wrong response status code'

    def test_service_post_specs_info_d(self, get_service_post_specs_info_d):
        assert get_service_post_specs_info_d.status_code == 200, 'Wrong response status code'

    def test_get_mo_resource_info_d(self, get_mo_resource_info_d):
        assert get_mo_resource_info_d.status_code == 200, 'Wrong response status code'

    def test_get_schedule_info_d(self, get_schedule_info_d):
        assert get_schedule_info_d.status_code == 200, 'Wrong response status code'

    def test_create_appointment_d(self, create_appointment_d):
        assert create_appointment_d.status_code == 200, 'Wrong response status code'
