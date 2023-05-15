class FreeAppointment:
    def get_token(self, data):
        pass
        # code
        # return response.json()

    def get_PatientInfo(self, data):
        pass
        # code
        # return response.json()

    def get_MOInfoExtended(self, data):
        pass
        # code
        # return response.json()

    def get_ServicePostSpecsInfo(self, data):
        pass
        # code
        # return response.json()

    def get_MOResourceInfo(self, data):
        pass
        # code
        # return response.json()

    def create_appointment(self, data):
        pass
        # code
        # return response.json()


class TestCaseSection:
    def test_free_appointment_chain(self):
        fa = FreeAppointment()
        data = {}
        token = fa.get_token(data=data)

        # формируем в data данные для запроса GetPatientInfo с использованием информации полученной в предыдущем запросе
        patient_info = fa.get_PatientInfo(data=data)

        # формируем в data данные для запроса GetMOInfoExtended с использованием информации полученной в предыдущих запросах
        mo_info_extended = fa.get_MOInfoExtended(data=data)

        # формируем в data данные для запроса GetServicePostSpecsInfo с использованием информации полученной в предыдущих запросах
        service_post_info = fa.get_ServicePostSpecsInfo(data=data)

        # формируем в data данные для запроса GetMOResourceInfo с использованием информации полученной в предыдущих запросах
        mo_resource_info = fa.get_MOResourceInfo(data=data)

        # формируем в data данные для запроса GetMOResourceInfo с использованием информации полученной в предыдущих запросах
        mo_resource_info = fa.get_MOResourceInfo(data=data)

        # Финальный запрос. В data данные полученные в предыдущих запросах
        appointment = fa.create_appointment(data=data)
        # Проверки на корректности полученного результата