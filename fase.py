import pygame
from config import screen_height, screen_width
from objeto import Objeto
objetos_fase=[]
# Função para carregar o plano de fundo e outros objetos da fase 1
def carregar_fase_1():
    #background_image = pygame.image.load('Sprites/plano de fundo.jpeg').convert()
    objetos_fase = [ Objeto(x=0, y=0, largura=screen_width, altura=screen_height, solido=False, imagem= 'Sprites/plano de fundo.jpeg', angulo=0),
                    Objeto(x=screen_width*0.2, y=0.35*screen_height, largura=screen_width*0.05, altura=screen_width*0.05, solido=False, imagem= 'Sprites/lampada_desligada.png', angulo=180),
                    Objeto(x=screen_width*0.667, y=0.08*screen_height, largura=screen_width*0.05, altura=screen_width*0.05, solido=False, imagem= 'Sprites/coração.png', angulo=0),
                    Objeto(x=screen_width*0, y=0.90*screen_height, largura=screen_width, altura=screen_width*0.08, solido=True, imagem= 'Sprites/plataformas juntas teste (32x8).png', angulo=0)

                   ]
    #novo metodo de alocação de imagem de forma mais dinâmica
    for i in range(len(objetos_fase)):
        objetos_fase[i].imagem=pygame.image.load(objetos_fase[i].imagem).convert()
        objetos_fase[i].imagem.set_colorkey((0, 0, 0))  # Define a cor preta como transparente (R: 0, G: 0, B: 0)
        objetos_fase[i].imagem=pygame.transform.scale(objetos_fase[i].imagem, (objetos_fase[i].largura,objetos_fase[i].altura))#redimensionando
        objetos_fase[i].imagem=pygame.transform.rotate(objetos_fase[i].imagem, objetos_fase[i].angulo)#rotacionando
    # Carrega objetos da fase 1
    #plataforma = pygame.Rect(150, 450, 250, 20)  # Exemplo de uma plataforma
    #preciso melhorar essa parte usando um for e matriz para ficar menor e mais tranquilo de criar novos
    #realizando configuração da imagem da lâmpada
    
    
    return objetos_fase
def carregar_fase_1_mapeamento():
    #background_image = pygame.image.load('Sprites/plano de fundo.jpeg').convert()
    objetos_fase = [ Objeto(x=0, y=0, largura=screen_width, altura=screen_height, solido=False, imagem= 'Sprites/plano de fundo.jpeg', angulo=0),
                    Objeto(x=screen_width*0.2, y=0.35*screen_height, largura=screen_width*0.05, altura=screen_width*0.05, solido=False, imagem= 'Sprites/lampada_desligada.png', angulo=180),
                    Objeto(x=screen_width*0.667, y=0.08*screen_height, largura=screen_width*0.05, altura=screen_width*0.05, solido=False, imagem= 'Sprites/coração.png', angulo=0),
                    Objeto(x=screen_width*0, y=0.90*screen_height, largura=screen_width, altura=screen_width*0.08, solido=True, imagem= 'Sprites/plataformas juntas teste (32x8).png', angulo=0)

                   ]
    #novo metodo de alocação de imagem de forma mais dinâmica
    
    #plataforma = pygame.Rect(150, 450, 250, 20)  # Exemplo de uma plataforma
    #preciso melhorar essa parte usando um for e matriz para ficar menor e mais tranquilo de criar novos
    #realizando configuração da imagem da lâmpada
    
    
    return objetos_fase

# Função para desenhar a fase (plano de fundo e objetos)
def desenhar_fase(screen, objetos_fase):
    # Desenha o plano de fundo
    #screen.blit(background_image, (0, 0))

    # Desenha os objetos da fase (ex: plataformas)
    for objeto in objetos_fase:
        screen.blit(objeto.imagem, (objeto.x, objeto.y))  # Desenha as plataformas em vermelho