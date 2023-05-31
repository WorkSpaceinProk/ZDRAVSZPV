from lib.base_case import BaseCase

class TestSmokeVaccin(BaseCase):
    def test_get_token(self, get_token):

        assert get_token.status_code == 200, f"Response is not correct"

    def test_get_patient_info(self, get_patient_info):

        assert get_patient_info.status_code == 200, 'Wrong response status code'

    def test_get_mo_info_extended_v(self, get_mo_info_extended_v):

        assert get_mo_info_extended_v.status_code == 200, 'Wrong response status code'

    def test_service_post_specs_info_v(self, get_service_post_specs_info_v):

        assert get_service_post_specs_info_v.status_code == 200, 'Wrong response status code'

    def test_get_mo_resource_info_v(self, get_mo_resource_info_v):

        assert get_mo_resource_info_v.status_code == 200, 'Wrong response status code'

    def test_get_schedule_info_v(self, get_schedule_info_v):

        assert get_schedule_info_v.status_code == 200, 'Wrong response status code'

    def test_create_appointment_v(self, create_appointment_v):

        assert create_appointment_v.status_code == 200, 'Wrong response status code'