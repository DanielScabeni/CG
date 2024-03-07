import sys
import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configuração da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pygame")

# Função para gerar uma cor aleatória
def cor_aleatoria():
    # Gera valores aleatórios para os componentes de cor (RGB)
    vermelho = random.randint(0, 255)
    verde = random.randint(0, 255)
    azul = random.randint(0, 255)
    
    # Retorna a cor no formato (R, G, B)
    return (vermelho, verde, azul)

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
COR = cor_aleatoria()

# Fontes
tamanho_fonte = 50 
fonte = pygame.font.SysFont(None, tamanho_fonte)

texto = fonte.render("AAaaaaaaa", True, COR)
text_react = texto.get_rect(center=(largura/2, altura/2))
#text_react = texto.get_rect(center=(94,0))

# Variáveis da bola
tamanho_bola = 40
bola_x = largura // 2
bola_y = altura // 2
vbola = 0.5
velocidade_bola_x = vbola
velocidade_bola_y = vbola

# loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # VERTICAL - Y
    if bola_y <= 0 + tamanho_bola /2 or bola_y >= altura - tamanho_bola /2:
        velocidade_bola_y *= -1
        COR = cor_aleatoria()

    # HORIZONTAL - X
    if bola_x <= 0 + tamanho_bola /2 or bola_x >= largura - tamanho_bola /2:
        velocidade_bola_x *= -1
        COR = cor_aleatoria()

    bola_x += velocidade_bola_x
    bola_y += velocidade_bola_y
    
    tela.fill(PRETO)
    #tela.blit(texto, text_react)
    pygame.draw.circle(tela, COR, (bola_x, bola_y), tamanho_bola // 2)
    pygame.display.flip()