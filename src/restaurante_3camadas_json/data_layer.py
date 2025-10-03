# data_layer.py
import json
import os

cardapio = {
    1: {"nome": "Hambúrguer", "preco": 15.0},
    2: {"nome": "Pizza", "preco": 25.0},
    3: {"nome": "Suco", "preco": 7.0},
    4: {"nome": "Refrigerante", "preco": 6.0}
}

PEDIDOS_FILE = "pedidos.json"


def carregar_pedidos():
    """Carrega os pedidos do arquivo JSON, se existir."""
    if os.path.exists(PEDIDOS_FILE):
        with open(PEDIDOS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salvar_pedidos(pedidos):
    """Salva os pedidos no arquivo JSON."""
    with open(PEDIDOS_FILE, "w", encoding="utf-8") as f:
        json.dump(pedidos, f, indent=4, ensure_ascii=False)

