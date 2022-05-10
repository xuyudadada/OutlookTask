import requests
import json


class OutlookMail:
    Sender=""
    Recipient=""
    ContentType="text"
    #text or html
    Header=""
    data=""
    
    def __init__(self,Sender,Recipient,ContentType,Header,data):
        self.Sender=Sender
        self.Recipient=Recipient
        self.ContentType=ContentType
        self.Header=Header
        self.data=data

    #SendMail(MSApp,senderEmail,recipientEmail,data):
    def send(self,MSApp):
        token=MSApp.GetToken()
        url="https://graph.microsoft.com/v1.0/users/{}/sendMail".format(self.Sender)


        head = {
            'Authorization': 'Bearer {}'.format(token),
            'Content-Type': 'application/json'
            }

        datadict={
        "message":{
            "subject": self.Header,
            "toRecipients": [
                {
                    "emailAddress": {
                        "address": self.Recipient
                    }
                }
            ],
            "body": {
                "content": self.data,
                "contentType": self.ContentType
            }
            },
        "SaveToSentItems":True
        }
        response=requests.post(url,data=json.dumps(datadict),headers=head)
        return response.status_code