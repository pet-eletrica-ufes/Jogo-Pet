from config import screen_width, screen_height, velo
from mapeamento import obter_plataformas, obter_objetos_acao

def check_collision_bordas(x, y, width, height, dx, dy):
    """
    Verifica se o personagem está colidindo com as bordas da tela e ajusta a posição.

    :param x: Coordenada X do personagem.
    :param y: Coordenada Y do personagem.
    :param width: Largura do personagem.
    :param height: Altura do personagem.
    :param dx: Variação no eixo X (sentido do movimento no eixo X).
    :param dy: Variação no eixo Y (sentido do movimento no eixo Y).
    :return: Nova posição X ou Y ajustada para não ultrapassar as bordas.
    """
    if dx != 0:  # Movimento no eixo horizontal
        if x < 0:
            x = 0  # Limita a posição à borda esquerda
        elif x + width > screen_width:
            x = screen_width - width  # Limita a posição à borda direita

    if dy != 0:  # Movimento no eixo vertical
        if y < 0:
            y = 6  # Limita a posição à borda superior
        elif y + height > screen_height:
            y = screen_height - height  # Limita a posição à borda inferior

    return x, y


def check_collision_objetos(x, y, width, height, dx, dy, objetos):
    """
    Verifica se há colisão com objetos sólidos e impede o avanço do personagem no eixo em questão.

    :param x: Coordenada X atual do personagem.
    :param y: Coordenada Y atual do personagem.
    :param width: Largura do personagem.
    :param height: Altura do personagem.
    :param dx: Variação no eixo X (sentido do movimento no eixo X).
    :param dy: Variação no eixo Y (sentido do movimento no eixo Y).
    :param objetos: Lista de objetos sólidos para verificar colisão.
    :return: Nova posição X ou Y ajustada em caso de colisão.
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
            elif dy < 0:  # Movendo-se para cima (pulando)
                if y < objeto.y + objeto.altura:  # Colisão por cima
                    y = objeto.y + objeto.altura  # Ajusta a posição para parar antes da colisão

    return x, y


def check_full_collision(x, y, width, height, dx, dy, is_falling, is_jumping):
    """
    Verifica colisão com as bordas da tela e com objetos sólidos, impedindo o avanço do personagem no eixo de colisão.

    :param x: Coordenada X do personagem.
    :param y: Coordenada Y do personagem.
    :param width: Largura do personagem.
    :param height: Altura do personagem.
    :param dx: Variação no eixo X (sentido do movimento no eixo X).
    :param dy: Variação no eixo Y (sentido do movimento no eixo Y).
    :param is_falling: Se o personagem está caindo.
    :param is_jumping: Se o personagem está pulando.
    :return: Nova posição X e Y ajustada, e flags de estado (is_falling, is_jumping) atualizadas.
    """
    # Verifica colisão com as bordas da tela
    x, y = check_collision_bordas(x, y, width, height, dx, dy)

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