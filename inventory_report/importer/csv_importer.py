import csv
from .importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        path_especific = path.split(".")[-1]
        if path_especific != "csv":
            raise ValueError("Arquivo inválido")
        with open(path, mode="r", newline="", encoding="utf8") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
