# Camada de abstração da fonte de dados
# Basta trocar a importação abaixo para mudar a implementação
# Esta camada atua como "ponte" para a camada de negócio
# integration.py
# Camada de integração - define funções intermediárias
# Basta trocar a importação para mudar a fonte de dados
# >>> TROQUE AQUI <<< #
#from data_layer_vector import cardapio, carregar_pedidos, salvar_pedidos, limpar_pedidos
from data_layer_json import cardapio, carregar_pedidos, salvar_pedidos, limpar_pedidos


def get_cardapio():
    """Retorna o cardápio vindo da camada de dados."""
    return cardapio


def get_pedidos():
    """Carrega os pedidos do Data Layer."""
    return carregar_pedidos()


def add_pedido(pedidos):
    """Salva os pedidos no Data Layer."""
    salvar_pedidos(pedidos)


def clear_pedidos():
    """Remove todos os pedidos do Data Layer."""
    limpar_pedidos()
