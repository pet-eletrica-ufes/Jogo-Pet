import pygame
from collision import check_collision, check_full_collision

def handle_movement(x_pos, y_pos, frame_width, frame_height, keys, current_animation, current_frame,
                    facing_right, is_jumping, is_falling, jump_speed, fall_speed, gravity, move_speed,
                    block_size, level_layout, frame_duration, last_update_time, current_character, sprites,
                    jump_key_pressed, double_jump_activated):

    # Movimentação para a esquerda
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        new_x_pos = x_pos - move_speed
        if not check_full_collision(new_x_pos, y_pos, frame_width, frame_height, None, block_size):
            x_pos = new_x_pos
        else:
            # Ajustar a posição para fora do bloco
            while check_full_collision(x_pos - 1, y_pos, frame_width, frame_height, None, block_size):
                x_pos += 1
        if not is_jumping and not is_falling:
            current_animation = 'Run'
        facing_right = False

    # Movimentação para a direita
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        new_x_pos = x_pos + move_speed
        if not check_full_collision(new_x_pos, y_pos, frame_width, frame_height, None, block_size):
            x_pos = new_x_pos
        else:
            # Ajustar a posição para fora do bloco
            while check_full_collision(x_pos + 1, y_pos, frame_width, frame_height, None, block_size):
                x_pos -= 1
        if not is_jumping and not is_falling:
            current_animation = 'Run'
        facing_right = True

    # Pulo
    if (keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE]):
        if not is_jumping and not is_falling and not jump_key_pressed:
            is_jumping = True
            fall_speed = jump_speed
            current_animation = 'Jump'
            double_jump_activated = False  # Reset double jump activation
            jump_key_pressed = True  # Marca a tecla de pulo como pressionada
        elif is_jumping and not double_jump_activated and not jump_key_pressed:
            is_jumping = True
            fall_speed = jump_speed
            current_animation = 'Double Jump'
            double_jump_activated = True  # Activate double jump
            jump_key_pressed = True  # Marca a tecla de pulo como pressionada

    # Se a tecla de pulo foi liberada, permitir novo pulo duplo
    if not (keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE]):
        jump_key_pressed = False

    # Aplicação da gravidade se o personagem estiver no ar
    if not is_jumping and not is_falling:
        is_falling = True
        fall_speed = 0

    if is_falling:
        new_y_pos = y_pos + fall_speed
        if not check_full_collision(x_pos, new_y_pos, frame_width, frame_height, None, block_size):
            y_pos = new_y_pos
            fall_speed += gravity
        else:
            # Ajustar a posição para fora do bloco
            while check_full_collision(x_pos, y_pos + 1, frame_width, frame_height, None, block_size):
                y_pos -= 1
            fall_speed = 0
            is_falling = False
            is_jumping = False
            current_animation = 'Idle'
            double_jump_activated = False  # Reset double jump activation

    # Verificação de colisão ao pular
    if is_jumping:
        new_y_pos = y_pos + fall_speed
        if not check_full_collision(x_pos, new_y_pos, frame_width, frame_height, None, block_size):
            y_pos = new_y_pos
            fall_speed += gravity
        else:
            # Bateu em um bloco enquanto subia
            is_jumping = False
            is_falling = True
            fall_speed = gravity  # Inicia a queda
            current_animation = 'Fall'

    # Verificação de colisão lateral durante o pulo
    if is_jumping or is_falling:
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            new_x_pos = x_pos - move_speed
            if check_full_collision(new_x_pos, y_pos, frame_width, frame_height, None, block_size):
                x_pos += move_speed  # Reverte a movimentação se houver colisão
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            new_x_pos = x_pos + move_speed
            if check_full_collision(new_x_pos, y_pos, frame_width, frame_height, None, block_size):
                x_pos -= move_speed  # Reverte a movimentação se houver colisão

    # Se nenhuma tecla de movimento for pressionada e não estiver pulando ou caindo, volta para Idle
    if not (keys[pygame.K_a] or keys[pygame.K_LEFT] or keys[pygame.K_d] or keys[pygame.K_RIGHT] or is_jumping or is_falling):
        current_animation = 'Idle'

    return x_pos, y_pos, current_animation, facing_right, is_jumping, is_falling, fall_speed, jump_key_pressed, double_jump_activated