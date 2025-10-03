import socket
import json

def request_business_layer(payload):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 5002))
    client.send(json.dumps(payload).encode())
    resposta = client.recv(4096).decode()
    client.close()
    return json.loads(resposta)

def handle_request(data):
    req = json.loads(data)
    
    if req["acao"] == "obter_cardapio":
        return request_business_layer({"acao": "mostrar_cardapio"})
    
    elif req["acao"] == "registrar_pedido":
        return request_business_layer({"acao": "fazer_pedido", "item": req["item"]})
    
    elif req["acao"] == "obter_pedidos":
        return request_business_layer({"acao": "mostrar_pedidos"})
    
    else:
        return {"erro": "Serviço não reconhecido"}

def start_service_layer():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 5003))
    server.listen()
    print("Service Layer rodando na porta 5003...")
    
    while True:
        conn, _ = server.accept()
        data = conn.recv(4096).decode()
        resposta = json.dumps(handle_request(data))
        conn.send(resposta.encode())
        conn.close()

if __name__ == "__main__":
    start_service_layer()
