import requests
from lib.base_case import BaseCase

class TestGetPatientInfo(BaseCase):

    def setup_method(self):

        self.data = """
               <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v2="http://www.rt-eu.ru/med/er/v2_0">
           <soapenv:Header/>
           <soapenv:Body>
              <v2:GetPatientInfoRequest>
                 <v2:Session_ID>99</v2:Session_ID>
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
                <v2:Pass_referral>0</v2:Pass_referral>
            <!--   <v2:Patient_Info_Kind>REFERRAL</v2:Patient_Info_Kind>-->
              </v2:GetPatientInfoRequest>
           </soapenv:Body>
        </soapenv:Envelope>                
                """

        self.headers = {
            'Content-Type': 'text/xml',
            'SOAPAction': 'GetPatientInfo'}

        self.url = "http://r78-test.zdrav.netrika.ru/fer4/ErWebService"

        response = requests.post(url=self.url, headers=self.headers, data=self.data.encode('utf-8'))

        print(f'***** {response.status_code}')
        print(f'***** {response.content}')


    def test_get_patient_info(self, get_token):
        token = get_token['content']['token']
        self.headers['token'] = token

        response = requests.post(url=self.url, headers=self.headers, data=self.data.encode('utf-8'))

        assert response.status_code == 200, 'Wrong response status code'
        print(response.text)
