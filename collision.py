from config import screen_width, screen_height, velo
from mapeamento import obter_plataformas, obter_objetos_acao

def check_collision_bordas(x, y, width, height, dx, dy, is_falling, is_jumping):
    """
    Verifica se o personagem está colidindo com as bordas da tela e ajusta a posição.
    """
    if dx != 0:  # Movimento no eixo horizontal
        if x < 0:
            x = 0  # Limita a posição à borda esquerda
        elif x + width > screen_width:
            x = screen_width - width  # Limita a posição à borda direita

    if dy != 0:  # Movimento no eixo vertical
        if y < 0:
            y = 6  # Limita a posição à borda superior
            is_falling = False
            is_jumping = False
        elif y + height > screen_height:
            y = screen_height - height  # Limita a posição à borda inferior
            is_falling = False
            is_jumping = False  # Reseta o estado de pulo ao tocar o chão

    return x, y, is_falling, is_jumping


def check_collision_objetos(x, y, width, height, dx, dy, objetos):
    """
    Verifica se há colisão com objetos sólidos e impede o avanço do personagem no eixo em questão.
    """
    for objeto in objetos:
        if objeto.solido and objeto.colide(x, y, width, height):
            if dx > 0:  # Movendo-se para a direita
                if x + width > objeto.x:  # Colisão à direita
                    x = objeto.x - width  # Ajusta a posição para parar antes da colisão
            elif dx < 0:  # Movendo-se para a esquerda
                if x < objeto.x + objeto.largura:  # Colisão à esquerda
                    x = objeto.x + objeto.largura  # Ajusta a posição para parar antes da colisão

            if dy > 0:  # Movendo-se para baixo (caindo)
                if y + height > objeto.y:  # Colisão por baixo
                    y = objeto.y - height  # Ajusta a posição para parar antes da colisão
                    is_falling = False  # Reseta o estado de queda ao tocar a plataforma
                    is_jumping = False  # Reseta o estado de pulo ao tocar a plataforma
            elif dy < 0:  # Movendo-se para cima (pulando)
                if y < objeto.y + objeto.altura:  # Colisão por cima
                    y = objeto.y + objeto.altura  # Ajusta a posição para parar antes da colisão

    return x, y


def check_full_collision(x, y, width, height, dx, dy, is_falling, is_jumping):
    """
    Verifica colisão com as bordas da tela e com objetos sólidos, impedindo o avanço do personagem no eixo de colisão.
    """
    # Verifica colisão com as bordas da tela
    x, y, is_falling, is_jumping = check_collision_bordas(x, y, width, height, dx, dy, is_falling, is_jumping)

    # Verifica colisão com objetos sólidos (plataformas, blocos, etc.)
    plataformas = obter_plataformas()  # Pega as plataformas mapeadas
    objetos_acao = obter_objetos_acao()  # Pega os objetos com ação, se necessário

    # Verifica colisão com plataformas e objetos de ação (se forem sólidos)
    x, y = check_collision_objetos(x, y, width, height, dx, dy, plataformas + objetos_acao)

    # Verifica colisão com o chão (somente no eixo vertical)
    if dy > 0:  # Somente verifica colisão com o chão se estiver caindo
        for plataforma in plataformas:
            if plataforma.solido and plataforma.colide(x, y + height, width, 1):
                y = plataforma.y - height  # Ajusta para ficar em cima da plataforma
                is_falling = False
                is_jumping = False
    
    return x, y, is_falling, is_jumping