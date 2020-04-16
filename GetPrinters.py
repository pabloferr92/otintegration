import sys
sys.path.append("f:/projetos/integracoes/")

import requests
import json
from Services.XmlParser import PrintersParser

from Services.ReturnEnterpriseID import ReturnEnpriseIDFixed

from Services.GetHostFromURL import GetHost

def GetPrinters(url,dealername,email,password,enterprise):

  enterpriseid = ReturnEnpriseIDFixed(dealername,email,password,enterprise)

  hostname = GetHost(url)

  payload ="""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns:xsd="http://www.w3.org/2001/XMLSchema"
        xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
          <soap:Body>
          <GetPrinters xmlns="nddprint.com/api/">
          <dealerName>{}</dealerName>
          <dealerUserEmail>{}</dealerUserEmail>
          <dealerUserPassword>{}</dealerUserPassword>
          <enterpriseID>{}</enterpriseID>
          <fieldsList>PrinterDeviceID;PrinterName;ModelName;SerialNumber;AddressMac</fieldsList>
          </GetPrinters>
        </soap:Body>
    </soap:Envelope>
    """.format(dealername,email,password,enterpriseid)

  headers = {
      'Host': "{}".format(hostname),
      'Content-Type': "text/xml;charset=UTF-8",
      'soapAction': "nddprint.com/api/GetPrinters",
      #'cache-control': "no-cache",
      #'Postman-Token': "1499284d-bfba-41b6-a9f4-38bf7bbaaeea"
      }


  response = requests.post(url, data = payload, headers = headers)
  #print(response.content)
  
  Printers_json = json.loads(PrintersParser(response.content))
  #print(Printers_json)
  return Printers_json

#print(GetPrinters("http://mpstraining.nddprint.com/GeneralWS/GeneralData.asmx","FM_INTEGRACAO","marcelo@fmsdi.com.br","GtiMy6NNfIY/bqgYslSKLQ==","RACIONAL"))
