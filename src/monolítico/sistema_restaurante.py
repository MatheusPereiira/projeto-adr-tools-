# sistema_restaurante.py

# Cardápio fixo
cardapio = {
    1: {"nome": "Hambúrguer", "preco": 15.0},
    2: {"nome": "Pizza", "preco": 25.0},
    3: {"nome": "Suco", "preco": 7.0},
    4: {"nome": "Refrigerante", "preco": 6.0}
}

# Lista de pedidos
pedidos = []


def mostrar_cardapio():
    print("\n--- Cardápio ---")
    for codigo, item in cardapio.items():
        print(f"{codigo} - {item['nome']} (R$ {item['preco']:.2f})")


def fazer_pedido():
    mostrar_cardapio()
    escolha = int(input("Digite o código do item: "))
    quantidade = int(input("Quantidade: "))

    if escolha in cardapio:
        item = cardapio[escolha]
        pedidos.append({"nome": item["nome"], "preco": item["preco"], "quantidade": quantidade})
        print(f"V {quantidade}x {item['nome']} adicionado ao pedido.")
    else:
        print("X Código inválido!")


def fechar_conta():
    print("\n--- Conta Final ---")
    total = 0
    for pedido in pedidos:
        subtotal = pedido["preco"] * pedido["quantidade"]
        print(f"{pedido['quantidade']}x {pedido['nome']} - R$ {subtotal:.2f}")
        total += subtotal
    print(f"TOTAL: R$ {total:.2f}")
    print("Obrigado pela preferência!")


# Programa principal (tudo no mesmo arquivo)
while True:
    print("\n--- Restaurante Monolítico ---")
    print("1. Fazer Pedido")
    print("2. Fechar Conta")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        fazer_pedido()
    elif opcao == "2":
        fechar_conta()
        pedidos.clear()  # limpa para próximo cliente
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
