def check_collision(x, y, level_layout, block_size):
    col = x // block_size
    row = y // block_size
    if row < len(level_layout) and col < len(level_layout[0]):
        return level_layout[row][col] == 1
    return False

def check_full_collision(x, y, width, height, level_layout, block_size):
    # Verificar colisão nos quatro cantos do personagem
    return (check_collision(x, y, level_layout, block_size) or
            check_collision(x + width - 1, y, level_layout, block_size) or
            check_collision(x, y + height - 1, level_layout, block_size) or
            check_collision(x + width - 1, y + height - 1, level_layout, block_size) or
            check_collision(x + width // 2, y, level_layout, block_size) or
            check_collision(x + width // 2, y + height - 1, level_layout, block_size))