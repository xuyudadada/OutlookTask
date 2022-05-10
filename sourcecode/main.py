import OutlookAPI as ms
import datetime

import json


#加载配置文件
def LoadSettings(FileName):
    try:
        Settings=json.load(open(FileName,"r"))
        return Settings
    except:
        return None



def main():
    #读取配置文件
    Settings=LoadSettings("settings.ini")
    if(Settings==None):
        return "Can't find appropriate configuration file!"

    #生成所需的hust用户对象和outlook对象
    MSAccount=ms.MSApp(Settings["client_id"],Settings["client_secret"],Settings["tenant"])



    #生成邮件内容
    ContentSeq="test email"
    #发送邮件
    testmail=ms.OutlookMail("auto@xuyudadada.onmicrosoft.com","hjlbb1013@163.com","text","雷雷的微校园提醒","".join(ContentSeq))
    print(testmail.send(MSAccount))
    

if (__name__=="__main__"):
    main()