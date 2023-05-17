import json
import requests
from lib.base_case import BaseCase
from lxml import etree as et
from lxml.builder import ElementMaker

class TestFirstSmoke(BaseCase):
    def test_get_token(self):

        response = requests.get(url="http://r78-test.zdrav.netrika.ru/authorization/api/newsession")

        print(response.json()['content']['token'])

        key = 'token'

        if key in response.json()['content']:
            print([key])

        else:
            print(f"Ключа {key} нет в ответе")

        assert response.status_code == 200, f"Response is not correct"

    def test_get_patient_info(self):

        nslist = {
            'soapenv':'http://schemas.xmlsoap.org/soap/envelope/',
            'v2':'http://www.rt-eu.ru/med/er/v2_0'}

        E = ElementMaker(namespace="http://schemas.xmlsoap.org/soap/envelope/", nsmap=nslist)
        E0 = ElementMaker(namespace="http://www.rt-eu.ru/med/er/v2_0", nsmap=nslist)

        out = \
            E.Envelope(
                E.Header(),
                E.Body(
                        E0.GetPatientInfoRequest(
                            E0.Session_ID('9'),
                            E0.Patient_Data(
                                E0.OMS_Number('7849500830000203'),
                                E0.SNILS('000-666-666 25'),
                                E0.First_Name('Андрей'),
                                E0.Last_Name('Ящеркин'),
                                E0.Birth_Date('1986-06-07'),
                                E0.Sex('M'),
                                E0.Phone('9111223456')),
                            E0.Pass_referral('0'))
                    )
                )
        xml_request = et.tostring(out, pretty_print=True)
        print(xml_request)

        self.headers = {
            'Content-Type': 'text/xml',
            'SOAPAction': 'GetPatientInfo'}

        self.url = "http://r78-test.zdrav.netrika.ru/fer4/ErWebService"

        response0 = requests.post(url=self.url, headers=self.headers, data=xml_request)

        print(response0.text)
        assert response0.status_code == 200, 'Wrong response status code'

    def test_get_mo_resource_info(self):
        nslist = {
            'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
            'v2': 'http://www.rt-eu.ru/med/er/v2_0'}

        E = ElementMaker(namespace="http://schemas.xmlsoap.org/soap/envelope/", nsmap=nslist)
        E0 = ElementMaker(namespace="http://www.rt-eu.ru/med/er/v2_0", nsmap=nslist)

        out = \
            E.Envelope(
                E.Header(),
                E.Body(
                    E0.GetMOResourceInfoRequest(
                        E0.Session_ID('9'),
                        E0.Service_Posts(
                            E0.Post(
                                E0.Post_Id('109'))),
                        E0.MO_OID_List(
                            E0.MO_OID('1.2.643.5.1.13.13.12.2.78.8639.0.238289')),
                        E0.Cards_Id('512451409'),
                        E0.Start_Date_Range('2023-05-17'),
                        E0.End_Date_Range('2023-05-28'))
                )
            )
        xml_request = et.tostring(out, pretty_print=True)
        print(xml_request)

        self.headers = {
                'Content-Type': 'text/xml',
                'SOAPAction': 'GetMOResourceInfo'}

        self.url = "http://r78-test.zdrav.netrika.ru/fer4/ErWebService"

        response3 = requests.post(url=self.url, headers=self.headers, data=xml_request)

        assert response3.status_code == 200, 'Wrong response status code'
        print(response3.text)

    def test_get_schedule_info(self):
        nslist = {
            'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
            'v2': 'http://www.rt-eu.ru/med/er/v2_0'}

        E = ElementMaker(namespace="http://schemas.xmlsoap.org/soap/envelope/", nsmap=nslist)
        E0 = ElementMaker(namespace="http://www.rt-eu.ru/med/er/v2_0", nsmap=nslist)

        out = \
            E.Envelope(
                E.Header(),
                E.Body(
                    E0.GetScheduleInfoRequest(
                        E0.Session_ID('9'),
                        E0.Specialist_SNILS('00000000000'),
                        E0.MO_OID('1.2.643.5.1.13.13.12.2.78.8639.0.238289'),
                        E0.Service_Posts(
                            E0.Post(
                                E0.Post_Id('178'))),
                        E0.Cards_Id('512451409'),
                        E0.Start_Date_Range('2023-05-17'),
                        E0.End_Date_Range('2023-05-28'))
                )
            )
        xml_request = et.tostring(out, pretty_print=True)
        print(xml_request)

        self.headers = {
                'Content-Type': 'text/xml',
                'SOAPAction': 'GetScheduleInfo'}

        self.url = "http://r78-test.zdrav.netrika.ru/fer4/ErWebService"

        response4 = requests.post(url=self.url, headers=self.headers, data=xml_request)

        assert response4.status_code == 200, 'Wrong response status code'
        print(response4.text)

    def test_create_appointment(self):
        nslist = {
            'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
            'v2': 'http://www.rt-eu.ru/med/er/v2_0'}

        E = ElementMaker(namespace="http://schemas.xmlsoap.org/soap/envelope/", nsmap=nslist)
        E0 = ElementMaker(namespace="http://www.rt-eu.ru/med/er/v2_0", nsmap=nslist)

        out = \
            E.Envelope(
                E.Header(),
                E.Body(
                    E0.CreateAppointmentRequest(
                        E0.Session_ID('9'),
                        E0.Slot_Id('aded0f77-19c2-4fb1-ad7a-c4b6a2d9caaa'),
                        E0.MO_OID('1.2.643.5.1.13.13.12.2.78.8639.0.238289')
                )
            )
            )
        xml_request = et.tostring(out, pretty_print=True)
        print(xml_request)

        self.headers = {
                'Content-Type': 'text/xml',
                'SOAPAction': 'CreateAppointment'}

        self.url = "http://r78-test.zdrav.netrika.ru/fer4/ErWebService"

        response5 = requests.post(url=self.url, headers=self.headers, data=xml_request)

        assert response5.status_code == 200, 'Wrong response status code'
        print(response5.text)