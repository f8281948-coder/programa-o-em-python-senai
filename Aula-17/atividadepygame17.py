# MANIPULAÇÃO DOS EVENTOS
# JOGO LABIRINTO

import pygame

# Inicializa o Pygame
pygame.init()

# ATIVIDADE 1: 

# o que é a estrutura(sintaticamente)? para que serve(contexto)? 
# COMENTE O CÓDIGO, EXPLIQUE COM SUAS PALAVRAS O QUE ESTA OCORRENDO EM CADA ESTRUTURA DO 
# CÓDIGO E VERIFIQUE O QUE OCORRE. 
# CONSULTE A BIBLIOTECA -> https://www.pygame.org/docs/

# 1 - cita a estrutura de código
# 2 - contextualiza 

#escreverei a função em cada linha como um comentário.


#exemplo:
# 2 varáveis , uma defini a altura a outra a largura 
largura, altura = 400, 400 #está definindo o tamanho da tela que vai ser gerada

tela = pygame.display.set_mode((largura, altura)) #está atribuindo os valores da linha 24 para a criação da tela
pygame.display.set_caption("Labirinto") #está dando um nome à tela gerada


preto = (0, 0, 0)
branco = (255, 255, 255)       #essas 3 linhas em conjunto estão dando cores ao display(tela), onde o preto é o limite do mapa, o branco é o labirinto e o vermelho é o personagem(por isso que ainda não está aparecendo no mapa) e 
vermelho = (255, 0, 0)


tamanho_celula = 40 #a célula pode ser lida como uma variável, mas nesse caso, é praticamente o tamanho de cada célula do mapa, cada número no mapa tem o tamanho 40 por causa dessa função
labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],      #esse aqui é basicamente o mapa do jogo, os números dentro desse mapa representam a sua construção
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


x, y = 1 * tamanho_celula, 1 * tamanho_celula
velocidade = 40    #aqui é basicamente a continha realizada para fazer as variáveis anteriores funcionarem do jeito que queremos

def desenhar_labirinto():
    for linha in range(len(labirinto)):
        for coluna in range(len(labirinto[linha])):
            cor = preto if labirinto[linha][coluna] == 1 else branco
            pygame.draw.rect(tela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula)) #esse conjunto todo de linhas está atuando como os "pintores", responsáveis por fazer os desenhos


executando = True #um looping que se estenderá por todo o código a partir de agora
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:   #esse conjunto está trazendo o botão de fechar o jogo para o código e criando um looping infinito
            executando = False


    teclas = pygame.key.get_pressed()  #]]]]]  essa linha em específico, está trazendo a interação do teclado para o jogo e verificando quais teclas estão apertadas
    if teclas[pygame.K_LEFT]:          #]]]] é a condicional que ativa se o botão da seta da esquerda for acionado
        novo_x = x - velocidade     #reduz a velocidade do x para que ele se mova
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0: #vê se não tem nenhuma barreira impedindo o movimento
            x = novo_x #se tiver algo impedindo, x não se altera
    if teclas[pygame.K_RIGHT]: #é a condicional que ativa se o botão da seta da direita for acionado
        novo_x = x + velocidade #reduz a velocidade do x para que ele se mova
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0: #vê se não tem nenhuma barreira impedindo o movimento
            x = novo_x #se tiver algo impedindo, x não se altera
    if teclas[pygame.K_UP]: #é a condicional que ativa se o botão da seta de cima for acionado
        novo_y = y - velocidade #reduz a velocidade do x para que ele se mova
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0: #vê se não tem nenhuma barreira impedindo o movimento
            y = novo_y  #se tiver algo impedindo, y não se altera
    if teclas[pygame.K_DOWN]: #]]]] é a condicional que ativa se o botão da seta de baixo for acionado
        novo_y = y + velocidade  #reduz a velocidade do x para que ele se mova
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0: #vê se não tem nenhuma barreira impedindo o movimento
            y = novo_y #se tiver algo impedindo, y não se altera


    tela.fill(branco) #pinta toda a tela de branco

    
    desenhar_labirinto() #está chamando a célula que trazem a coloração ao mapa
    pygame.draw.rect(tela, vermelho, (x, y, tamanho_celula, tamanho_celula)) #desenha o personagem na tela


    pygame.display.flip() #mostra oque foi desenhado na tela


    pygame.time.Clock().tick(10) #controla a velocidade do jogo


pygame.quit() #simplesmente sai do jogo se para de executar


# subir para o github com os comentários que você fizeram... 