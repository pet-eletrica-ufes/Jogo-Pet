import pygame
from config import screen_height, screen_width
from objeto import Objeto
objetos_fase_1=[ Objeto(x=0, y=0, largura=screen_width, altura=screen_height, solido=False, imagem= 'Sprites/fundo.jpg', angulo=0),
                    Objeto(x=screen_width*0.2, y=0.35*screen_height, largura=screen_width*0.05, altura=screen_width*0.05, solido=False, imagem= 'Sprites/lampada_desligada.png', angulo=180),
                    Objeto(x=screen_width*0.667, y=0.08*screen_height, largura=screen_width*0.05, altura=screen_width*0.05, solido=False, imagem= 'Sprites/coração.png', angulo=0),
                    Objeto(x=screen_width*0, y=0.973*screen_height, largura=screen_width*0.8, altura=screen_width*0.027, solido=True, imagem= 'Sprites/plataformas/plataforma_chao.png', angulo=0,correc_altura=0.5),
                    Objeto(x=screen_width*0.8, y=0.865*screen_height, largura=screen_width*0.2, altura=screen_width*0.14, solido=True, imagem= 'Sprites/plataformas/caixa.png', angulo=0),
                    Objeto(x=screen_width*0, y=0.5*screen_height, largura=screen_width*0.8, altura=screen_width*0.04, solido=True, imagem= 'Sprites/plataformas/plataforma_esquerda.png', angulo=0,correc_altura=0.5),
                    Objeto(x=screen_width*0.2, y=0.2*screen_height, largura=screen_width*0.8, altura=screen_width*0.04, solido=True, imagem= 'Sprites/plataformas/plataforma_direita.png', angulo=0,correc_altura=0.5)


                   ]
# Função para carregar o plano de fundo e outros objetos da fase 1
def carregar_fase_1():
    #background_image = pygame.image.load('Sprites/plano de fundo.jpeg').convert()
    #novo metodo de alocação de imagem de forma mais dinâmica
    for i in range(len(objetos_fase_1)):
        objetos_fase_1[i].imagem=pygame.image.load(objetos_fase_1[i].imagem).convert()
        objetos_fase_1[i].imagem.set_colorkey((0, 0, 0))  # Define a cor preta como transparente (R: 0, G: 0, B: 0)
        objetos_fase_1[i].imagem=pygame.transform.scale(objetos_fase_1[i].imagem, (objetos_fase_1[i].largura,objetos_fase_1[i].altura))#redimensionando
        objetos_fase_1[i].imagem=pygame.transform.rotate(objetos_fase_1[i].imagem, objetos_fase_1[i].angulo)#rotacionando
    # Carrega objetos da fase 1
    #plataforma = pygame.Rect(150, 450, 250, 20)  # Exemplo de uma plataforma
    #preciso melhorar essa parte usando um for e matriz para ficar menor e mais tranquilo de criar novos
    #realizando configuração da imagem da lâmpada
    
    
    return objetos_fase_1
def carregar_fase_1_mapeamento():
    #background_image = pygame.image.load('Sprites/plano de fundo.jpeg').convert()
    
    #novo metodo de alocação de imagem de forma mais dinâmica
    
    #plataforma = pygame.Rect(150, 450, 250, 20)  # Exemplo de uma plataforma
    #preciso melhorar essa parte usando um for e matriz para ficar menor e mais tranquilo de criar novos
    #realizando configuração da imagem da lâmpada
    
    
    return objetos_fase_1

# Função para desenhar a fase (plano de fundo e objetos)
def desenhar_fase(screen, objetos_fase):
    # Desenha o plano de fundo
    #screen.blit(background_image, (0, 0))

    # Desenha os objetos da fase (ex: plataformas)
    for objeto in objetos_fase:
        screen.blit(objeto.imagem, (objeto.x, objeto.y))  # Desenha as plataformas em vermelho