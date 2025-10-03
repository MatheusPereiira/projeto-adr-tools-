# business_layer.py
from data_layer import cardapio, carregar_pedidos, salvar_pedidos

# Carrega pedidos já existentes
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
        salvar_pedidos(pedidos)  # sempre salva após novo pedido
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


def limpar_pedidos():
    pedidos.clear()
    salvar_pedidos(pedidos)  # limpa também no JSON

