from lib.base_case import BaseCase

class TestFirstSmoke(BaseCase):
    def test_get_token(self, get_token):

        assert get_token.status_code == 200, f"Response is not correct"

    def test_get_patient_info(self, get_patient_info):

        assert get_patient_info.status_code == 200, 'Wrong response status code'

    def test_get_mo_info_extended(self, get_mo_info_extended):

        assert get_mo_info_extended.status_code == 200, 'Wrong response status code'

    def test_get_service_post_specs_info(self, get_service_post_specs_info):

        assert get_service_post_specs_info.status_code == 200, 'Wrong response status code'

    def test_get_mo_resource_info(self, get_mo_resource_info):

        assert get_mo_resource_info.status_code == 200, 'Wrong response status code'

    def test_get_schedule_info(self, get_schedule_info):

        assert get_schedule_info.status_code == 200, 'Wrong response status code'

    def test_get_mo_resource_info2(self, get_mo_resource_info2):
        assert get_mo_resource_info2.status_code == 200, 'Wrong response status code'

    def test_get_schedule_info2(self, get_schedule_info2):

        assert get_schedule_info2.status_code == 200, 'Wrong response status code'

    def test_create_appointment(self, create_appointment):

        assert create_appointment.status_code == 200, 'Wrong response status code'