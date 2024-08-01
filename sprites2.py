import pygame
import math

# Lista de personagens
characters = ['Mask Dude', 'Ninja Frog', 'Pink Man', 'Virtual Guy']

# Lista de animações para cada personagem
animations = ['Run', 'Idle', 'Jump', 'Fall', 'Double Jump', 'Wall Jump']

# Dicionário para armazenar as sprites de cada animação
sprites = {char: {anim: [] for anim in animations} for char in characters}

# Lista para armazenar os blocos de terreno
terrain_blocks = []

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

def load_terrain_blocks():
    sprite_sheet_path = 'Sprites/Pixel Adventure 1/Free/Terrain/Terrain (16x16).png'
    block_size = 16
    sheet_width = 352
    sheet_height = 176

    try:
        sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
    except pygame.error as e:
        print(f"Erro ao carregar a sprite sheet: {sprite_sheet_path}")
        print(e)
        return

    for y in range(0, sheet_height, block_size):
        for x in range(0, sheet_width, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            block_image = sprite_sheet.subsurface(rect)
            terrain_blocks.append(block_image)

    # Verificação de depuração
    print(f"Carregado {len(terrain_blocks)} blocos de terreno")

# Carrega todas as sprites
def initialize_sprites():
    load_sprites()
    load_terrain_blocks()