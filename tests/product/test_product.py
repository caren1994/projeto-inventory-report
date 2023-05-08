from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(
        id=1,
        nome_do_produto="tênis",
        nome_da_empresa="redley",
        data_de_fabricacao="2023-05-08",
        data_de_validade="2030-05-08",
        numero_de_serie="08052023",
        instrucoes_de_armazenamento="Mantenha longe de cachorros"
    )

    assert produto.id == 1
    assert produto.nome_do_produto == "tênis"
    assert produto.nome_da_empresa == "redley"
    assert produto.data_de_fabricacao == "2023-05-08"
    assert produto.data_de_validade == "2030-05-08"
    assert produto.numero_de_serie == "08052023"
    assert produto.instrucoes_de_armazenamento == "Mantenha longe de cachorros"
