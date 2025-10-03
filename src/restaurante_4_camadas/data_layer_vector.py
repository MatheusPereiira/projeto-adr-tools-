# data_layer_vector.py
# Implementação simples em memória (vetor/lista)

cardapio = {
    1: {"nome": "Hambúrguer", "preco": 15.0},
    2: {"nome": "Pizza", "preco": 25.0},
    3: {"nome": "Suco", "preco": 7.0},
    4: {"nome": "Refrigerante", "preco": 6.0}
}

pedidos = []


def carregar_pedidos():
    return pedidos


def salvar_pedidos(novos_pedidos):
    global pedidos
    pedidos = novos_pedidos


def limpar_pedidos():
    global pedidos
    pedidos = []

