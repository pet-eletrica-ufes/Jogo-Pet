# mapeamento.py

# Função que retorna as coordenadas das plataformas (ou outras áreas de colisão)
def obter_plataformas():
    # Cada plataforma é representada por um dicionário com as coordenadas (x, y) e dimensões (largura, altura)
    plataformas = [
        {"x": 100, "y": 200, "largura": 300, "altura": 20},  # Plataforma 1
        {"x": 150, "y": 400, "largura": 250, "altura": 20},  # Plataforma 2
        {"x": 400, "y": 350, "largura": 200, "altura": 20},  # Plataforma 3
    ]
    return plataformas

# Você pode adicionar outras funções para mapear outros tipos de objetos, como paredes, inimigos, etc.
def obter_paredes():
    paredes = [
        {"x": 50, "y": 100, "largura": 10, "altura": 500},  # Parede 1
        {"x": 600, "y": 50, "largura": 10, "altura": 500},  # Parede 2
    ]
    return paredes