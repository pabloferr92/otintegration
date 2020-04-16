import requests
import json
import sys
sys.path.append("f:/projetos/integracoes/")

from Services.XmlParser import ReturnEnterprises
from Services.GetHostFromURL import GetHost

def GetEnterprises(url,dealername,usermail, userpw):
    url = url
    hostname = GetHost(url)
    #print(url,dealername,usermail, userpw)

    payload ="""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns:xsd="http://www.w3.org/2001/XMLSchema"
        xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <GetEnterprises xmlns="nddprint.com/api/">
            <dealerName>{}</dealerName>
            <dealerUserEmail>{}</dealerUserEmail>
            <dealerUserPassword>{}</dealerUserPassword>
            <fieldsList></fieldsList>
        </GetEnterprises>
        </soap:Body>
    </soap:Envelope>
    """.format(dealername,usermail,userpw)

    headers = {
    'Host': "{}".format(hostname),
    'Content-Type': "text/xml;charset=UTF-8",
    'soapAction': "nddprint.com/api/GetEnterprises",
    #'cache-control': "no-cache",
    #'Postman-Token': "c283943b-5a24-4d5f-9f99-05559274026e"
    }
    #print(headers)
    response = requests.post(url, data = payload, headers = headers)
    #print(response.content)
    Enterprises_Json = json.loads(ReturnEnterprises(response.content))
    #print(payload, headers)
    return Enterprises_Json


def GetEnterprisesFixed(dealername,usermail, userpw):
    url = "http://mpstraining.nddprint.com/GeneralWS/GeneralData.asmx"
    hostname = GetHost(url)
    #print(url,dealername,usermail, userpw)

    payload ="""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns:xsd="http://www.w3.org/2001/XMLSchema"
        xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <GetEnterprises xmlns="nddprint.com/api/">
            <dealerName>{}</dealerName>
            <dealerUserEmail>{}</dealerUserEmail>
            <dealerUserPassword>{}</dealerUserPassword>
            <fieldsList></fieldsList>
        </GetEnterprises>
        </soap:Body>
    </soap:Envelope>
    """.format(dealername,usermail,userpw)

    headers = {
    'Host': "{}".format(hostname),
    'Content-Type': "text/xml;charset=UTF-8",
    'soapAction': "nddprint.com/api/GetEnterprises",
    #'cache-control': "no-cache",
    #'Postman-Token': "c283943b-5a24-4d5f-9f99-05559274026e"
    }
    #print(headers)
    response = requests.post(url, data = payload, headers = headers)
    #print(response.content)
    Enterprises_Json = json.loads(ReturnEnterprises(response.content))
    #print(payload, headers)
    return Enterprises_Json
