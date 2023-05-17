from lib.base_case import BaseCase

class TestFirstSmoke(BaseCase):
    def test_get_token(self, get_token):

        assert get_token.status_code == 200, f"Response is not correct"

    def test_get_patient_info(self, get_patient_info):

        assert get_patient_info.status_code == 200, 'Wrong response status code'

    def test_get_mo_IE(self, get_mo_info_extended_v):

        assert get_mo_info_extended_v.status_code == 200, 'Wrong response status code'

    def test_service_post_specs_info(self, get_service_post_specs_info):

        assert get_service_post_specs_info.status_code == 200, 'Wrong response status code'

    def test_get_mo_resource_info(self, get_mo_resource_info_v):

        assert get_mo_resource_info_v.status_code == 200, 'Wrong response status code'

    def test_get_schedule_info(self, get_schedule_info):

        assert get_schedule_info.status_code == 200, 'Wrong response status code'

    def test_create_appointment(self, create_appointment):

        assert create_appointment.status_code == 200, 'Wrong response status code'