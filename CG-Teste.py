import sys
import pygame

pygame.init()

#Configuração da tela
largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pygame")

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

tamanho_fonte = 50 
fonte = pygame.font.SysFont(None, tamanho_fonte)

texto = fonte.render("Scabencini", True, BRANCO)
#text_react = texto.get_rect(center=(largura/2, altura/2))
text_react = texto.get_rect(center=(94,0))

def tamanho_fonte(largura, alt):
    tamanho_fonte = texto.get_rect(center=(largura, alt))
    return tamanho_fonte

#loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill(PRETO)
    tela.blit(texto, tamanho_fonte(94,15))
    tela.blit(texto, tamanho_fonte(400,15))
    tela.blit(texto, tamanho_fonte(706,15))
    
    tela.blit(texto, tamanho_fonte(94,300))
    tela.blit(texto, tamanho_fonte(400,300))
    tela.blit(texto, tamanho_fonte(706,300))

    tela.blit(texto, tamanho_fonte(94,585))
    tela.blit(texto, tamanho_fonte(400,585))
    tela.blit(texto, tamanho_fonte(706,585))
    pygame.display.flip()




