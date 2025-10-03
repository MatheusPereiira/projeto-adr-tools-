import socket
import json

# Banco de dados em memória
cardapio = {
    1: {"nome": "Hambúrguer", "preco": 15.0},
    2: {"nome": "Pizza", "preco": 25.0},
    3: {"nome": "Suco", "preco": 7.0},
    4: {"nome": "Refrigerante", "preco": 6.0}
}
pedidos = []

def handle_request(data):
    req = json.loads(data)
    if req["acao"] == "listar_cardapio":
        return json.dumps(cardapio)
    elif req["acao"] == "adicionar_pedido":
        pedidos.append(cardapio[req["item"]])
        return json.dumps({"status": "ok"})
    elif req["acao"] == "listar_pedidos":
        return json.dumps(pedidos)
    else:
        return json.dumps({"erro": "Ação desconhecida"})

def start_data_layer():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
