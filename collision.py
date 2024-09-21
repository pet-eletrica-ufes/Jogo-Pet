# collision.py
from config import screen_width, screen_height, velo
from mapeamento import obter_plataformas, obter_objetos_acao

def check_collision_bordas(x, y, width, height, eixo):
    """
    Verifica se o personagem está colidindo com as bordas da tela e ajusta a posição.
    
    :param x: Coordenada X do personagem.
    :param y: Coordenada Y do personagem.
    :param width: Largura do personagem.
    :param height: Altura do personagem.
    :param eixo: Eixo de movimentação ("horizontal" ou "vertical").
    :return: Nova posição X ou Y ajustada para não ultrapassar as bordas.
    """
    if eixo == "horizontal":
        # Verifica se o personagem está saindo da tela no eixo X
        if x < 0:
            x = 0  # Limita a posição à borda esquerda
        elif x + width > screen_width:
            x = screen_width - width  # Limita a posição à borda direita

    elif eixo == "vertical":
        # Verifica se o personagem está saindo da tela no eixo Y
        if y < 0:
            y = 0  # Limita a posição à borda superior
        elif y + height > screen_height:
            y = screen_height - height  # Limita a posição à borda inferior

    return x, y


def check_collision_objetos(x, y, width, height, objetos, eixo):
    """
    Verifica se há colisão com objetos sólidos e impede o avanço do personagem no eixo em questão.
    
    :param x: Coordenada X atual do personagem.
    :param y: Coordenada Y atual do personagem.
    :param width: Largura do personagem.
    :param height: Altura do personagem.
    :param objetos: Lista de objetos sólidos para verificar colisão.
    :param eixo: Eixo de movimentação ("horizontal" ou "vertical").
    :return: Nova posição X ou Y ajustada em caso de colisão.
    """
    for objeto in objetos:
        if objeto.solido and objeto.colide(x, y, width, height):
            if eixo == "horizontal":
                # Verifica colisão horizontal
                if x < objeto.x + objeto.largura and x + width > objeto.x:
                    if x + width > objeto.x:  # Colisão pela direita
                        return objeto.x - width, y  # Impede o avanço no eixo X
                    elif x < objeto.x + objeto.largura:  # Colisão pela esquerda
                        return objeto.x + objeto.largura, y  # Impede o avanço no eixo X

            elif eixo == "vertical":
                # Verifica colisão vertical
                if y < objeto.y + objeto.altura and y + height > objeto.y:
                    if y + height > objeto.y:  # Colisão por baixo
                        return x, objeto.y - height  # Impede o avanço no eixo Y
                    elif y < objeto.y + objeto.altura:  # Colisão por cima
                        return x, objeto.y + objeto.altura  # Impede o avanço no eixo Y

    return x, y


def check_full_collision(x, y, width, height, eixo, is_falling, is_jumping):
    """
    Verifica colisão com as bordas da tela e com objetos sólidos, impedindo o avanço do personagem no eixo de colisão.
    
    :param x: Coordenada X do personagem.
    :param y: Coordenada Y do personagem.
    :param width: Largura do personagem.
    :param height: Altura do personagem.
    :param eixo: Eixo de movimentação ("horizontal" ou "vertical").
    :param is_falling: Se o personagem está caindo.
    :param is_jumping: Se o personagem está pulando.
    :return: Nova posição X e Y ajustada, e flags de estado (is_falling, is_jumping) atualizadas.
    """
    # Verifica colisão com as bordas da tela
    x, y = check_collision_bordas(x, y, width, height, eixo)

    # Verifica colisão com objetos sólidos (plataformas, blocos, etc.)
    plataformas = obter_plataformas()  # Pega as plataformas mapeadas
    objetos_acao = obter_objetos_acao()  # Pega os objetos com ação, se necessário

    # Verifica colisão com plataformas e objetos de ação (se forem sólidos)
    x, y = check_collision_objetos(x, y, width, height, plataformas + objetos_acao, eixo)

    # Verifica colisão com o chão (somente no eixo vertical)
    if eixo == "vertical":
        for plataforma in plataformas:
            if plataforma.solido and plataforma.colide(x, y + height, width, 1):
                y = plataforma.y - height  # Ajusta para ficar em cima da plataforma
                is_falling = False
                is_jumping = False

    return x, y, is_falling, is_jumping