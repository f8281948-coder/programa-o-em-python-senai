import pygame
import sys
import random

pygame.init()

# tamanho da tela
LARGURA = 800
ALTURA = 400

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("T-Rex Runner")

# carregar imagens
trex1 = pygame.image.load("trex1.png")
trex2 = pygame.image.load("trex3.png")
cacto_img = pygame.image.load("obstacle1.png")
chao = pygame.image.load("ground2.png")

# posição do chão
CHAO_Y = 340

# posição do trex
trex_x = 100
trex_y = CHAO_Y - trex1.get_height()

# física do pulo
vel_y = 0
gravidade = 1
forca_pulo = -20
pulando = False

# chão infinito
chao_x = 0

# cacto
cacto_x = 800
cacto_y = CHAO_Y - cacto_img.get_height()

# animação
frame = 0

# pontuação
score = 0
fonte = pygame.font.SysFont("Arial", 30)

# controle do jogo
game_over = False

clock = pygame.time.Clock()

while True:

    # eventos
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # pular
        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_SPACE and not pulando:
                vel_y = forca_pulo
                pulando = True

            if evento.key == pygame.K_r and game_over:

                # reiniciar jogo
                trex_y = CHAO_Y - trex1.get_height()
                cacto_x = 800
                cacto_y = CHAO_Y - cacto_img.get_height()

                vel_y = 0
                pulando = False

                score = 0
                game_over = False

    if not game_over:

        # -------------------------
        # FÍSICA DO PULO
        # -------------------------

        vel_y += gravidade
        trex_y += vel_y

        # limitar no chão
        if trex_y >= CHAO_Y - trex1.get_height():
            trex_y = CHAO_Y - trex1.get_height()
            vel_y = 0
            pulando = False

        # -------------------------
        # MOVER CHÃO
        # -------------------------

        chao_x -= 5

        if chao_x <= -800:
            chao_x = 0

        # -------------------------
        # MOVER CACTO
        # -------------------------

        cacto_x -= 5

        if cacto_x < -50:
            cacto_x = random.randint(800, 1000)
            score += 1

        # -------------------------
        # ANIMAÇÃO
        # -------------------------

        frame += 1

        if frame > 20:
            frame = 0

        if frame < 10:
            trex = trex1
        else:
            trex = trex2

        # -------------------------
        # COLISÃO
        # -------------------------

        # retângulo original do T-Rex
        trex_rect = trex.get_rect(
            topleft=(trex_x, trex_y)
        )

        # hitbox menor do T-Rex
        trex_hitbox = pygame.Rect(
            trex_rect.x + 15,
            trex_rect.y + 10,
            trex_rect.width - 30,
            trex_rect.height - 15
        )

        # retângulo original do cacto
        cacto_rect = cacto_img.get_rect(
            topleft=(cacto_x, cacto_y)
        )

        # hitbox menor do cacto
        cacto_hitbox = pygame.Rect(
            cacto_rect.x + 10,
            cacto_rect.y + 5,
            cacto_rect.width - 20,
            cacto_rect.height - 5
        )

        # verificar colisão
        if trex_hitbox.colliderect(cacto_hitbox):
            game_over = True

    # -------------------------
    # DESENHAR FUNDO
    # -------------------------

    tela.fill((255, 255, 255))

    # chão infinito
    tela.blit(chao, (chao_x, CHAO_Y))
    tela.blit(chao, (chao_x + 800, CHAO_Y))

    # desenhar trex
    tela.blit(trex, (trex_x, trex_y))

    # desenhar cacto
    tela.blit(cacto_img, (cacto_x, cacto_y))

    # pontuação
    texto = fonte.render(
        "Score: " + str(score),
        True,
        (0, 0, 0)
    )

    tela.blit(texto, (650, 20))

    # game over
    if game_over:

        texto2 = fonte.render(
            "GAME OVER - Aperte R",
            True,
            (255, 0, 0)
        )

        tela.blit(texto2, (250, 200))

    pygame.display.update()

    clock.tick(30)