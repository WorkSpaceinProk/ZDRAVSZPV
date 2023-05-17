import pytest
import requests

from lxml import etree as et
from lxml.builder import ElementMaker
from bs4 import BeautifulSoup

from resources import *

@pytest.fixture(scope="class")
def get_token():
    response = requests.get(url="http://r78-test.zdrav.netrika.ru/authorization/api/newsession")

    print(response.json()['content']['token'])

    key = 'token'

    if key in response.json()['content']:
        print([key])
    else:
        print(f"Ключа {key} нет в ответе")
    return response


#фикстуры для свободной записи

@pytest.fixture(scope="class")
def get_patient_info(get_token):

    nslist = {
        'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
        'v2': 'http://www.rt-eu.ru/med/er/v2_0'}

    E = ElementMaker(namespace="http://schemas.xmlsoap.org/soap/envelope/", nsmap=nslist)
    E0 = ElementMaker(namespace="http://www.rt-eu.ru/med/er/v2_0", nsmap=nslist)

    out = \
        E.Envelope(
            E.Header(),
            E.Body(
                E0.GetPatientInfoRequest(
                    E0.Session_ID(GUID),
                    E0.Patient_Data(
                        E0.OMS_Number(OMS_NUMBER),
                        E0.SNILS(PATIENT_SNILS),
                        E0.First_Name(First_Name),
                        E0.Last_Name(Last_Name),
                        E0.Birth_Date(Birth_Date),
                        E0.Sex(Sex),
                        E0.Phone(Phone)),
                    E0.Pass_referral(Pass_referral))
            )
        )
    xml_request = et.tostring(out, pretty_print=True)
    print(xml_request)

    headers = {
        'Content-Type': 'text/xml',
        'SOAPAction': 'GetPatientInfo'}

    response = requests.post(url=URL, headers=headers, data=xml_request)

    print(response.text)

    return response

@pytest.fixture(scope="class")
def get_mo_info_extended(get_patient_info):

    nslist = {
        'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
        'v2': 'http://www.rt-eu.ru/med/er/v2_0'}

    E = ElementMaker(namespace="http://schemas.xmlsoap.org/soap/envelope/", nsmap=nslist)
    E0 = ElementMaker(namespace="http://www.rt-eu.ru/med/er/v2_0", nsmap=nslist)

    out = \
        E.Envelope(
            E.Header(),
            E.Body(
                E0.GetMOInfoExtendedRequest(
                    E0.Session_ID(GUID),
                    E0.Booking_Type(Booking_Type))
            )
        )

    xml_request = et.tostring(out, pretty_print=True)
    print(xml_request)

    headers = {
        'Content-Type': 'text/xml',
        'SOAPAction': 'GetMOInfoExtended'}

    response = requests.post(url=URL, headers=headers, data=xml_request)

    print(response.text)

    return response

@pytest.fixture(scope="class")
def get_service_post_specs_info(get_mo_info_extended):

    nslist = {
        'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
        'v2': 'http://www.rt-eu.ru/med/er/v2_0'}

    E = ElementMaker(namespace="http://schemas.xmlsoap.org/soap/envelope/", nsmap=nslist)
    E0 = ElementMaker(namespace="http://www.rt-eu.ru/med/er/v2_0", nsmap=nslist)

    out = \
        E.Envelope(
            E.Header(),
            E.Body(
                E0.GetServicePostSpecsInfoRequest(
                    E0.Session_ID(GUID),
                    E0.MO_Id(MO_Id))
            )
        )
    xml_request = et.tostring(out, pretty_print=True)
    print(xml_request)

    headers = {
        'Content-Type': 'text/xml',
        'SOAPAction': 'GetServicePostSpecsInfo'}

    response = requests.post(url=URL, headers=headers, data=xml_request)

    print(response.text)

    return response

@pytest.fixture(scope="class")
def get_mo_resource_info(get_service_post_specs_info):

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
                    E0.Session_ID(GUID),
                    E0.Service_Posts(
                        E0.Post(
                            E0.Post_Id(Post_Id))),
                    E0.MO_OID_List(
                            E0.MO_OID(MO_OID_LPU)),
                    E0.Start_Date_Range(Start_Date_Range),
                    E0.End_Date_Range(End_Date_Range)
                    )
             )
        )
    xml_request = et.tostring(out, pretty_print=True)
    print(xml_request)

    headers = {
        'Content-Type': 'text/xml',
        'SOAPAction': 'GetMOResourceInfo'}

    response = requests.post(url=URL, headers=headers, data=xml_request)

    print(response.text)

    return response

