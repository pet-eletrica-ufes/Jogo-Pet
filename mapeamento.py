# mapeamento_de_imagem.py
from objeto import Objeto
import fase
objetos=fase.carregar_fase_1_mapeamento()
def obter_plataformas():
    """
    Retorna uma lista de objetos do tipo Objeto, que representam as plataformas no jogo.
    """
    plataformas = [
        #Objeto(x=0, y=782, largura=1060, altura=10, solido=True),  # Plataforma de baixo ao lado do bloco
        #Objeto(x=1061, y=681, largura=219, altura=111, solido=True),# Bloco do lado da plataforma
        #Objeto(x=0, y=507, largura=1060, altura=32, solido=True),
        #Objeto(x=218, y=235, largura=1066, altura=40, solido=True),
          
    ]
    # Carregar as plataformas a partir da imagem
    #objetos_fase = carregar_fase_1()  # Pega a imagem da fase 1
    #objetos=fase.objetos_fase
    for objeto in objetos:
        if objeto.solido:  # Se o objeto for sólido, adiciona-o à lista de plataformas
            plataformas.append(objeto)
    #verifica a possibilidade de criar outra mecanica para carregar collision
    return plataformas
    
    

def obter_paredes():
    """
    Retorna uma lista de objetos do tipo Objeto, que representam as paredes no jogo.
    """
    paredes = [
        # Exemplo de uma parede, se necessário no futuro
        # Objeto(x=50, y=100, largura=10, altura=500, solido=True),
    ]
    return paredes

def obter_objetos_acao():
    """
    Retorna uma lista de objetos que possuem ações associadas (por exemplo, interruptores, portas, etc.).
    """
    objetos_acao = [
        #Objeto(x=500, y=500, largura=50, altura=50, solido=False, acao=True),  # Exemplo de um objeto com ação
    ]
    return objetos_acao