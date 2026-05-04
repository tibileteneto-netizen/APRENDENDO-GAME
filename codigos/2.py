import pygame

pygame.init()

LARGURA, ALTURA = 720, 720
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Meu primeiro jogo")

# Variável com a cor do fundo em RGB
COR_FUNDO = (30, 144, 255)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Pintar o fundo da tela
    tela.fill(COR_FUNDO)

    pygame.display.flip()

pygame.quit()