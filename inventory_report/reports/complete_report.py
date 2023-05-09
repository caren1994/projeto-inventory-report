from inventory_report.reports.simple_report import SimpleReport

#  satic método faz mais sentido porque usamos quando não precisamos
#  receber a referência de um objeto especial
#  (seja da classe ou de uma instância) e funciona como uma função
# comum, sem relação.

# se fosse usar o classmethod no lugar de
#  Simplereport.generate seria super().generate


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(products):
        simple_report = SimpleReport.generate(products)
        # para acessar o método generate por ser um
        # metodo de class acessamos ele com o dot chamando o nome da classe

        produtos_empresa = {}

        for product in products:
            empresa = product["nome_da_empresa"]
            if empresa in produtos_empresa:
                produtos_empresa[empresa] += 1
            else:
                produtos_empresa[empresa] = 1

        format = "Produtos estocados por empresa:\n"

        for empresa in produtos_empresa:
            format += f"- {empresa}: {produtos_empresa[empresa]}\n"

        return f"{simple_report}\n" f"{format}"
