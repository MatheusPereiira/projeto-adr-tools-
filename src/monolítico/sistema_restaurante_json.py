# sistema_restaurante_historico_simples.py

import json
import os

# Cardápio fixo
cardapio = {
    1: {"nome": "Hambúrguer", "preco": 15.0},
    2: {"nome": "Pizza", "preco": 25.0},
    3: {"nome": "Suco", "preco": 7.0},
    4: {"nome": "Refrigerante", "preco": 6.0}
}

ARQUIVO_PEDIDOS = "pedidos.json"

# Funções para manipulação do arquivo JSON
def carregar_pedidos():
    """Carrega pedidos do arquivo JSON, se existir."""
    if os.path.exists(ARQUIVO_PEDIDOS):
        with open(ARQUIVO_PEDIDOS, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def salvar_pedidos(pedidos):
    """Salva pedidos no arquivo JSON."""
    with open(ARQUIVO_PEDIDOS, "w", encoding="utf-8") as f:
        json.dump(pedidos, f, ensure_ascii=False, indent=4)

# Funções do sistema
def mostrar_cardapio():
    print("\n--- Cardápio ---")
    for codigo, item in cardapio.items():
        print(f"{codigo} - {item['nome']} (R$ {item['preco']:.2f})")

def fazer_pedido():
    mostrar_cardapio()
    escolha = int(input("Digite o código do item: "))
    quantidade = int(input("Quantidade: "))

    if escolha in cardapio:
        pedidos = carregar_pedidos()
        item = cardapio[escolha]
        pedidos.append({"nome": item["nome"], "preco": item["preco"], "quantidade": quantidade})
        salvar_pedidos(pedidos)
        print(f"V {quantidade}x {item['nome']} adicionado ao pedido.")
    else:
        print("X Código inválido!")

def fechar_conta():
    pedidos = carregar_pedidos()
    if not pedidos:
        print("\nNenhum pedido registrado.")
        return

    print("\n--- Conta Final ---")
    total = 0
    for pedido in pedidos:
        subtotal = pedido["preco"] * pedido["quantidade"]
        print(f"{pedido['quantidade']}x {pedido['nome']} - R$ {subtotal:.2f}")
        total += subtotal
    print(f"TOTAL: R$ {total:.2f}")
    print("Obrigado pela preferência!")

# Programa principal
while True:
    print("\n--- Restaurante Monolítico (Histórico) ---")
    print("1. Fazer Pedido")
    print("2. Fechar Conta")
    print("3. Ver Histórico de Pedidos")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        fazer_pedido()
    elif opcao == "2":
        fechar_conta()
    elif opcao == "3":
        pedidos = carregar_pedidos()
        if not pedidos:
            print("\nNenhum pedido registrado ainda.")
        else:
            print("\n--- Histórico de Pedidos ---")
            for p in pedidos:
                print(f"{p['quantidade']}x {p['nome']} - R$ {p['preco']*p['quantidade']:.2f}")
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")

