import requests
import json
import sys
sys.path.append("f:/projetos/integracoes/")
from Parsers import ReturnItemsOfShipments
from CriptNDD import EncryptPW
from datetime import datetime, date, timedelta

def GetItemsFromInputShipment(supplierid,email,passsword, shipmentid):
    passsword = EncryptPW(passsword)
    url = 'https://api-supplierorders.nddprint.com/SupplierOrdersWS/SupplierOrdersData.asmx'
    #print(url,dealername,usermail, userpw)
    payload ="""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns:xsd="http://www.w3.org/2001/XMLSchema"
        xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
        <GetItemsFromInputShipment xmlns="nddprint.com/api/">
            <supplierID>{}</supplierID>
            <supplierUserEmail>{}</supplierUserEmail>
            <supplierUserPassword>{}</supplierUserPassword>
            <shipmentID>{}</shipmentID>                    
            </GetItemsFromInputShipment>
        </soap:Body>
    </soap:Envelope>
    """.format(supplierid,email,passsword,shipmentid)
    headers = {
    'Host': "api-supplierorders.nddprint.com",
    'Content-Type': "text/xml;charset=UTF-8",
    'soapAction': "nddprint.com/api/GetItemsFromInputShipment",
    }
    response = requests.post(url, data = payload, headers = headers)

    response_json = ReturnItemsOfShipments(response.content)

    items_shipments_return = {
        "items" : response_json,
        "total_items" : len(response_json),
    }

    return items_shipments_return

print(GetItemsFromInputShipment('362','lucas.silva@ndd.com.br','aca122','382878'))

#senha descriptografada aca122