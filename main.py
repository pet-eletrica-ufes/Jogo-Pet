import pygame
import game

# Inicializa o Pygame
pygame.init()

# Define as dimensões da janela
screen_width = 600
screen_height = 600

# Cria a janela com as dimensões especificadas
screen = pygame.display.set_mode((screen_width, screen_height))

# Chama a função principal do jogo
game.game_loop(screen, screen_width, screen_height)