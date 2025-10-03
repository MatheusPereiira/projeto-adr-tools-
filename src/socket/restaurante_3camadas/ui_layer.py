import socket
import json

def request_business_layer(payload):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 5002))
    client.send(json.dumps(payload).encode())
    resposta = client.recv(4096).decode()
    client.close()
    return json.loads(resposta)

def menu():
    while True:
        print("\n=== Sistema Restaurante ===")
        print("1 - Mostrar Cardápio")
        print("2 - Fazer Pedido")
        print("3 - Mostrar Pedidos")
        print("0 - Sair")
        
        opcao = input("Escolha: ")
        
        if opcao == "1":
            cardapio = request_business_layer({"acao": "mostrar_cardapio"})
            for k, v in cardapio.items():
                print(f"{k} - {v['nome']} : R${v['preco']}")
        
        elif opcao == "2":
            item = int(input("Digite o número do item: "))
            resposta = request_business_layer({"acao": "fazer_pedido", "item": item})
            print("Pedido realizado:", resposta)
        
        elif opcao == "3":
            pedidos = request_business_layer({"acao": "mostrar_pedidos"})
            print("Pedidos feitos:")
            for p in pedidos:
                print(f"- {p['nome']} (R${p['preco']})")
        
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
