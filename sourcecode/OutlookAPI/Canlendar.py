import requests
from urllib import parse
import json





def CreateTask(name,date,timelist,location,remindtime):
    #2019-06-16T12:00:00
    #此处应该写一个程序获得日历的唯一识别码和用户识别码而不是直接引入
    settings=json.load(open('mydata.yml','r'))

    token=GetToken()
    head = {
        'Authorization': 'Bearer {}'.format(token),
        'Content-Type': 'application/json'
        }
    datadict={
        "subject":"{}@{}".format(name,location),
        "start":{
            "dateTime": "{}T{}".format(date,timelist[0]),
            "timeZone": "Asia/Shanghai"
            },
        "end":{
            "dateTime": "{}T{}".format(date,timelist[1]),
            "timeZone": "Asia/Shanghai"
            },
        "location":{
            "displayName":location
            },
        "reminderMinutesBeforeStart":remindtime
        }
    jsondata=json.dumps(datadict)
    response=requests.post(settings['_URL'],data=jsondata,headers=head)
    return response.status_code



#name="hello"
#date="2022-03-25"
#timelist=['17:49:41','18:49:41']
#location="test"
#remindtime=30

#CreateTask(name,date,timelist,location,remindtime)

