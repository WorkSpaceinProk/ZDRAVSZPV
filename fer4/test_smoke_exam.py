from lib.base_case import BaseCase


class TestSmokeExam(BaseCase):
    def test_get_token(self, get_token):
        assert get_token.status_code == 200, f"Response is not correct"

    def test_get_patient_info(self, get_patient_info):
        assert get_patient_info.status_code == 200, 'Wrong response status code'

    def test_get_mo_resource_info_exam(self, get_mo_resource_info_exam):
        assert get_mo_resource_info_exam.status_code == 200, 'Wrong response status code'

    def test_get_schedule_info_exam(self, get_schedule_info_exam):
        assert get_schedule_info_exam.status_code == 200, 'Wrong response status code'

    def test_create_appointment_exam(self, create_appointment_exam):
        assert create_appointment_exam.status_code == 200, 'Wrong response status code'
