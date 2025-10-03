import socket, json

def request_integration_layer(payload):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 5004))
    client.send(json.dumps(payload).encode())
    resposta = client.recv(4096).decode()
    client.close()
    return json.loads(resposta)

def handle_request(data):
    req = json.loads(data)
    if req["acao"] == "mostrar_cardapio":
        return request_integration_layer({"acao": "obter_cardapio"})
    elif req["acao"] == "fazer_pedido":
        return request_integration_layer({"acao": "salvar_pedido", "item": req["item"]})
    elif req["acao"] == "mostrar_pedidos":
        return request_integration_layer({"acao": "obter_pedidos"})
    else:
        return {"erro": "Negócio desconhecido"}

def start_business_layer():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 5002))
    server.listen()
    print("Business Layer rodando na porta 5002...")
    while True:
        conn, _ = server.accept()
        data = conn.recv(4096).decode()
        resposta = json.dumps(handle_request(data))
        conn.send(resposta.encode())
        conn.close()

if __name__ == "__main__":
    start_business_layer()
