import csv
import json
import xml.etree.ElementTree as Et
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class FileC:
    @staticmethod
    def file_csv(path):
        with open(path, mode="r", newline="", encoding="utf8") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]


class FileJ:
    @staticmethod
    def file_json(path):
        with open(path, mode="r", encoding="utf8") as file:
            return json.load(file)


class FileX:
    @staticmethod
    def file_xml(path):
        tree = Et.parse(path)
        roots = tree.getroot()
        stock = []
        for root in roots:
            item = {}
            for subroot in root:
                item[subroot.tag] = subroot.text
            stock.append(item)
        return stock


class Inventory:
    @staticmethod
    def read(path):
        path_especific = path.split(".")[-1]
        if path_especific == "csv":
            return FileC.file_csv(path)
        elif path_especific == "json":
            return FileJ.file_json(path)
        elif path_especific == "xml":
            return FileX.file_xml(path)

    @staticmethod
    def import_data(path, type):
        result = Inventory.read(path)
        if type == "simples":
            report = SimpleReport.generate(result)
        elif type == "completo":
            report = CompleteReport.generate(result)

        return report
