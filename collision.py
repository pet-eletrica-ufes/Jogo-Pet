# Importa screen_width e screen_height diretamente do game.py
from config import screen_width, screen_height
def check_collision(x, y, level_layout, block_size):
    """
    Verifica se há colisão com as bordas da tela ou com blocos do layout, se fornecido.
    """
    # Verificar se está dentro dos limites da tela
    if x < 0 or x >= screen_width or y < 0 or y >= screen_height:
        return True  # Colisão com as bordas da tela

    # Se o level_layout for None, não haverá colisão com blocos
    if level_layout is None:
        return False
    
    # Se o level_layout for fornecido, verificar colisão com blocos
    col = x // block_size
    row = y // block_size
    if row < len(level_layout) and col < len(level_layout[0]):
        return level_layout[row][col] == 1  # Colisão com bloco
    return False

def check_full_collision(x, y, width, height, level_layout, block_size):
    """
    Verifica colisão nos quatro cantos e no centro do personagem com as bordas da tela e blocos do layout.
    """
    # Verificar colisão nos quatro cantos e no centro do personagem
    return (check_collision(x, y, level_layout, block_size) or
            check_collision(x + width - 1, y, level_layout, block_size) or
            check_collision(x, y + height - 1, level_layout, block_size) or
            check_collision(x + width - 1, y + height - 1, level_layout, block_size) or
            check_collision(x + width // 2, y, level_layout, block_size) or
            check_collision(x + width // 2, y + height - 1, level_layout, block_size))