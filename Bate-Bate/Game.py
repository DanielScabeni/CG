import pygame # import das bibliotecas
import sys
from MecMovimento import MovendoTexto # importa a classe MecMovimento no arquivo MecMovimento


class Game: 
    def __init__(self):
        pygame.init() # inicializa o pygame
        self.largura = 800 
        self.altura = 600 # define as variaveis e valores de largura e altura
        self.tela = pygame.display.set_mode((self.largura, self.altura)) # Cria a superficie da tela com as dimensoes definidas
        pygame.display.set_caption("Bate-Bate") # Define o título da janela com
        self.clock = pygame.time.Clock() # Cria um objeto Clock para controlar a taxa de atualização da tela
        self.MovendoTexto = MovendoTexto("Movendo Texto", 50, self.largura, self.altura) # Cria um objeto MovendoTexto para controlar o texto que se move na tela

    def run(self): # loop principal do jogo
        rodando = True # variavel para controlar se o jogo não foi fechado
        while rodando: # mantém o jogo rodando enquanto não for fechado
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT: # verifica se o botão de fechar foi pressionado
                    rodando = False # altera a variavel para sair do loop

            self.MovendoTexto.move() # atualiza a posição do texto
            self.tela.fill((0, 0, 0)) # preenche a tela com a cor preta
            self.tela.blit(self.MovendoTexto.texto_surf, self.MovendoTexto.rect) # Desenha o texto movel na tela
            pygame.display.flip() # atualiza a tela
            self.s # controla a taxa de atualização da tela

        pygame.quit() # finaliza o pygame quando sai do loop
        sys.exit() # encerra o script
