# sistema_restaurante_spaghetti.py
# Exemplo de "Spaghetti Code" (mal estruturado, tudo misturado)

cardapio = {
    1: {"nome": "Hambúrguer", "preco": 15.0},
    2: {"nome": "Pizza", "preco": 25.0},
    3: {"nome": "Suco", "preco": 7.0},
    4: {"nome": "Refrigerante", "preco": 6.0}
}

pedidos = []
total = 0

while True:
    print("\n=== Restaurante ===")
    print("1. Fazer Pedido")
    print("2. Fechar Conta")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n--- Cardápio ---")
        for codigo, item in cardapio.items():
            print(str(codigo) + " - " + item["nome"] + " (R$ " + str(item["preco"]) + ")")

        escolha = input("Digite o código do item: ")
        if escolha.isdigit():
            escolha = int(escolha)
            if escolha in cardapio:
                quantidade = input("Quantidade: ")
                if quantidade.isdigit():
                    quantidade = int(quantidade)
                    pedidos.append({"nome": cardapio[escolha]["nome"],
                                    "preco": cardapio[escolha]["preco"],
                                    "quantidade": quantidade})
                    print(str(quantidade) + "x " + cardapio[escolha]["nome"] + " adicionado!")
                else:
                    print("Quantidade inválida!")
            else:
                print("Código inválido!")
        else:
            print("Entrada inválida!")

    elif opcao == "2":
        print("\n--- Conta Final ---")
        total = 0
        for pedido in pedidos:
            subtotal = pedido["preco"] * pedido["quantidade"]
            print(str(pedido["quantidade"]) + "x " + pedido["nome"] + " - R$ " + str(subtotal))
            total += subtotal
        print("TOTAL: R$ " + str(total))
        print("Obrigado!")
        pedidos = []
        total = 0

    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
