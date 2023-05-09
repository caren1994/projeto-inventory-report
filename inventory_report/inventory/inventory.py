from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @staticmethod
    def read(path):
        path_especific = path.split(".")[-1]
        if path_especific == "csv":
            return CsvImporter.import_data(path)
        elif path_especific == "json":
            return JsonImporter.import_data(path)
        elif path_especific == "xml":
            return XmlImporter.import_data(path)

    @staticmethod
    def import_data(path, type):
        result = Inventory.read(path)
        if type == "simples":
            return SimpleReport.generate(result)
        elif type == "completo":
            return CompleteReport.generate(result)
