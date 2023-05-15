import json

import requests
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lxml import etree as et
from lxml.builder import ElementMaker

def test_create_xml_body_using_elementtree():
    soapenv_namespace = "http://schemas.xmlsoap.org/soap/envelope/"
    soapenv = "{%s}" % soapenv_namespace
    v2_namespace = "http://www.rt-eu.ru/med/er/v2_0"
    v2 = "{%s}" % v2_namespace
    nsmap = {'soapenv': soapenv_namespace, 'v2': v2_namespace}
    Envelope = et.Element(soapenv + "Envelope", nsmap=nsmap)
    Header = et.SubElement(soapenv + "Envelope", nsmap=nsmap)
    Body = et.SubElement(soapenv + "Envelope", nsmap=nsmap)
    GetPatientInfoRequest = et.SubElement(Body, v2 + "GetPatientInfoRequest", nsmap=nsmap)
    Session_ID = et.SubElement(Body, v2 + "Session_ID", nsmap=nsmap, text='7')
    Patient_Data = et.SubElement(Body, v2 + "Patient_Data", nsmap=nsmap)
    OMS_Number = et.SubElement(Body, v2 + "OMS_Number", nsmap=nsmap, text='7849500830000203')
    SNILS = et.SubElement(Body, v2 + "SNILS", nsmap=nsmap, text='000-666-666 25')
    First_Name = et.SubElement(Body, v2 + "First_Name", nsmap=nsmap, text='Андрей')
    Last_Name = et.SubElement(Body, v2 + "Last_Name", nsmap=nsmap, text='Ящеркин')
    Birth_Date = et.SubElement(Body, v2 + "Birth_Date", nsmap=nsmap, text='1986-06-07')
    Sex = et.SubElement(Body, v2 + "Sex", nsmap=nsmap, text='М')
    Phone = et.SubElement(Body, v2 + "Phone", nsmap=nsmap, text='9111223456')
    Pass_referral = et.SubElement(Body, v2 + "Pass_referral", nsmap=nsmap, text='0')

    nslist = {
        'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
        'v2': 'http://www.rt-eu.ru/med/er/v2_0'}

    E = ElementMaker(namespace="http://schemas.xmlsoap.org/soap/envelope/", nsmap=nslist)
    E0 = ElementMaker(namespace="http://www.rt-eu.ru/med/er/v2_0", nsmap="http://www.rt-eu.ru/med/er/v2_0")

    out = E.Envelope(
        E.Header(),
        E.Body(
            E0.GetPatientInfoRequest,
            E0.Session_ID('7'),
            E0.Patient_Data,
            E0.OMS_Number('7849500830000203'),
            E0.SNILS('000-666-666 25'),
            E0.First_Name('Андрей'),
            E0.Last_Name('Ящеркин'),
            E0.Birth_Date('1986-06-07'),
            E0.Sex('М'),
            E0.Phone('9111223456'),
            E0.Pass_referral('0')
        )
    )

    print(et.tostring(out, encoding="UTF-8", standalone="yes", pretty_print=True))