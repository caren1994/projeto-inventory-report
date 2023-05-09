import json
from .importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        path_especific = path.split(".")[-1]
        if path_especific != "json":
            raise ValueError("Arquivo inválido")
        with open(path, mode="r", encoding="utf8") as file:
            return json.load(file)
