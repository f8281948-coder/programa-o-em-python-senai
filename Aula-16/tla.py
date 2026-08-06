import pygame


pygame.init()


janela = pygame.display.set_mode([500 , 700])

run = True
while run:
    for evento in pygame.event.get():
     if evento.type == pygame.QUIT:
        run = False