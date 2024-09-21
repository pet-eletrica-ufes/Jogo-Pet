import pygame
import sys
from sprites2 import sprites, initialize_sprites
from menu import character_selection_menu
from movement import handle_movement
from collision import check_full_collision
from config import screen_width, screen_height
# Dimensões da tela


# Tamanho dos blocos (não será usado para blocos, mas para cálculos)
block_size = 16

# Função principal do jogo
def game_loop(screen, screen_width, screen_height):
    # Inicializa as sprites após a criação da tela
    initialize_sprites()

    # Chama a função de menu de seleção de personagens
    current_character = character_selection_menu(screen, screen_width, screen_height)

    # Carrega a imagem de fundo
    background_image = pygame.image.load('plano de fundo.jpeg').convert()

    # Define a posição inicial do personagem na parte inferior da tela
    x_pos = screen_width // 2
    y_pos = screen_height - block_size * 4  # Ajuste para estar um pouco acima da base da tela

    # Define a animação e o frame atuais
    current_animation = 'Idle'
    previous_animation = current_animation
    current_frame = 0
    frame_duration = 50  # 50ms por frame

    # Definir frame_width e frame_height inicialmente
    frame_width = sprites[current_character][current_animation][current_frame].get_width()
    frame_height = sprites[current_character][current_animation][current_frame].get_height()

    # Velocidade de movimento
    move_speed = 5

    # Variáveis de pulo e gravidade
    is_jumping = False
    is_falling = False
    jump_speed = -10  # Ajuste este valor para alterar o tamanho do pulo
    fall_speed = 0
    gravity = 1
    ground_level = screen_height - frame_height  # Define o nível do "chão"
    can_double_jump = True
    double_jump_activated = False  # Nova variável para controlar a ativação do pulo duplo
    jump_key_pressed = False  # Nova variável para controlar o estado da tecla de pulo

    # Direção inicial (True para direita, False para esquerda)
    facing_right = True

    # Inicia o relógio do Pygame
    clock = pygame.time.Clock()
    last_update_time = pygame.time.get_ticks()

    # Loop principal do jogo
    running = True
    while running:
        # Verifica eventos (como o fechamento da janela)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_w, pygame.K_UP, pygame.K_SPACE):
                    jump_key_pressed = False  # Marca a tecla de pulo como liberada

        # Obtém o estado das teclas
        keys = pygame.key.get_pressed()

        # Atualiza a posição e a animação do personagem
        x_pos, y_pos, current_animation, facing_right, is_jumping, is_falling, fall_speed, jump_key_pressed, double_jump_activated = handle_movement(
            x_pos, y_pos, frame_width, frame_height, keys, current_animation, current_frame,
            facing_right, is_jumping, is_falling, jump_speed, fall_speed, gravity, move_speed,
            block_size, None, frame_duration, last_update_time, current_character, sprites, jump_key_pressed, double_jump_activated)

        # Limite de movimentação para não ultrapassar as bordas da janela
        if x_pos < 5:
            x_pos = 5
        elif x_pos > screen_width - frame_width - 5:
            x_pos = screen_width - frame_width - 5

        # Impedir que o personagem caia abaixo do "chão"
        if y_pos > ground_level:
            y_pos = ground_level
            is_falling = False
            fall_speed = 0
            is_jumping = False
            can_double_jump = True  # Reseta a possibilidade de pulo duplo quando atinge o chão

        # Verifica se a animação mudou
        if current_animation != previous_animation:
            current_frame = 0
            previous_animation = current_animation

        # Obtém o tempo atual
        current_time = pygame.time.get_ticks()

        # Atualiza o frame se o tempo por frame tiver passado
        if current_time - last_update_time > frame_duration:
            current_frame = (current_frame + 1) % len(sprites[current_character][current_animation])
            last_update_time = current_time

        # Verificação de depuração
        #print(f"Animação atual: {current_animation}, Frame atual: {current_frame}")

        # Obtém a imagem
                # Obtém a imagem do frame atual
        if current_frame >= len(sprites[current_character][current_animation]):
            current_frame = 0

        frame_image = sprites[current_character][current_animation][current_frame]

        # Espelha a imagem se estiver se movendo para a esquerda
        if not facing_right:
            frame_image = pygame.transform.flip(frame_image, True, False)

        # Desenha o fundo e o personagem na tela
        screen.blit(background_image, (0, 0))  # Desenha o fundo na tela

        # Desenha o personagem na tela
        screen.blit(frame_image, (x_pos, y_pos))

        # Atualiza a tela
        pygame.display.flip()

        # Controla a taxa de atualização
        clock.tick(60)

    # Sai do Pygame
    pygame.quit()
    sys.exit()

# Inicializa o Pygame e configura a tela
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jogo de Plataforma")

# Chama a função principal do jogo
game_loop(screen, screen_width, screen_height)