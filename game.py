import pygame
import sys
from sprites2 import sprites, initialize_sprites, terrain_blocks
from menu import character_selection_menu
from level import level_layout
from movement import handle_movement
from collision import check_full_collision

# Dimensões da tela
screen_width = 600
screen_height = 600

# Tamanho dos blocos
block_size = 16

# Função principal do jogo
def game_loop(screen, screen_width, screen_height):
    # Inicializa as sprites após a criação da tela
    initialize_sprites()

    # Chama a função de menu de seleção de personagens
    current_character = character_selection_menu(screen, screen_width, screen_height)

    # Encontrando a terceira posição com zero de baixo para cima e da esquerda para a direita
    zero_positions = []
    for row_index in range(len(level_layout)-1, -1, -1):
        for col_index in range(len(level_layout[row_index])):
            if level_layout[row_index][col_index] == 0:
                # Verificar se há um quadrado de 3x3 com zeros a partir dessa posição
                if (row_index - 2 >= 0 and col_index + 2 < len(level_layout[row_index]) and
                    level_layout[row_index-1][col_index] == 0 and
                    level_layout[row_index-2][col_index] == 0 and
                    level_layout[row_index][col_index+1] == 0 and
                    level_layout[row_index-1][col_index+1] == 0 and
                    level_layout[row_index-2][col_index+1] == 0 and
                    level_layout[row_index][col_index+2] == 0 and
                    level_layout[row_index-1][col_index+2] == 0 and
                    level_layout[row_index-2][col_index+2] == 0):
                    
                    zero_positions.append((col_index, row_index))
                
                if len(zero_positions) == 3:
                    break
        if len(zero_positions) == 3:
            break

    # Se encontrarmos a terceira posição com zero que atende às condições
    if len(zero_positions) == 3:
        third_zero_col, third_zero_row = zero_positions[2]
        # Definindo a posição inicial no zero central do quadrado de 3x3
        x_pos = (third_zero_col + 1) * block_size
        y_pos = (third_zero_row - 1) * block_size
    else:
        # Caso não haja três posições com zero que atendam às condições, definir uma posição padrão
        x_pos = block_size * 2
        y_pos = screen_height - block_size * 3

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
    ground_level = screen_height // 2
    can_double_jump = True
    double_jump_activated = False  # Nova variável para controlar a ativação do pulo duplo
    jump_key_pressed = False  # Nova variável para controlar o estado da tecla de pulo

    # Direção inicial (True para direita, False para esquerda)
    facing_right = True

    # Inicia o relógio do Pygame
    clock = pygame.time.Clock()
    last_update_time = pygame.time.get_ticks()

    # Verificar e corrigir posição inicial do personagem
    if check_full_collision(x_pos, y_pos, frame_width, frame_height, level_layout, block_size):
        while check_full_collision(x_pos, y_pos, frame_width, frame_height, level_layout, block_size):
            y_pos -= 1  # Tentar mover o personagem para cima até sair do bloco

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
            block_size, level_layout, frame_duration, last_update_time, current_character, sprites, jump_key_pressed, double_jump_activated)

        # Limite de movimentação para não ultrapassar as bordas da janela
        if x_pos < 5:
            x_pos = 5
        elif x_pos > screen_width - frame_width - 5:
            x_pos = screen_width - frame_width - 5

        if y_pos < 0:
            y_pos = 0
        elif y_pos > screen_height - frame_height - 5:
            y_pos = screen_height - frame_height - 5

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

        # Obtém a imagem do frame atual
        if current_frame >= len(sprites[current_character][current_animation]):
            current_frame = 0

        frame_image = sprites[current_character][current_animation][current_frame]

        # Espelha a imagem se estiver se movendo para a esquerda
        if not facing_right:
            frame_image = pygame.transform.flip(frame_image, True, False)

        # Desenha a imagem na tela
        screen.fill((0, 0, 0))  # Limpa a tela

        # Desenha a fase
        for row_index, row in enumerate(level_layout):
            for col_index, cell in enumerate(row):
                if cell == 1:
                    block = terrain_blocks[12]  # Usar o primeiro bloco de terreno como exemplo
                    screen.blit(block, (col_index * block_size, row_index * block_size))

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