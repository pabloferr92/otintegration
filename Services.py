from ExampleReturn import ActiveShipment
from ReadNF import ReturnNfInformations
from GetActiveShipmentsForSupplier import GetActiveShipmentsForSupplier


def NfShipmentComparative(logon, password, shipmentid):

    nfs = ReturnNfInformations()
    shipments = ActiveShipment
    #shipments = GetActiveShipmentsForSupplier(logon,password,shipmentid)
    context = {
            'nfs_in_shipments' : [],
            'nfs_in_nfs' : [],
            'nfs_not_in_shipments' : []
    }

    for n in nfs['nfs']:
        nf = n[0].split(';')
        context['nfs_in_nfs'].append(nf[0])

    for s in shipments:
        context['nfs_in_shipments'].append(s['OrderField1Value'])

    for nf in context['nfs_in_nfs']:
        if nf not in context['nfs_in_shipments']:
            context['nfs_not_in_shipments'].append(nf)
            
    return context
        
