import xml.etree.ElementTree as ET

def parse_nfe_xml(file):
    tree = ET.parse(file)
    root = tree.getroot()

    # Simples exemplo — adaptar conforme o XML da NF-e
    cfop = root.findtext('.//CFOP')
    ncm = root.findtext('.//NCM')
    cst = root.findtext('.//CST')
    icms = root.findtext('.//vICMS')

    return {
        'cfop': cfop or '',
        'ncm': ncm or '',
        'cst': cst or '',
        'icms': icms or '0.00',
    }
