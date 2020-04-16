from bs4 import BeautifulSoup

def ReturnAciteShipments(response):
    soup = BeautifulSoup(response, 'html.parser')
    try:
        activeshipments = soup.getactiveshipmentsforsupplierresult.get_text()
        return activeshipments
    except:
        errors = soup.faultstring.get_text()
        return errors


