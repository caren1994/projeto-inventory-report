from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable


class InventoryRefactor(Iterable):
    def __init__(self, importer: Importer):
        self.data = []
        self.importer = importer

    def import_data(self, path, type):

        imported = self.importer.import_data(path)
        self.data += imported

        if type == "simples":
            return SimpleReport.generate(self.data)
        elif type == "completo":
            return CompleteReport.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
