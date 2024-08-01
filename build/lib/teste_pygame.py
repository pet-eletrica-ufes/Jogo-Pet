# exemplo_pygame.py
import pygame
import sys

# Inicialização do pygame
pygame.init()

# Configurações da janela
size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Exemplo PyGame")

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preenchendo a tela com uma cor (azul)
    screen.fill((0, 0, 255))
    
    # Atualizando a tela
    pygame.display.flip()

# Finalizando o pygame
pygame.quit()
sys.exit()
