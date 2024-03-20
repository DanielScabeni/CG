import pygame 
import random

class MovendoTexto:
    def __init__(self, texto, fonte_tamanho, largura, altura):
        self.fonte = pygame.font.SysFont(None, fonte_tamanho) #  Objeto Font do Pygame usado para renderizar o texto.
        self.texto = texto # String que contém o texto que será renderizado.
        self.largura = largura # Largura da tela do jogo.
        self.altura = altura # Altura da tela do jogo.
        self.texto_surf = self.fonte.render(texto, True, (255, 255, 255)) # Superfície do Pygame que contém o texto renderizado.
        self.rect = self.texto_surf.get_rect(center = (largura/2, altura/2)) # Retângulo que define a posição e o tamanho do texto na tela.
        
        self.velocidade_x = self.gerar_numero_nao_zero() # Velocidade horizontal do movimento do texto.
        self.velocidade_y = self.gerar_numero_nao_zero() # Velocidade vertical do movimento do texto.

    def gerar_numero_nao_zero(self): # Função que gera um número aleatório que não seja zero.
        numero = 0
        while numero == 0: # Enquanto o numero não for zera, o loop se repete.
            numero = random.randint(-1, 1) # Gera um numero aleatorio INTEIRO entre -1 e 1.
        return numero

    def move(self): # Atualiza a posição do texto na tela.
        self.rect.x += self.velocidade_x
        self.rect.y += self.velocidade_y #Move o retângulo rect de acordo com as velocidades X e Y.

        if self.rect.left <= 0: # Verifica se o canto esquerdo do texto está na posição 0 ou à esquerda dela (fora da tela).
            self.velocidade_x = random.randint(0, 1) # Define aleatoriamente uma velocidade horizontal do texto, garantindo que não seja menor q 0 horizontalmente (à esquerda dela)
            self.velocidade_y = random.randint(-1, 1) # Define aleatoriamente uma velocidade vertical 
            self.change_color() # Altera a cor usando a função de aleatorizar a mesmam

        if self.rect.right >= self.largura:
            self.velocidade_x = random.randint(-1, 0) # # Define aleatoriamente uma velocidade horizontal e impede que va para fora da tela
            self.velocidade_y = random.randint(-1, 1) # Define aleatoriamente uma velocidade vertical 
            self.change_color() # Altera a cor usando a função de aleatorizar a mesmam

        if self.rect.top <= 0:
            self.velocidade_x = random.randint(-1, 1) # Define aleatoriamente uma velocidade horizontal
            self.velocidade_y = random.randint(0, 1) # Define aleatoriamente uma velocidade vertical e impede que va para fora da tela
            self.change_color() # Altera a cor usando a função de aleatorizar a mesmam

        if self.rect.bottom >= self.altura:
            self.velocidade_x = random.randint(-1, 1) # Define aleatoriamente uma velocidade horizontal
            self.velocidade_y = random.randint(-1, 0) # Define aleatoriamente uma velocidade vertical e impede que va para fora da tela
            self.change_color() # Altera a cor usando a função de aleatorizar a mesmam

    def change_color(self): # Função que altera a cor do texto.
        cor_texto = (
            random.randint(0, 255), # Gera uma cor aleatorio para as posições de (Red, Green, Blue)
            random.randint(0, 255),
            random.randint(0, 255),
        )
        self.texto_surf = self.fonte.render(self.texto, True, cor_texto) # Atualiza a superficie do texto com a cor
