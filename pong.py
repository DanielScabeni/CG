import pygame
import sys
import random

pygame.init()

# Definição de cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
cor_bola = BRANCO

largura = 800
altura = 600

screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pong")

# Definição da Raquete
raquete_largura = 10
raquete_altura = 60
tamanho_bola = 10

# Velocidade da raquete
raquete_player_1_dy = 5
raquete_pc_dy = 5

# Velocidade geral
velocidade_geral = 3

# Velocidade da bola
velocidade_bola_x = velocidade_geral
velocidade_bola_y = velocidade_geral

# Definir Vencedor
vencedor = ""

# Definir controle
controle = False
rodando = True

# Configuração da fonte
font_file = "font/PressStart2P-Regular.ttf"
font = pygame.font.Font(font_file, 36)

clock = pygame.time.Clock()

# Opacidade inicial
opacidade_bola = 255
start_ticks = pygame.time.get_ticks()  # Tempo inicial

def menu_principal():
    global rodando, controle
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    controle = True
                    return
        # Renderiza o texto do menu
        screen.fill(PRETO)
        texto_menu = font.render("Pong", True, BRANCO)
        text_menu_rect = texto_menu.get_rect(center=(largura // 2, altura // 2))
        screen.blit(texto_menu, text_menu_rect)

        tempo = pygame.time.get_ticks()
        # Pressione Space para jogar
        if tempo % 2000 < 1000:
            texto_iniciar = font.render("Pressione Espaço", True, BRANCO)
            texto_iniciar_rect = texto_iniciar.get_rect(center=(largura // 2, 450))
            screen.blit(texto_iniciar, texto_iniciar_rect)

        clock.tick(1)
        pygame.display.flip()


def posicao_inicial():
    global pc_x, pc_y, player_1_x, player_1_y, bola_x, bola_y, score_pc, score_player_1, velocidade_bola_x, velocidade_bola_y, cor_bola, opacidade_bola

    # Posição da Raquete do pc
    pc_x = 10
    pc_y = altura // 2 - raquete_altura // 2

    # Posição da Raquete do player
    player_1_x = largura - 20
    player_1_y = altura // 2 - raquete_altura // 2

    # Posição da bola
    bola_x = largura // 2 - tamanho_bola // 2
    bola_y = altura // 2 - tamanho_bola // 2

    # Define o Score
    score_player_1 = 0
    score_pc = 0

    # Define a cor inicial e opacidade da bola
    cor_bola = BRANCO
    opacidade_bola = 255

    # Define a velocidade inicial da bola
    alterar_direcao_bola('')


def fim_jogo():
    global rodando, vencedor, controle
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    controle = True
                    posicao_inicial()
                    return
        # Renderiza o texto do menu
        screen.fill(PRETO)
        texto_fim = font.render(f"Vencedor: {vencedor}", True, BRANCO)
        text_fim_rect = texto_fim.get_rect(center=(largura // 2, altura // 2))
        screen.blit(texto_fim, text_fim_rect)

        pygame.display.flip()


def alterar_direcao_bola(eixo):
    global velocidade_bola_x, velocidade_bola_y, cor_bola

    # Mudança de direção e cor da bola
    if eixo == 'x':
        velocidade_bola_x = velocidade_bola_x * -1
        velocidade_bola_y = velocidade_bola_y * random.choice([1, -1])
    elif eixo == 'y':
        velocidade_bola_x = velocidade_bola_x * random.choice([1, -1])
        velocidade_bola_y = velocidade_bola_y * -1
    else:
        velocidade_bola_x = velocidade_bola_x * random.choice([1, -1])
        velocidade_bola_y = velocidade_bola_y * random.choice([1, -1])

    # Mudar a cor da bola aleatoriamente
    cor_bola = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


menu_principal()
posicao_inicial()

while rodando:
    if not controle:
        fim_jogo()
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

        screen.fill(PRETO)

        # Movendo a bola
        bola_x += velocidade_bola_x
        bola_y += velocidade_bola_y

        # Incremento na velocidade a cada 10 segundos
        segundos = (pygame.time.get_ticks() - start_ticks) / 1000
        if segundos > 10:
            velocidade_geral += 0.1
            velocidade_bola_x += 0.1 if velocidade_bola_x > 0 else -0.1
            velocidade_bola_y += 0.1 if velocidade_bola_y > 0 else -0.1
            start_ticks = pygame.time.get_ticks()  

        # Diminuição da opacidade da bola
        opacidade_bola = max(0, opacidade_bola - 0.1)
        bola_cor_transparente = (cor_bola[0], cor_bola[1], cor_bola[2], int(opacidade_bola))

        # Retângulos de Colisão
        bola_rect = pygame.Rect(bola_x, bola_y, tamanho_bola, tamanho_bola)
        raquete_pc_rect = pygame.Rect(pc_x, pc_y, raquete_largura, raquete_altura)
        raquete_player_1_rect = pygame.Rect(
            player_1_x, player_1_y, raquete_largura, raquete_altura
        )

        # Colisão da bola com a raquete do pc e a raquete do player
        if bola_rect.colliderect(raquete_pc_rect) or bola_rect.colliderect(
            raquete_player_1_rect
        ):
            alterar_direcao_bola('x')

        # Colisão da bola com as bordas da tela
        if bola_y <= 0 or bola_y >= altura - tamanho_bola:
            alterar_direcao_bola('y')

        # Posicionar a bola no inicio do jogo
        if bola_x <= 0:
            bola_x = largura // 2 - tamanho_bola // 2
            bola_y = altura // 2 - tamanho_bola // 2
            alterar_direcao_bola('')
            score_player_1 += 1
            print(f"Score Player_1: {score_player_1}")
            if score_player_1 == 5:
                print("Player_1 ganhou!")
                vencedor = "Player 1"
                fim_jogo()

        if bola_x >= largura - tamanho_bola:
            bola_x = largura // 2 - tamanho_bola // 2
            bola_y = altura // 2 - tamanho_bola // 2
            alterar_direcao_bola('')
            score_pc += 1
            print(f"Score PC: {score_pc}")
            if score_pc == 5:
                print("PC ganhou!")
                vencedor = "PC"
                fim_jogo()

        # Movendo a raquete do pc pra seguir a bola
        if pc_y + raquete_altura // 2 < bola_y:
            pc_y += raquete_pc_dy
        elif pc_y + raquete_altura // 2 > bola_y:
            pc_y -= raquete_pc_dy

        # Evitar que a raquete do pc saia da área
        if pc_y < 0:
            pc_y = 0
        elif pc_y > altura - raquete_altura:
            pc_y = altura - raquete_altura

        # Mostrando Score no jogo
        fonte_score = pygame.font.Font(font_file, 16)
        score_texto = fonte_score.render(
            f"Score PC: {score_pc}       Score Player_1: {score_player_1}", True, BRANCO
        )
        score_rect = score_texto.get_rect(center=(largura // 2, 30))

        screen.blit(score_texto, score_rect)

        # assets (objetos)
        pygame.draw.rect(screen, BRANCO, (pc_x, pc_y, raquete_largura, raquete_altura))
        pygame.draw.rect(
            screen, BRANCO, (player_1_x, player_1_y, raquete_largura, raquete_altura)
        )
        
        # Criar uma superfície para a bola com transparência
        bola_surface = pygame.Surface((tamanho_bola, tamanho_bola), pygame.SRCALPHA)
        pygame.draw.ellipse(
            bola_surface, bola_cor_transparente, (0, 0, tamanho_bola, tamanho_bola)
        )
        screen.blit(bola_surface, (bola_x, bola_y))
        
        pygame.draw.aaline(screen, BRANCO, (largura // 2, 0), (largura // 2, altura))

        # Controle Teclado do Player_1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player_1_y > 0:
            player_1_y -= raquete_player_1_dy
        if keys[pygame.K_DOWN] and player_1_y < altura - raquete_altura:
            player_1_y += raquete_player_1_dy

        pygame.display.flip()

        clock.tick(60)

# fim_jogo()
pygame.quit()
sys.exit()
