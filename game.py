import pygame
import sys
from sprites2 import sprites, initialize_sprites
from menu import character_selection_menu
from movement import handle_movement
from collision import check_full_collision
from config import screen_width, screen_height, initial_x_pos, initial_y_pos, velo, gravidade  # Importa as coordenadas iniciais
from fase import carregar_fase_1, desenhar_fase  # Importa as funções de fase.py

# Tamanho dos blocos (não será usado para blocos, mas para cálculos)
block_size = 16

# Função principal do jogo
def game_loop(screen, screen_width, screen_height):
    # Inicializa as sprites após a criação da tela
    initialize_sprites()

    # Chama a função de menu de seleção de personagens
    current_character = character_selection_menu(screen, screen_width, screen_height)

    # Carrega o plano de fundo e objetos da fase 1
    objetos_fase = carregar_fase_1()

    # Define a posição inicial do personagem com base nas coordenadas da config
    x_pos = initial_x_pos
    y_pos = initial_y_pos

    # Define a animação e o frame atuais
    current_animation = 'Idle'
    previous_animation = current_animation
    current_frame = 0
    frame_duration = 50  # 50ms por frame

    # Definir frame_width e frame_height inicialmente
    frame_width = sprites[current_character][current_animation][current_frame].get_width()
    frame_height = sprites[current_character][current_animation][current_frame].get_height()

    # Velocidade de movimento
    move_speed = velo

    # Variáveis de pulo e gravidade
    is_jumping = False
    is_falling = False
    jump_speed = -10  # Ajuste este valor para alterar o tamanho do pulo
    fall_speed = 0
    gravity = gravidade
    can_double_jump = True
    double_jump_activated = False  # Nova variável para controlar a ativação do pulo duplo
    jump_key_pressed = False  # Nova variável para controlar o estado da tecla de pulo

    # Direção inicial (True para direita, False para esquerda)
    facing_right = True

    # Inicia o relógio do Pygame
    clock = pygame.time.Clock()
    last_update_time = pygame.time.get_ticks()

    ### CORREÇÃO: Verifica a colisão inicial para posicionar o personagem corretamente ###
    # Verifica se o personagem está colidindo com o chão ou plataformas no início do jogo
    # Passamos dx = 0 e dy = 0, pois não há movimento inicial
    x_pos, y_pos, is_falling, is_jumping = check_full_collision(x_pos, y_pos, frame_width, frame_height, 0, 0, is_falling, is_jumping)

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

        # Inicializa as variáveis de movimento horizontal e vertical
        dx = 0
        dy = fall_speed if is_falling else 0  # Se estiver caindo, aplica a velocidade de queda

        # Atualiza a posição e a animação do personagem
        x_pos, y_pos, current_animation, facing_right, is_jumping, is_falling, fall_speed, jump_key_pressed, double_jump_activated = handle_movement(
            x_pos, y_pos, frame_width, frame_height, keys, current_animation, current_frame,
            facing_right, is_jumping, is_falling, jump_speed, fall_speed, gravity, move_speed,
            block_size, None, frame_duration, last_update_time, current_character, sprites, jump_key_pressed, double_jump_activated)

        # Define o movimento horizontal (dx) com base nas teclas pressionadas
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx = -move_speed  # Movendo-se para a esquerda
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = move_speed  # Movendo-se para a direita

        # Verifica colisão com o chão ou plataformas
        # Se o personagem não estiver pulando, verifica se ele está no ar (aplica gravidade)
        if not is_jumping:
            # Verifica se o personagem está no ar (não há colisão com o chão)
            dy = 1  # Movendo-se para baixo (gravidade)
            _, y_pos_after_collision, is_falling, _ = check_full_collision(x_pos, y_pos + 1, frame_width, frame_height, dx, dy, is_falling, is_jumping)

            if is_falling:  # Se o personagem está no ar, aplica a gravidade
                new_y_pos = y_pos + fall_speed
                dx = 0  # Sem movimento horizontal aqui para a gravidade
                dy = fall_speed  # Movendo-se para baixo com a velocidade da queda
                x_pos, y_pos, is_falling, is_jumping = check_full_collision(x_pos, new_y_pos, frame_width, frame_height, dx, dy, is_falling, is_jumping)
                fall_speed += gravity
            else:
                fall_speed = 0  # Para a queda se o personagem estiver no chão

        # Verifica colisão lateral (movimento horizontal)
        # Passa dx e dy para a função de colisão
        x_pos, y_pos, is_falling, is_jumping = check_full_collision(x_pos, y_pos, frame_width, frame_height, dx, 0, is_falling, is_jumping)

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
        # print(f"Animação atual: {current_animation}, Frame atual: {current_frame}")

        # Obtém a imagem do frame atual
        if current_frame >= len(sprites[current_character][current_animation]):
            current_frame = 0

        frame_image = sprites[current_character][current_animation][current_frame]

        # Espelha a imagem se estiver se movendo para a esquerda
        if not facing_right:
            frame_image = pygame.transform.flip(frame_image, True, False)

        # Desenha o fundo e os objetos da fase na tela
        desenhar_fase(screen, objetos_fase)  # Agora desenha o fundo e objetos da fase

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
pygame.display.set_caption("Jogo do PET")

# Chama a função principal do jogo
game_loop(screen, screen_width, screen_height)