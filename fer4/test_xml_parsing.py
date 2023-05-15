import requests
import xml.etree.ElementTree as et

class TestXMLParsing:
    def test_get_token(self):

        response = requests.get(url="http://r78-test.zdrav.netrika.ru/authorization/api/newsession")

        print(response.json()['content']['token'])

        key = 'token'

        if key in response.json()['content']:
            print([key])

        else:
            print(f"Ключа {key} нет в ответе")

        assert response.status_code == 200, f"Response is not correct"


    def create_xml_body_using_elementtree(self):

            root = et.Element('Envelope')
            head = et.SubElement(root, 'Header')
            body = et.SubElement(head, 'Body')
            et.SubElement(body, 'GetPatientInfoRequest')
            et.SubElement(body, 'Session_ID', text='7')
            et.SubElement(body, 'Patient_Data')
            et.SubElement(body, 'OMS_Number', text='7849500830000203')
            et.SubElement(body, 'SNILS', text='000-666-666 25')
            et.SubElement(body, 'First_Name', text='Андрей')
            et.SubElement(body, 'Last_Name', text='Ящеркин')
            et.SubElement(body, 'Birth_Date', text='1986-06-07')
            et.SubElement(body, 'Sex', text='М')
            et.SubElement(body, 'Phone', text='9111223456')
            et.SubElement(body, 'Pass_referral', text='0')
            return et.tostring(root)

        response = requests.post(url="http://10.50.3.41:17825/fer4/ErWebService",
                                 headers={'Content-Type': 'text/xml', 'SOAPAction': 'GetPatientInfo', 'Version':'1.0.0'},
                                 data=create_xml_body_using_elementtree())

        assert response.status_code == 200, 'Wrong response status code'

        print(response.text)


root = et.Element('Envelope')
head = et.SubElement(root, 'Header')
body = et.SubElement(root, 'Body')
et.SubElement(body, 'GetPatientInfoRequest')
et.SubElement(body, 'Session_ID', text='7')
et.SubElement(body, 'Patient_Data')
et.SubElement(body, 'OMS_Number', text='7849500830000203')
et.SubElement(body, 'SNILS', text='000-666-666 25')
et.SubElement(body, 'First_Name', text='Андрей')
et.SubElement(body, 'Last_Name', text='Ящеркин')
et.SubElement(body, 'Birth_Date', text='1986-06-07')
et.SubElement(body, 'Sex', text='М')
et.SubElement(body, 'Phone', text='9111223456')
et.SubElement(body, 'Pass_referral', text='0')

print(et.tostring(root))
return et.tostring(root)

soapenv_namespace = "http://schemas.xmlsoap.org/soap/envelope/"
soapenv = "{%s}" % soapenv_namespace
v2_namespace = "http://www.rt-eu.ru/med/er/v2_0"
v2 = "{%s}" % v2_namespace
nsmap = {'soapenv': soapenv_namespace, 'v2': v2_namespace}
Envelope = et.Element(soapenv + "Envelope", nsmap=nsmap)
Header = et.SubElement(Envelope, nsmap=nsmap)
Body = et.SubElement(Envelope, nsmap=nsmap)
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