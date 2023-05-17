# import pytest
# import requests
#
# from lxml import etree as et
# from lxml.builder import ElementMaker
#
#
# @pytest.fixture(scope="class")
# def get_token():
#     # headers1 = dict(Server='nginx', Date=)
#     # headers = {
#     #     'Server': 'nginx',
#     #     'Date': 'Tue, 21 Mar 2023 09:27:18 GMT',
#     #     'Transfer-Encoding': 'chunked',
#     #     'Connection': 'keep-alive',
#     #     'X-Request-ID': 'N3RID1ca5d4de309a05dc44ee86e18d021758'
#     # }
#     #
#     # response = requests.get("http://r78-test.zdrav.netrika.ru/authorization/api/newsession", headers=headers)
#     # return response.json()
#     response = requests.get(url="http://r78-test.zdrav.netrika.ru/authorization/api/newsession")
#
#     print(response.json()['content']['token'])
#
#     key = 'token'
#
#     if key in response.json()['content']:
#         print([key])
#     else:
#         print(f"Ключа {key} нет в ответе")
#     return response
#
# @pytest.fixture(scope="class")
# def get_patient_info(get_token):
#     nslist = {
#         'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
#         'v2': 'http://www.rt-eu.ru/med/er/v2_0'}
#
#     E = ElementMaker(namespace="http://schemas.xmlsoap.org/soap/envelope/", nsmap=nslist)
#     E0 = ElementMaker(namespace="http://www.rt-eu.ru/med/er/v2_0", nsmap=nslist)
#
#     out = \
#         E.Envelope(
#             E.Header(),
#             E.Body(
#                 E0.GetPatientInfoRequest(
#                     E0.Session_ID(self.guid),
#                     E0.Patient_Data(
#                         E0.OMS_Number(self.oms_number),
#                         E0.SNILS(self.patient_snils),
#                         E0.First_Name('Андрей'),
#                         E0.Last_Name('Ящеркин'),
#                         E0.Birth_Date('1986-06-07'),
#                         E0.Sex('M'),
#                         E0.Phone('9111223456')),
#                     E0.Pass_referral('0'))
#             )
#         )
#     xml_request = et.tostring(out, pretty_print=True)
#     print(xml_request)
#
#     self.headers = {
#         'Content-Type': 'text/xml',
#         'SOAPAction': 'GetPatientInfo'}
#
#     response0 = requests.post(url=self.url, headers=self.headers, data=xml_request)
#
#     print(response0.text)
#
