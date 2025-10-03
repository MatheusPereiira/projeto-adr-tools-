# business_layer.py
from integration_layer import cardapio, carregar_pedidos, salvar_pedidos, limpar_pedidos

pedidos = carregar_pedidos()


def listar_cardapio():
    return cardapio


def adicionar_pedido(codigo, quantidade):
    if codigo in cardapio:
        item = cardapio[codigo]
        pedidos.append({
            "nome": item["nome"],
            "preco": item["preco"],
            "quantidade": quantidade
        })
        salvar_pedidos(pedidos)
        return True
    return False


def calcular_conta():
    total = 0
    detalhes = []
    for pedido in pedidos:
        subtotal = pedido["preco"] * pedido["quantidade"]
        detalhes.append((pedido["quantidade"], pedido["nome"], subtotal))
        total += subtotal
    return detalhes, total


def fechar_conta():
    detalhes, total = calcular_conta()
    limpar_pedidos()
    return detalhes, total
