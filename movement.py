import pygame
from collision import check_full_collision

def handle_movement(x_pos, y_pos, frame_width, frame_height, keys, current_animation, current_frame,
                    facing_right, is_jumping, is_falling, jump_speed, fall_speed, gravity, move_speed,
                    block_size, level_layout, frame_duration, last_update_time, current_character, sprites,
                    jump_key_pressed, double_jump_activated):

    # Inicializa as variáveis de movimento
    dx = 0  # Movimento horizontal
    dy = 0  # Movimento vertical

    # Movimentação para a esquerda
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        dx = -move_speed  # Movendo-se para a esquerda
        new_x_pos = x_pos + dx
        x_pos, _, _, _ = check_full_collision(new_x_pos, y_pos, frame_width, frame_height, dx, dy, is_falling, is_jumping)
        if not is_jumping and not is_falling:
            current_animation = 'Run'
        facing_right = False

    # Movimentação para a direita
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        dx = move_speed  # Movendo-se para a direita
        new_x_pos = x_pos + dx
        x_pos, _, _, _ = check_full_collision(new_x_pos, y_pos, frame_width, frame_height, dx, dy, is_falling, is_jumping)
        if not is_jumping and not is_falling:
            current_animation = 'Run'
        facing_right = True

    # Pulo
    if keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE]:
        if not is_jumping and not is_falling and not jump_key_pressed:
            is_jumping = True
            fall_speed = jump_speed
            dy = fall_speed  # Aplicar o pulo ao movimento vertical
            current_animation = 'Jump'
            double_jump_activated = False  # Reset da ativação do pulo duplo
            jump_key_pressed = True  # Marca a tecla de pulo como pressionada
        elif is_jumping and not double_jump_activated and not jump_key_pressed:
            is_jumping = True
            fall_speed = jump_speed
            dy = fall_speed  # Aplicar o pulo ao movimento vertical
            current_animation = 'Double Jump'
            double_jump_activated = True  # Ativa o pulo duplo
            jump_key_pressed = True  # Marca a tecla de pulo como pressionada

    # Se a tecla de pulo foi liberada, permitir novo pulo duplo
    if not (keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE]):
        jump_key_pressed = False

    # Verifica se o personagem está no chão (não está pulando nem caindo)
    dy = 1  # Movendo-se para baixo para verificar colisão com o chão
    _, y_pos_after_collision, is_falling, _ = check_full_collision(x_pos, y_pos + dy, frame_width, frame_height, dx, dy, is_falling, is_jumping)

    if not is_falling and not is_jumping:
        # Se o personagem não estiver caindo nem pulando, ele está no chão
        fall_speed = 0
    else:
        # Se houver uma queda, aplica a gravidade
        is_falling = True

    # Movimentação vertical (queda)
    if is_falling:
        #print("entrou em queda!")
        dy = fall_speed  # Aplicar a gravidade
        new_y_pos = y_pos + dy
        x_pos, y_pos, is_falling, is_jumping = check_full_collision(x_pos, new_y_pos, frame_width, frame_height, dx, dy, is_falling, is_jumping)
        fall_speed += gravity
        if not is_falling:
            current_animation = 'Idle'
            double_jump_activated = False  # Reset da ativação do pulo duplo

    # Verificação de colisão ao pular
    if is_jumping:
        dy = fall_speed  # Aplicar a velocidade do pulo
        new_y_pos = y_pos + dy
        x_pos, y_pos, is_falling, is_jumping = check_full_collision(x_pos, new_y_pos, frame_width, frame_height, dx, dy, is_falling, is_jumping)
        fall_speed += gravity
        if not is_jumping:
            is_falling = True
            fall_speed = gravity  # Inicia a queda
            current_animation = 'Fall'

    # Verificação de colisão lateral durante o pulo
    if is_jumping or is_falling:
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx = -move_speed  # Movendo-se para a esquerda durante o pulo/queda
            new_x_pos = x_pos + dx
            x_pos, _, _, _ = check_full_collision(new_x_pos, y_pos, frame_width, frame_height, dx, dy, is_falling, is_jumping)
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx = move_speed  # Movendo-se para a direita durante o pulo/queda
            new_x_pos = x_pos + dx
            x_pos, _, _, _ = check_full_collision(new_x_pos, y_pos, frame_width, frame_height, dx, dy, is_falling, is_jumping)

    # Se nenhuma tecla de movimento for pressionada e não estiver pulando ou caindo, volta para Idle
    if not (keys[pygame.K_a] or keys[pygame.K_LEFT] or keys[pygame.K_d] or keys[pygame.K_RIGHT] or is_jumping or is_falling):
        current_animation = 'Idle'

    return x_pos, y_pos, current_animation, facing_right, is_jumping, is_falling, fall_speed, jump_key_pressed, double_jump_activated