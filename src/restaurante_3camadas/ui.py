# app.py
from business_layer import listar_cardapio, adicionar_pedido, calcular_conta, limpar_pedidos

while True:
    print("\n--- Restaurante (3 camadas) ---")
    print("1. Fazer Pedido")
    print("2. Fechar Conta")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n--- Cardápio ---")
        for codigo, item in listar_cardapio().items():
            print(f"{codigo} - {item['nome']} (R$ {item['preco']:.2f})")

        try:
            escolha = int(input("Digite o código do item: "))
            quantidade = int(input("Quantidade: "))
            if adicionar_pedido(escolha, quantidade):
                print(f"{quantidade}x {listar_cardapio()[escolha]['nome']} adicionado!")
            else:
                print("Código inválido!")
        except ValueError:
            print("Entrada inválida!")

    elif opcao == "2":
        detalhes, total = calcular_conta()
        print("\n--- Conta Final ---")
        for qtd, nome, subtotal in detalhes:
            print(f"{qtd}x {nome} - R$ {subtotal:.2f}")
        print(f"TOTAL: R$ {total:.2f}")
        print("Obrigado pela preferência!")
        limpar_pedidos()

    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
