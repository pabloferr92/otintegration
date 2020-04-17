import requests
import json
import sys
sys.path.append("f:/projetos/integracoes/")
from Parsers import ReturnAciteShipments
from CriptNDD import EncryptPW

from datetime import datetime, date, timedelta

def ReceiveItems(supplierid,email,passsword,shipmentid,datereceived,utc,shipmentlist):

    passsword = EncryptPW(passsword)

    url = 'https://api-supplierorders.nddprint.com/SupplierOrdersWS/SupplierOrdersData.asmx'

    payload ="""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns:xsd="http://www.w3.org/2001/XMLSchema"
        xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <ReceiveItems xmlns="nddprint.com/api/">
            <supplierID>{}</supplierID>
            <supplierUserEmail>{}</supplierUserEmail>
            <supplierUserPassword>{}</supplierUserPassword>
            <shipmentID>{}</shipmentID>
             <dateReceived>{}</dateReceived>
             <utc>{}</utc>
             <shipmentItemList>{}</shipmentItemList>
             <comments>{}</comments>
            </ReceiveItems>
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










'''ShipmentStatusID

Identificador do status da entrega, que pode ser:

1 - Requested (Solicitada)

5 - Reserved (Processada)

7 - Sent (Encaminhada)

8 - Receiving (Em recebimento)'''