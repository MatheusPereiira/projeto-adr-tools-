
import socket
import json
import os

cardapio = {
    1: {"nome": "Hambúrguer", "preco": 15.0},
    2: {"nome": "Pizza", "preco": 25.0},
    3: {"nome": "Suco", "preco": 7.0},
    4: {"nome": "Refrigerante", "preco": 6.0}
}

ARQUIVO_PEDIDOS = "pedidos.json"


def carregar_pedidos():
    """Carrega os pedidos do arquivo JSON, se existir."""
    if os.path.exists(ARQUIVO_PEDIDOS):
        with open(ARQUIVO_PEDIDOS, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def salvar_pedidos(pedidos):
    """Salva a lista de pedidos no arquivo JSON."""
    with open(ARQUIVO_PEDIDOS, "w", encoding="utf-8") as f:
        json.dump(pedidos, f, ensure_ascii=False, indent=4)


def handle_request(data):
    pedidos = carregar_pedidos()
    req = json.loads(data)

    if req["acao"] == "listar_cardapio":
        return json.dumps(cardapio, ensure_ascii=False, indent=4)

    elif req["acao"] == "adicionar_pedido":
        if req["item"] in cardapio:
            pedidos.append(cardapio[req["item"]])
            salvar_pedidos(pedidos)
            return json.dumps({"status": "ok"})
        else:
            return json.dumps({"erro": "Item inválido"})

    elif req["acao"] == "listar_pedidos":
        return json.dumps(pedidos, ensure_ascii=False, indent=4)

    else:
        return json.dumps({"erro": "Ação desconhecida"})


def start_data_layer():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("localhost", 5001))
    server.listen()
    print("Data Layer rodando na porta 5001...")

    while True:
        conn, _ = server.accept()
        data = conn.recv(4096).decode()
        resposta = handle_request(data)
        conn.send(resposta.encode())
        conn.close()


if __name__ == "__main__":
    start_data_layer()
