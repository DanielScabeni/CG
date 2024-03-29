import sys
import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# Variáveis de Velocidade 
vel_geral = 0.1
Vel_incremental = 1.1

# Variáveis da bola
tamanho_bola = 10
bola_x = largura // 2
bola_y = altura // 2
velocidade_bola_x = vel_geral
velocidade_bola_y = vel_geral

# Variáveis das barras
largura_barra = 10
altura_barra = 60
barra1_x = 50
barra1_y = altura // 2 - altura_barra // 2
barra2_x = largura - 50 - largura_barra
barra2_y = altura // 2 - altura_barra // 2
velocidade_barra = vel_geral

# Variáveis de controle para as barras
seguir_bola_barra1 = True
seguir_bola_barra2 = True

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimento das barras
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w]:
        barra1_y -= velocidade_barra
    if teclas[pygame.K_s]:
        barra1_y += velocidade_barra
    if teclas[pygame.K_UP]:
        barra2_y -= velocidade_barra
    if teclas[pygame.K_DOWN]:
        barra2_y += velocidade_barra

    # Verifica colisão com as bordas verticais
    if bola_y <= 0 or bola_y >= altura - tamanho_bola:
        velocidade_bola_y *= -1

    # Verifica colisão com as barras
    bola_rect = pygame.Rect(bola_x - tamanho_bola // 2, bola_y - tamanho_bola // 2, tamanho_bola, tamanho_bola)
    barra1_rect = pygame.Rect(barra1_x, barra1_y, largura_barra, altura_barra)
    barra2_rect = pygame.Rect(barra2_x, barra2_y, largura_barra, altura_barra)

    if bola_rect.colliderect(barra1_rect):
        velocidade_bola_x *= Vel_incremental
        velocidade_bola_y *= Vel_incremental
        velocidade_barra *= Vel_incremental

        velocidade_bola_x *= -1
        seguir_bola_barra1 = False

    elif bola_rect.colliderect(barra2_rect):
        velocidade_bola_x *= Vel_incremental
        velocidade_bola_y *= Vel_incremental
        velocidade_barra *= Vel_incremental

        velocidade_bola_x *= -1
        seguir_bola_barra2 = False

    # Movimento das barras automaticamente
    if bola_x <= largura / 2 and seguir_bola_barra1:
        if barra1_y <= bola_y:
            barra1_y += velocidade_barra
        else:
            barra1_y -= velocidade_barra
    
    if bola_x >= largura / 2 and seguir_bola_barra2:
        if barra2_y >= bola_y:
            barra2_y -= velocidade_barra
        else:
            barra2_y += velocidade_barra

    # Movimento da bola
    bola_x += velocidade_bola_x
    bola_y += velocidade_bola_y

    # Verifica colisão com as bordas horizontais
    if bola_x <= 0 or bola_x >= largura - tamanho_bola:
        bola_x = largura // 2   
        bola_y = altura // 2
        velocidade_bola_x = vel_geral
        velocidade_bola_y = vel_geral
        velocidade_barra = vel_geral
        velocidade_bola_x *= -1
    

    # Verifica se a bola passou do meio da tela
    if bola_x < largura / 2 and velocidade_bola_x < 0:
        seguir_bola_barra1 = True
        seguir_bola_barra2 = False
    elif bola_x > largura / 2 and velocidade_bola_x > 0:
        seguir_bola_barra1 = False
        seguir_bola_barra2 = True

    # Deixar a bola e as barras lentas quando uma das barras deixar a bola passar
    if bola_x < barra1_x - largura_barra or bola_x > largura - barra1_x + largura_barra:
        clock.tick(1)
        #velocidade_bola_x = vel_geral / 3
        #velocidade_bola_y = vel_geral / 3
        #velocidade_barra = vel_geral / 3

    # Preencher a tela com a cor preta
    tela.fill(PRETO)

    # Desenhar as barras
    pygame.draw.rect(tela, BRANCO, (barra1_x, barra1_y - altura_barra // 2, largura_barra, altura_barra))
    pygame.draw.rect(tela, BRANCO, (barra2_x, barra2_y - altura_barra // 2, largura_barra, altura_barra))

    # Desenhar a bola
    pygame.draw.circle(tela, BRANCO, (bola_x, bola_y), tamanho_bola // 2)

    # Atualizar a tela
    pygame.display.flip()
