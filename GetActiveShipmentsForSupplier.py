import requests
import json
import sys
sys.path.append("f:/projetos/integracoes/")
from Parsers import ReturnAciteShipments
from CriptNDD import EncryptPW

from datetime import datetime, date, timedelta

def GetActiveShipmentsForSupplier(supplierid,email,passsword):

    passsword = EncryptPW(passsword)

    url = 'https://api-supplierorders.nddprint.com/SupplierOrdersWS/SupplierOrdersData.asmx'
    #print(url,dealername,usermail, userpw)

    payload ="""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns:xsd="http://www.w3.org/2001/XMLSchema"
        xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <GetActiveShipmentsForSupplier xmlns="nddprint.com/api/">
            <supplierID>{}</supplierID>
            <supplierUserEmail>{}</supplierUserEmail>
            <supplierUserPassword>{}</supplierUserPassword>
            <fieldsList>
                ShipmentID;
                ExpectedDate;
                ShipmentStatusID;
                OrderID;
                OrderShipmentNumber;
                StockID;
                StockName;
                OrderField1Name;
                OrderField1Value
            </fieldsList>                       
            </GetActiveShipmentsForSupplier>
        </soap:Body>
    </soap:Envelope>
    """.format(supplierid,email,passsword)

    headers = {
    'Host': "api-supplierorders.nddprint.com",
    'Content-Type': "text/xml;charset=UTF-8",
    'soapAction': "nddprint.com/api/GetActiveShipmentsForSupplier",
    }
    response = requests.post(url, data = payload, headers = headers)

    response_json = ReturnAciteShipments(response.content)

    shipments_return = {
        "shipments" : response_json,
        "total_shipments" : len(response_json),
    }

    return shipments_return

#print(GetActiveShipmentsForSupplier('362','lucas.silva@ndd.com.br','MU/TS5GBuxjdP7bMT773nw=='))

#senha descriptografada aca122