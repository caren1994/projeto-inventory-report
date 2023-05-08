from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, produtos):
        data_de_fabricacao = min(
            [produto["data_de_fabricacao"] for produto in produtos]
        )
        data_de_validade = min(
            [
                produto["data_de_validade"]
                for produto in produtos
                if datetime.strptime(produto["data_de_validade"], "%Y-%m-%d")
                >= datetime.today()
            ]
        )
        empresas = {}
        for produto in produtos:
            if produto["nome_da_empresa"] in empresas:
                empresas[produto["nome_da_empresa"]] += 1
            else:
                empresas[produto["nome_da_empresa"]] = 1
        empresa = max(
            empresas, key=empresas.get
        )  # necessaria para o max identificar
        # cada chave que tem no meu dicionario
        return (
            f"Data de fabricação mais antiga: {data_de_fabricacao}\n"
            f"Data de validade mais próxima: {data_de_validade}\n"
            f"Empresa com mais produtos: {empresa}"
        )
