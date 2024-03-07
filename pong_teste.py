import sys
import pygame

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pong")

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# Variáveis da bola
tamanho_bola = 20
bola_x = largura // 2
bola_y = altura // 2
velocidade_bola_x = 0.1
velocidade_bola_y = 0.1

# Variáveis das barras
largura_barra = 5
altura_barra = 150
barra1_x = 50
barra1_y = altura // 4 - altura_barra // 4
barra2_x = largura - 50 - largura_barra
barra2_y = altura // 2 - altura_barra // 2
velocidade_barra = 0.3

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimento das barras (barras)
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w]:
        barra1_y -= velocidade_barra
    if teclas[pygame.K_s]:
        barra1_y += velocidade_barra
    if teclas[pygame.K_UP]:
        barra2_y -= velocidade_barra
    if teclas[pygame.K_DOWN]:
        barra2_y += velocidade_barra

    # Movimento da bola
    bola_x += velocidade_bola_x
    bola_y += velocidade_bola_y

    # Verifica colisão com as bordas verticais
    if bola_y <= 0 or bola_y >= altura - tamanho_bola:
        velocidade_bola_y *= -1

    # Verifica colisão com as barras (barras)
    if (barra1_x <= bola_x <= barra1_x + largura_barra and 
            barra1_y <= bola_y <= barra1_y + altura_barra) or \
       (barra2_x <= bola_x <= barra2_x + largura_barra and 
            barra2_y <= bola_y <= barra2_y + altura_barra):
        velocidade_bola_x *= -1

    # Verifica colisão com as bordas horizontais
    if bola_x <= 0 or bola_x >= largura - tamanho_bola:
        # Se a bola atingir as extremidades laterais, reinicia a posição da bola
        bola_x = largura // 2   
        bola_y = altura // 2
        velocidade_bola_x *= -1

    # Preencher a tela com a cor preta
    tela.fill(PRETO)

    # Desenhar as barras (barras)
    pygame.draw.rect(tela, BRANCO, (barra1_x, barra1_y, largura_barra, altura_barra))
    pygame.draw.rect(tela, BRANCO, (barra2_x, barra2_y, largura_barra, altura_barra))

    # Desenhar a bola
    pygame.draw.circle(tela, BRANCO, (bola_x, bola_y), tamanho_bola // 2)

    # Atualizar a tela
    pygame.display.flip()
