import pygame
from config import screen_height, screen_width
from objeto import Objeto

# Função para carregar o plano de fundo e outros objetos da fase 1
def carregar_fase_1():
    background_image = pygame.image.load('Sprites/plano de fundo.jpeg').convert()
    objetos_fase = [Objeto(x=120, y=130, largura=screen_width*0.05, altura=screen_width*0.05, solido=False, imagem= None, angulo=180),
                    Objeto(x=400, y=30, largura=screen_width*0.05, altura=screen_width*0.05, solido=False, imagem= None, angulo=0)]
    imagens=['Sprites/lampada_desligada.png','Sprites/coração.png']
    #novo metodo de alocação de imagem de forma mais dinâmica
    for i in range(len(objetos_fase)):
        objetos_fase[i].imagem=pygame.image.load(imagens[i]).convert()
        objetos_fase[i].imagem.set_colorkey((0, 0, 0))  # Define a cor preta como transparente (R: 0, G: 0, B: 0)
        objetos_fase[i].imagem=pygame.transform.scale(objetos_fase[i].imagem, (objetos_fase[i].largura,objetos_fase[i].altura))#redimensionando
        objetos_fase[i].imagem=pygame.transform.rotate(objetos_fase[i].imagem, objetos_fase[i].angulo)#rotacionando
    # Carrega objetos da fase 1
    #plataforma = pygame.Rect(150, 450, 250, 20)  # Exemplo de uma plataforma
    #preciso melhorar essa parte usando um for e matriz para ficar menor e mais tranquilo de criar novos
    #realizando configuração da imagem da lâmpada
    
    
    return background_image, objetos_fase

# Função para desenhar a fase (plano de fundo e objetos)
def desenhar_fase(screen, background_image, objetos_fase):
    # Desenha o plano de fundo
    screen.blit(background_image, (0, 0))

    # Desenha os objetos da fase (ex: plataformas)
    for objeto in objetos_fase:
        screen.blit(objeto.imagem, (objeto.x, objeto.y))  # Desenha as plataformas em vermelho