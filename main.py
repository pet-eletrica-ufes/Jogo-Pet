import pygame
import game
from config import screen_width, screen_height

# Inicializa o Pygame
pygame.init()



# Cria a janela com as dimensões especificadas
screen = pygame.display.set_mode((screen_width, screen_height))

# Chama a função principal do jogo
game.game_loop(screen, screen_width, screen_height)