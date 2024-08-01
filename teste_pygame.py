import pygame
import sys
import math

# Inicializa o Pygame
pygame.init()

# Define as dimensões da janela
screen_width = 384
screen_height = 384
screen = pygame.display.set_mode((screen_width, screen_height))

# Lista de personagens
characters = ['Mask Dude', 'Ninja Frog', 'Pink Man', 'Virtual Guy']

# Lista de animações para cada personagem
animations = ['Run', 'Idle', 'Jump', 'Fall', 'Double Jump', 'Wall Jump']

# Dicionário para armazenar as sprites de cada animação
sprites = {char: {anim: [] for anim in animations} for char in characters}

# Função para carregar as sprites
def load_sprites():
    for char in characters:
        for anim in animations:
            if anim == 'Idle':
                sprite_sheet_path = f'Sprites/Pixel Adventure 1/Free/Main Characters/{char}/Idle (32x32).png'
                num_frames = 11
                width = 352
                height = 32
            elif anim == 'Run':
                sprite_sheet_path = f'Sprites/Pixel Adventure 1/Free/Main Characters/{char}/Run (32x32).png'
                num_frames = 12
                width = 384
                height = 32
            elif anim in ['Jump', 'Fall']:
                sprite_sheet_path = f'Sprites/Pixel Adventure 1/Free/Main Characters/{char}/{anim} (32x32).png'
                num_frames = 1
                width = 32
                height = 32
            elif anim == 'Double Jump':
                sprite_sheet_path = f'Sprites/Pixel Adventure 1/Free/Main Characters/{char}/Double Jump (32x32).png'
                num_frames = 6
                width = 192
                height = 32
            elif anim == 'Wall Jump':
                sprite_sheet_path = f'Sprites/Pixel Adventure 1/Free/Main Characters/{char}/Wall Jump (32x32).png'
                num_frames = 5
                width = 160
                height = 32
            
            try:
                sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
            except pygame.error as e:
                print(f"Erro ao carregar a sprite sheet: {sprite_sheet_path}")
                print(e)
                continue

            frame_width = math.floor(width / num_frames)
            frame_height = height

            for i in range(num_frames):
                x = i * frame_width
                rect = pygame.Rect(x, 0, frame_width, frame_height)
                frame_image = sprite_sheet.subsurface(rect)
                sprites[char][anim].append(frame_image)

            # Verificação de depuração
            print(f"Carregado {num_frames} frames para {char} - {anim}")

# Carrega todas as sprites
load_sprites()

# Função para carregar a imagem de texto e mapear os caracteres
def load_text_image():
    text_image_path = 'Sprites/Pixel Adventure 1/Free/Menu/Text/Text (White) (8x10).png'
    text_image = pygame.image.load(text_image_path).convert_alpha()
    char_width, char_height = 8, 10
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,:?!()[]+-'
    char_map = {}
    
    for i, char in enumerate(characters):
        x = (i % 10) * char_width
        y = (i // 10) * char_height
        rect = pygame.Rect(x, y, char_width, char_height)
        
        # Verificação para garantir que o retângulo está dentro dos limites da imagem
        if rect.right <= text_image.get_width() and rect.bottom <= text_image.get_height():
            char_map[char] = text_image.subsurface(rect)
        else:
            print(f"Erro: Retângulo {rect} fora dos limites da imagem de texto")

    return char_map

# Função para desenhar texto na tela
def draw_text(screen, text, x, y, char_map):
    for char in text:
        if char in char_map:
            screen.blit(char_map[char], (x, y))
            x += char_map[char].get_width()

# Carrega a imagem de texto e o mapa de caracteres
char_map = load_text_image()

# Função para exibir o menu de seleção de personagens
def character_selection_menu():
    selected_character = None
    current_frame = {char: 0 for char in characters}
    frame_duration = 150  # 150ms por frame
    last_update_time = pygame.time.get_ticks()
    
    while selected_character is None:
        screen.fill((0, 0, 0))  # Limpa a tela
        
        # Obtém o tempo atual
        current_time = pygame.time.get_ticks()

        # Atualiza o frame se o tempo por frame tiver passado
        if current_time - last_update_time > frame_duration:
            for char in characters:
                current_frame[char] = (current_frame[char] + 1) % len(sprites[char]['Idle'])
            last_update_time = current_time

        # Desenha as sprites "Idle" de cada personagem
        for index, char in enumerate(characters):
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

# Chama a função de menu de seleção de personagens
current_character = character_selection_menu()

# Define a animação e o frame atuais
current_animation = 'Idle'
previous_animation = current_animation
current_frame = 0
frame_duration = 50  # 50ms por frame

# Posição inicial do personagem
x_pos = screen_width // 2
y_pos = screen_height // 2

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

    # Movimentação para a esquerda
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        x_pos -= move_speed
        if not is_jumping and not is_falling:
            current_animation = 'Run'
        facing_right = False

    # Movimentação para a direita
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        x_pos += move_speed
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
        elif is_falling and not double_jump_activated and not jump_key_pressed:
            is_jumping = False
            is_falling = True
            fall_speed = jump_speed
            current_animation = 'Double Jump'
            double_jump_activated = True  # Activate double jump
            jump_key_pressed = True  # Marca a tecla de pulo como pressionada

    # Aplicação da gravidade
    if is_jumping or is_falling:
        y_pos += fall_speed
        fall_speed += gravity

        if fall_speed > 0 and current_animation == 'Jump':
            is_jumping = False
            is_falling = True
            current_animation = 'Fall'

        # Verifica se o personagem atingiu o chão
        if y_pos >= ground_level:
            y_pos = ground_level
            is_falling = False
            current_animation = 'Idle'
            can_double_jump = True

    # Se nenhuma tecla de movimento for pressionada e não estiver pulando ou caindo, volta para Idle
    if not (keys[pygame.K_a] or keys[pygame.K_LEFT] or keys[pygame.K_d] or keys[pygame.K_RIGHT] or is_jumping or is_falling):
        current_animation = 'Idle'

    # Limite de movimentação para não ultrapassar as bordas da janela
    if current_frame >= len(sprites[current_character][current_animation]):
        current_frame = 0

    frame_width = sprites[current_character][current_animation][current_frame].get_width()
    frame_height = sprites[current_character][current_animation][current_frame].get_height()

    if x_pos < 5:
        x_pos = 5
    elif x_pos > screen_width - frame_width - 5:
        x_pos = screen_width - frame_width - 5

    if y_pos < 5:
        y_pos = 5
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
    print(f"Animação atual: {current_animation}, Frame atual: {current_frame}")

    # Obtém a imagem do frame atual
    if current_frame >= len(sprites[current_character][current_animation]):
        current_frame = 0

    frame_image = sprites[current_character][current_animation][current_frame]

    # Espelha a imagem se estiver se movendo para a esquerda
    if not facing_right:
        frame_image = pygame.transform.flip(frame_image, True, False)

    # Desenha a imagem na tela
    screen.fill((0, 0, 0))  # Limpa a tela
    screen.blit(frame_image, (x_pos, y_pos))

    # Atualiza a tela
    pygame.display.flip()

    # Controla a taxa de atualização
    clock.tick(60)

# Sai do Pygame
pygame.quit()
sys.exit()