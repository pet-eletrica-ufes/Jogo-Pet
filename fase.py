import pygame

# Função para carregar o plano de fundo e outros objetos da fase 1
def carregar_fase_1():
    background_image = pygame.image.load('Sprites/plano de fundo.jpeg').convert()
    objetos_fase = []

    # Carrega objetos da fase 1
    plataforma = pygame.Rect(150, 450, 250, 20)  # Exemplo de uma plataforma
    lampada_image = pygame.image.load('Sprites/lampadas_desligada.png').convert()  # Usa convert() para otimizar
    lampada_image.set_colorkey((0, 0, 0))  # Define a cor preta como transparente (R: 0, G: 0, B: 0)
    objetos_fase.append(lampada_image)

    return background_image, objetos_fase

# Função para desenhar a fase (plano de fundo e objetos)
def desenhar_fase(screen, background_image, objetos_fase):
    # Desenha o plano de fundo
    screen.blit(background_image, (0, 0))

    # Desenha os objetos da fase (ex: plataformas)
    for objeto in objetos_fase:
        screen.blit(objeto, (100, 100))  # Desenha as plataformas em vermelho