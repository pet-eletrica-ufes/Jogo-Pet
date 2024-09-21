# objeto.py

class Objeto:
    def __init__(self, x, y, largura, altura, solido=True, acao=False):
        """
        Classe que representa um objeto no jogo.
        
        :param x: Coordenada X do objeto.
        :param y: Coordenada Y do objeto.
        :param largura: Largura do objeto.
        :param altura: Altura do objeto.
        :param solido: Define se o objeto é sólido (True) ou não (False).
        :param acao: Define se o objeto tem uma ação associada (True) ou não (False).
        """
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.solido = solido
        self.acao = acao

    def colide(self, x, y, largura, altura):
        """
        Verifica se há colisão entre o objeto e outro retângulo.
        
        :param x: Coordenada X do outro objeto.
        :param y: Coordenada Y do outro objeto.
        :param largura: Largura do outro objeto.
        :param altura: Altura do outro objeto.
        :return: True se houver colisão, False caso contrário.
        """
        return (self.x < x + largura and
                self.x + self.largura > x and
                self.y < y + altura and
                self.y + self.altura > y)