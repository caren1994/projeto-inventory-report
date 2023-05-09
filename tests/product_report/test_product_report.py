from inventory_report.inventory.product import Product


def test_relatorio_produto():
    produto = Product(
        1,
        "tênis",
        "redley",
        "08/05/2023",
        "08/05/2030",
        "08052023",
        "longe dos cachorros",
    )

    assert produto.__repr__() == (
        f"O produto {produto.nome_do_produto}"
        f" fabricado em {produto.data_de_fabricacao}"
        f" por {produto.nome_da_empresa} com validade"
        f" até {produto.data_de_validade}"
        f" precisa ser armazenado {produto.instrucoes_de_armazenamento}."
    )
