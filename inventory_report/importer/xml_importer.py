import xml.etree.ElementTree as Et
from .importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        path_especific = path.split(".")[-1]
        if path_especific != "xml":
            raise ValueError("Arquivo inválido")
        tree = Et.parse(path)
        roots = tree.getroot()
        stock = []
        for root in roots:
            item = {}
            for subroot in root:
                item[subroot.tag] = subroot.text
            stock.append(item)
        return stock
