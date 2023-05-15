import requests
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
import json
from json import JSONDecodeError
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

class TestReferral(BaseCase):
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

        self.data = """
               <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v2="http://www.rt-eu.ru/med/er/v2_0">
           <soapenv:Header/>
           <soapenv:Body>
              <v2:GetPatientInfoRequest>
                 <v2:Session_ID>7</v2:Session_ID>
                 <v2:Patient_Data>
                    <v2:OMS_Number>7849500830000203</v2:OMS_Number>
                    <v2:SNILS>000-666-666 25</v2:SNILS>
                    <v2:First_Name>Андрей</v2:First_Name>
                    <v2:Last_Name>Ящеркин</v2:Last_Name>
                    <v2:Middle_Name>Игоревич</v2:Middle_Name>
                    <v2:Birth_Date>1986-06-07</v2:Birth_Date>
                    <v2:Sex>M</v2:Sex>
                    <v2:Phone>9111223456</v2:Phone>
                 </v2:Patient_Data>
                <v2:Pass_referral>1</v2:Pass_referral>
            <!--   <v2:Patient_Info_Kind>REFERRAL</v2:Patient_Info_Kind>-->
              </v2:GetPatientInfoRequest>
           </soapenv:Body>
        </soapenv:Envelope>                
                """

        self.headers = {
            'Content-Type': 'text/xml',
            'SOAPAction': 'GetPatientInfo'}

        self.url = "http://r78-test.zdrav.netrika.ru/fer4/ErWebService"

        response0 = requests.post(url=self.url, headers=self.headers, data=self.data.encode('utf-8'))

        assert response0.status_code == 200, 'Wrong response status code'

        print(response0.text.encode('utf-8'))

    def test_get_mo_resource_info(self):
        self.data = """
                       <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v2="http://www.rt-eu.ru/med/er/v2_0">
                       <soapenv:Header/>
                       <soapenv:Body>
                          <v2:GetMOResourceInfoRequest>
                               <v2:Session_ID>7</v2:Session_ID>
                                <v2:Service_Posts>
                              <v2:Post>
                                   <v2:Post_Id>109</v2:Post_Id>
                                </v2:Post>
                             </v2:Service_Posts>
                             <v2:MO_OID_List>
                            <v2:MO_OID>1.2.643.5.1.13.13.12.2.78.8639.0.238289</v2:MO_OID>
                             </v2:MO_OID_List>
                      <v2:Referral_Id>78214000000471</v2:Referral_Id>
                            <v2:Start_Date_Range>2023-03-30</v2:Start_Date_Range>
                                <v2:End_Date_Range>2023-04-28</v2:End_Date_Range>
                          </v2:GetMOResourceInfoRequest>
                       </soapenv:Body>
                    </soapenv:Envelope>      
                    """

        self.headers = {
                'Content-Type': 'text/xml',
                'SOAPAction': 'GetMOResourceInfo'}

        self.url = "http://r78-test.zdrav.netrika.ru/fer4/ErWebService"

        response3 = requests.post(url=self.url, headers=self.headers, data=self.data.encode('utf-8'))

        assert response3.status_code == 200, 'Wrong response status code'
        print(response3.text.encode('utf-8'))

    def test_get_schedule_info(self):
        self.data = """
                       <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v2="http://www.rt-eu.ru/med/er/v2_0">
                           <soapenv:Header/>
                           <soapenv:Body>
                              <v2:GetScheduleInfoRequest>
                                  <v2:Session_ID>7</v2:Session_ID>         
                                  <v2:Specialist_SNILS>12345678901</v2:Specialist_SNILS>
                                 <v2:MO_OID>1.2.643.5.1.13.13.12.2.78.8639.0.238289</v2:MO_OID>
                            <!--   <v2:Service_Post>
                                    <v2:Post>
                                       <v2:Post_Id>58</v2:Post_Id>
                                    </v2:Post>
                                 <v2:Services_Info>
                                      <v2:Service>
                                       <v2:Service_Id>B04.047.002</v2:Service_Id>
                                    </v2:Service>
                                   </v2:Services_Info>
                                 </v2:Service_Post>-->
                          <v2:Referral_Id>78214000000471</v2:Referral_Id>
                             <v2:Start_Date_Range>2023-03-30</v2:Start_Date_Range>
                                    <v2:End_Date_Range>2023-04-28</v2:End_Date_Range>
                              </v2:GetScheduleInfoRequest>
                           </soapenv:Body>
                        </soapenv:Envelope>      
                    """

        self.headers = {
                'Content-Type': 'text/xml',
                'SOAPAction': 'GetScheduleInfo'}

        self.url = "http://r78-test.zdrav.netrika.ru/fer4/ErWebService"

        response4 = requests.post(url=self.url, headers=self.headers, data=self.data.encode('utf-8'))

        print(response4.text)

        try:
                parced_response_text = response4.json()
                print(parced_response_text)

        except JSONDecodeError:
                print(f"Response is not a JSON")

        parser = ET.XMLPullParser(['start', 'end'])



    def test_create_appointment(self):
        self.data = """
                        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v2="http://www.rt-eu.ru/med/er/v2_0">
                           <soapenv:Header/>
                           <soapenv:Body>
                              <v2:CreateAppointmentRequest>
                                 <!--Optional:-->
                                 <v2:Session_ID>7</v2:Session_ID>
                                 <!--Optional:-->
                                 <v2:Slot_Id>a69f0a43-ecbd-4f91-97a2-1819a90d0abf</v2:Slot_Id>
                              </v2:CreateAppointmentRequest>
                           </soapenv:Body>
                        </soapenv:Envelope>       
                    """

        self.headers = {
                'Content-Type': 'text/xml',
                'SOAPAction': 'CreateAppointment'}

        self.url = "http://r78-test.zdrav.netrika.ru/fer4/ErWebService"

        response5 = requests.post(url=self.url, headers=self.headers, data=self.data.encode('utf-8'))

        assert response5.status_code == 200, 'Wrong response status code'
        print(response5.text.encode('utf-8'))
