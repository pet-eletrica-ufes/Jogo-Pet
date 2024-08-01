import pygame

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
