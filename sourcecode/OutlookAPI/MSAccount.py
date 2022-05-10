import requests
import json



class MSApp:
    client_id=""
    client_secret=""
    tenant=""    

    def __init__(self,client_id,client_secret,tenant):
        self.client_id=client_id
        self.client_secret=client_secret
        self.tenant=tenant

    def GetToken(self):
        scope="https://graph.microsoft.com/.default"
        grant_type="client_credentials"

        url="https://login.microsoftonline.com/{}/oauth2/v2.0/token".format(self.tenant)
        head={
            "Host": "login.microsoftonline.com",
            "Content-Type": "application/x-www-form-urlencoded"
            }
        str="client_id={}&scope={}&client_secret={}&grant_type={}".format(self.client_id,scope,self.client_secret,grant_type)
        response=requests.post(url,headers=head,data=str)
        if (response.status_code==200):
            result=json.loads(response.text)["access_token"]
            return result
        else:
            return response.text

