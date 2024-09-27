import pygame
from pygame.locals import *
from sys import exit

# Classe para os pontos
class Ponto:
    def __init__(self, x, y, cor):
        self.pos = (x, y)
        self.cor = cor

    def desenhar(self, tela):
        pygame.draw.circle(tela, self.cor, self.pos, 10)

# Classe para o jogo
class Jogo:
    def __init__(self):
        pygame.init()

        # Configurações da tela
        self.largura = 640
        self.altura = 480
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption('Minigame')

        # Cores
        self.branco = (255, 255, 255)
        self.verde = (0, 255, 0)
        self.vermelho = (255, 0, 0)
        self.azul = (0, 0, 255)
        self.amarelo = (255, 255, 0)
        self.lilas = (200, 100, 255)
 
        self.iniciar_jogo()
    

          
          

    def iniciar_jogo(self):
        # Cria os pontos com margens adequadas
        margem = 20
        espaco_vertical = (self.altura - 2 * margem) // 5

        self.pontos_coluna_1 = [
            Ponto(150, margem + 0 * espaco_vertical, self.lilas),    # Lilás
            Ponto(150, margem + 1 * espaco_vertical, self.amarelo),   # Amarelo
            Ponto(150, margem + 2 * espaco_vertical, self.vermelho),  # Vermelho
            Ponto(150, margem + 3 * espaco_vertical, self.azul),      # Azul
            Ponto(150, margem + 4 * espaco_vertical, self.verde)      # Verde
        ]
        
        self.pontos_coluna_2 = [
            Ponto(490, margem + 0 * espaco_vertical, self.lilas),    # Lilás
            Ponto(490, margem + 1 * espaco_vertical, self.amarelo),   # Amarelo
            Ponto(490, margem + 2 * espaco_vertical, self.vermelho),  # Vermelho
            Ponto(490, margem + 3 * espaco_vertical, self.azul),      # Azul
            Ponto(490, margem + 4 * espaco_vertical, self.verde)      # Verde
        ]

        self.linhas = []  # Para armazenar as linhas desenhadas
        self.pontos_conectados = []  # Lista para armazenar pontos já conectados
        self.conexoes_corretas = 0  # Contador de conexões corretas (mesma cor)
        self.ganhou = False  # Flag para indicar se ganhou

        self.ponto_atual = None  # Ponto da primeira coluna que foi clicado

        self.rodar()  # Inicia o loop do jogo

    def rodar(self):
        executando = True
        while executando:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    self.verifica_clique(mouse_pos)
                    
                #if event.type == MOUSEBUTTONUP:
                #    self.ponto_atual = None  # Para a manipulação ao soltar o botão do mouse

                #if event.type == MOUSEMOTION:
                #    if self.ponto_atual is not None:
                #        self.mover_ponto(pygame.mouse.get_pos())

            self.desenhar()

    #def mover_ponto():


    def verifica_clique(self, mouse_pos):
        # Verifica se clicou em um ponto da primeira coluna
        for ponto in self.pontos_coluna_1:
            if pygame.mouse.get_pressed()[0] and pygame.math.Vector2(ponto.pos).distance_to(mouse_pos) < 10:
                if ponto not in self.pontos_conectados:  # Verifica se o ponto já foi conectado
                    self.ponto_atual = ponto
                    return  # Sai para não selecionar mais de um ponto

        # Verifica se clicou em um ponto da segunda coluna
        for ponto in self.pontos_coluna_2:
            if pygame.mouse.get_pressed()[0] and pygame.math.Vector2(ponto.pos).distance_to(mouse_pos) < 10:
                if self.ponto_atual and ponto not in self.pontos_conectados:
                    if self.ponto_atual.cor == ponto.cor:  # Verifica se as cores são correspondentes
                        self.linhas.append((self.ponto_atual.pos, ponto.pos, self.ponto_atual.cor))
                        self.pontos_conectados.append(self.ponto_atual)  # Marca os pontos como conectados
                        self.pontos_conectados.append(ponto)
                        self.conexoes_corretas += 1  # Incrementa as conexões corretas
                        if self.conexoes_corretas == 5:  # Verifica se todas as 5 conexões foram feitas corretamente
                            self.ganhou = True  # Marca que já ganhou
                    self.ponto_atual = None
                    break
             


    def desenhar(self):
        # Preenche o fundo
        self.tela.fill(self.branco)

        # Desenha todos os pontos da primeira coluna
        for ponto in self.pontos_coluna_1:
            ponto.desenhar(self.tela)

        # Desenha todos os pontos da segunda coluna
        for ponto in self.pontos_coluna_2:
            ponto.desenhar(self.tela)

        # Desenha as linhas
        for linha in self.linhas:
            pygame.draw.line(self.tela, linha[2], linha[0], linha[1], 5)  # Linha com a cor correspondente

        # Desenha a linha em andamento, se houver
        if self.ponto_atual:
            mouse_pos = pygame.mouse.get_pos()
            pygame.draw.line(self.tela, self.ponto_atual.cor, self.ponto_atual.pos, mouse_pos, 5)

        # Verifica a pontuação e exibe a mensagem de vitória
        if self.ganhou:
            self.exibir_vitoria()

        # Atualiza a tela
        pygame.display.update()

    def exibir_vitoria(self):
        # Exibe a tela de vitória
        self.tela.fill(self.branco)  # Limpa a tela
        font = pygame.font.Font(None, 74)
        texto = font.render("Win!", True, (0, 0, 0))
        self.tela.blit(texto, (self.largura // 2 - 100, self.altura // 2 - 50))
        
        # Adiciona opção de reiniciar o jogo
        font_restart = pygame.font.Font(None, 36)
       # texto_restart = font_restart.render("Clique para reiniciar", True, (0, 0, 0))
        #self.tela.blit(texto_restart, (self.largura // 2 - 100, self.altura // 2 + 20))

        pygame.display.update()

        # Aguarda o clique do mouse para reiniciar
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    waiting = False  # Sai do loop e reinicia o jogo
                    pygame.quit()
                    exit()

# Inicializa e roda o jogo
if __name__ == '__main__':
    jogo = Jogo()