@pytest.fixture(scope="class")
def get_schedule_info(get_mo_resource_info):
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
                    E0.Session_ID(GUID),
                    E0.Specialist_SNILS(DOCTOR_SNILS),
                    E0.MO_OID(MO_OID_LPU),
                    E0.Service_Posts(
                        E0.Post(
                            E0.Post_Id(Post_Id))),
                    E0.Start_Date_Range(Start_Date_Range),
                    E0.End_Date_Range(End_Date_Range))
            )
        )
    xml_request = et.tostring(out, pretty_print=True)
    print(xml_request)

    headers = {
        'Content-Type': 'text/xml',
        'SOAPAction': 'GetScheduleInfo'}
    response = requests.post(url=URL, headers=headers, data=xml_request)

    print(response.text)

    return response

@pytest.fixture(scope="class")
def create_appointment(get_schedule_info, get_slot_id):

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
                    E0.Session_ID(GUID),
                    E0.Slot_Id(get_slot_id),
                    E0.MO_OID(MO_OID_LPU)
                )
            )
        )
    xml_request = et.tostring(out, pretty_print=True)
    print(xml_request)

    headers = {
        'Content-Type': 'text/xml',
        'SOAPAction': 'CreateAppointment'}

    response = requests.post(url=URL, headers=headers, data=xml_request)

    print(response.text)

    return response

@pytest.fixture(scope="class")
def get_slot_id(get_schedule_info):

    xml_content = BeautifulSoup(get_schedule_info.text, 'xml')
    slot_id = xml_content.find('Slot_Id').text
    print(slot_id)
    return slot_id


#фикстуры для сервиса записи по направдению

@pytest.fixture(scope="class")
def get_patient_info_referral(get_token):

    nslist = {
        'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
        'v2': 'http://www.rt-eu.ru/med/er/v2_0'}

    E = ElementMaker(namespace="http://schemas.xmlsoap.org/soap/envelope/", nsmap=nslist)
    E0 = ElementMaker(namespace="http://www.rt-eu.ru/med/er/v2_0", nsmap=nslist)

    out = \
        E.Envelope(
            E.Header(),
            E.Body(
                E0.GetPatientInfoRequest(
                    E0.Session_ID(GUID),
                    E0.Patient_Data(
                        E0.OMS_Number(OMS_NUMBER),
                        E0.SNILS(PATIENT_SNILS),
                        E0.First_Name(First_Name),
                        E0.Last_Name(Last_Name),
                        E0.Birth_Date(Birth_Date),
                        E0.Sex(Sex),
                        E0.Phone(Phone)),
                    E0.Pass_referral(Pass_referral_1))
            )
        )
    xml_request = et.tostring(out, pretty_print=True)
    print(xml_request)

    headers = {
        'Content-Type': 'text/xml',
        'SOAPAction': 'GetPatientInfo'}

    response = requests.post(url=URL, headers=headers, data=xml_request)

    print(response.text)

    return response


@pytest.fixture(scope="class")
def get_schedule_info_referral(get_mo_resource_info):
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
                    E0.Session_ID(GUID),
                    E0.Specialist_SNILS(DOCTOR_SNILS),
                    E0.MO_OID(MO_OID_LPU),
                    E0.Service_Posts(
                        E0.Post(
                            E0.Post_Id(Post_Id))),
                    E0.Referral_id(Referral_id),
                    E0.Start_Date_Range(Start_Date_Range),
                    E0.End_Date_Range(End_Date_Range))
            )
        )
    xml_request = et.tostring(out, pretty_print=True)
    print(xml_request)

    headers = {
        'Content-Type': 'text/xml',
        'SOAPAction': 'GetScheduleInfo'}
    response = requests.post(url=URL, headers=headers, data=xml_request)

    print(response.text)

    return response


#фикстуры для сервиса вакцинации

