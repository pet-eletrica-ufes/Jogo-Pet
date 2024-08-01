import pygame
import sys
from sprites2 import sprites, characters
from text import load_text_image, draw_text

# Função para exibir o menu de seleção de personagens
def character_selection_menu(screen, screen_width, screen_height):
    selected_character = None
    current_frame = {char: 0 for char in characters}
    frame_duration = 150  # 150ms por frame
    last_update_time = pygame.time.get_ticks()
    char_map = load_text_image()
    
    while selected_character is None:
        screen.fill((0, 0, 0))  # Limpa a tela
        
        # Obtém o tempo atual
        current_time = pygame.time.get_ticks()

        # Atualiza o frame se o tempo por frame tiver passado
        if current_time - last_update_time > frame_duration:
            for char in characters:
                if len(sprites[char]['Idle']) > 0:
                    current_frame[char] = (current_frame[char] + 1) % len(sprites[char]['Idle'])
            last_update_time = current_time

        # Desenha as sprites "Idle" de cada personagem
        for index, char in enumerate(characters):
            if len(sprites[char]['Idle']) > 0:
                frame_image = sprites[char]['Idle'][current_frame[char]]
                x_pos = (index + 1) * (screen_width // (len(characters) + 1)) - frame_image.get_width() // 2
                y_pos = screen_height // 2 - frame_image.get_height() // 2
                screen.blit(frame_image, (x_pos, y_pos))
                
                # Desenha o nome do personagem abaixo da sprite
                text_x = x_pos + (frame_image.get_width() // 2) - (len(char) * 4)
                text_y = y_pos + frame_image.get_height() + 10
                draw_text(screen, char.upper(), text_x, text_y, char_map)
                
                # Verifica se o mouse está sobre a sprite
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if x_pos < mouse_x < x_pos + frame_image.get_width() and y_pos < mouse_y < y_pos + frame_image.get_height():
                    if pygame.mouse.get_pressed()[0]:  # Verifica se o botão esquerdo do mouse foi clicado
                        selected_character = char
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    return selected_character