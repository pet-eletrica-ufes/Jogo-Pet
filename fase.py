import pygame
from config import screen_height, screen_width
from objeto import Objeto

# Função para carregar o plano de fundo e outros objetos da fase 1
def carregar_fase_1():
    background_image = pygame.image.load('Sprites/plano de fundo.jpeg').convert()
    objetos_fase = [Objeto(x=120, y=130, largura=screen_width*0.05, altura=screen_width*0.05, solido=False, imagem= ),]

    # Carrega objetos da fase 1
    #plataforma = pygame.Rect(150, 450, 250, 20)  # Exemplo de uma plataforma
    lampada_image = pygame.image.load('Sprites/lampada_desligada.png').convert()  # Usa convert() para otimizar
    lampada_image.set_colorkey((0, 0, 0))  # Define a cor preta como transparente (R: 0, G: 0, B: 0)
    lampada_image = pygame.transform.scale(lampada_image, (screen_width*0.05,screen_width*0.05))#redimensionando
    lampada_image = pygame.transform.rotate(lampada_image, 180)#rotacionando
    objetos_fase.append(lampada_image)
    #aqui vai bugar, tenha certeza disso, anotação para corrigir o bug que vai dar aqui!é pq o objeto não foi bem elaborado, tem que ajustar nas outras partes

    return background_image, objetos_fase

# Função para desenhar a fase (plano de fundo e objetos)
def desenhar_fase(screen, background_image, objetos_fase):
    # Desenha o plano de fundo
    screen.blit(background_image, (0, 0))

    # Desenha os objetos da fase (ex: plataformas)
    for objeto in objetos_fase:
        screen.blit(objeto, (120, 130))  # Desenha as plataformas em vermelho