@pytest.fixture(scope="class")
def get_mo_info_extended_v(get_patient_info):

    nslist = {
        'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
        'v2': 'http://www.rt-eu.ru/med/er/v2_0'}

    E = ElementMaker(namespace="http://schemas.xmlsoap.org/soap/envelope/", nsmap=nslist)
    E0 = ElementMaker(namespace="http://www.rt-eu.ru/med/er/v2_0", nsmap=nslist)

    out = \
        E.Envelope(
            E.Header(),
            E.Body(
                E0.GetMOInfoExtendedRequest(
                    E0.Session_ID(GUID),
                    E0.Booking_Type(Booking_Type_v))
            )
        )

    xml_request = et.tostring(out, pretty_print=True)
    print(xml_request)

    headers = {
        'Content-Type': 'text/xml',
        'SOAPAction': 'GetMOInfoExtended'}

    response = requests.post(url=URL, headers=headers, data=xml_request)

    print(response.text)

    return response

@pytest.fixture(scope="class")
def get_mo_resource_info_v(get_service_post_specs_info):

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
                    E0.Session_ID(GUID),
                    E0.Vaccination_Id(Vaccination_Id),
                    E0.Service_Posts(
                        E0.Post(
                            E0.Post_Id(Post_Id))),
                    E0.MO_OID_List(
                            E0.MO_OID(MO_OID_LPU)),
                    E0.Start_Date_Range(Start_Date_Range),
                    E0.End_Date_Range(End_Date_Range)
                    )
             )
        )
    xml_request = et.tostring(out, pretty_print=True)
    print(xml_request)

    headers = {
        'Content-Type': 'text/xml',
        'SOAPAction': 'GetMOResourceInfo'}

    response = requests.post(url=URL, headers=headers, data=xml_request)

    print(response.text)

    return response



    #фикстуры для сервиса углубленной диспансеризации

@pytest.fixture(scope="class")
def get_mo_info_extended_d(get_patient_info):

    nslist = {
        'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
        'v2': 'http://www.rt-eu.ru/med/er/v2_0'}

    E = ElementMaker(namespace="http://schemas.xmlsoap.org/soap/envelope/", nsmap=nslist)
    E0 = ElementMaker(namespace="http://www.rt-eu.ru/med/er/v2_0", nsmap=nslist)

    out = \
        E.Envelope(
            E.Header(),
            E.Body(
                E0.GetMOInfoExtendedRequest(
                    E0.Session_ID(GUID),
                    E0.Booking_Type(Booking_Type_d))
            )
        )

    xml_request = et.tostring(out, pretty_print=True)
    print(xml_request)

    headers = {
        'Content-Type': 'text/xml',
        'SOAPAction': 'GetMOInfoExtended'}

    response = requests.post(url=URL, headers=headers, data=xml_request)

    print(response.text)

    return response


    #фикстуры для сервиса медосмотров (диспансеризации)
@pytest.fixture(scope="class")
def get_mo_resource_info_exam(get_patient_info):

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
                    E0.Session_ID(GUID),
                    E0.Vaccination_Id(Vaccination_Id),
                    E0.Service_Posts(
                        E0.Post(
                            E0.Post_Id(Post_Id))),
                    E0.MO_OID_List(
                            E0.MO_OID(MO_OID_LPU)),
                    E0.Cards_Id(Cards_Id),
                    E0.Start_Date_Range(Start_Date_Range),
                    E0.End_Date_Range(End_Date_Range)
                    )
             )
        )
    xml_request = et.tostring(out, pretty_print=True)
    print(xml_request)

    headers = {
        'Content-Type': 'text/xml',
        'SOAPAction': 'GetMOResourceInfo'}

    response = requests.post(url=URL, headers=headers, data=xml_request)

    print(response.text)

    return response

@pytest.fixture(scope="class")
def get_schedule_info_exam(get_mo_resource_info):
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
                    E0.Session_ID(GUID),
                    E0.Specialist_SNILS(DOCTOR_SNILS),
                    E0.MO_OID(MO_OID_LPU),
                    E0.Service_Posts(
                        E0.Post(
                            E0.Post_Id(Post_Id))),
                    E0.Cards_Id(Cards_Id),
                    E0.Start_Date_Range(Start_Date_Range),
                    E0.End_Date_Range(End_Date_Range))
            )
        )
    xml_request = et.tostring(out, pretty_print=True)
    print(xml_request)

    headers = {
        'Content-Type': 'text/xml',
        'SOAPAction': 'GetScheduleInfo'}
    response = requests.post(url=URL, headers=headers, data=xml_request)

    print(response.text)

    return response