from ExampleReturn import ActiveShipment
from ReadNF import ReturnNfInformations


def NfShipmentComparative():
    nf_informations = ReturnNfInformations()

    total_nfs = len(nf_informations['nfs'])
    total_nfs_to_close = len(nf_informations['nfs_to_close'])

    total_shipments = len(ActiveShipment)
    print(total_shipments)       

NfShipmentComparative()