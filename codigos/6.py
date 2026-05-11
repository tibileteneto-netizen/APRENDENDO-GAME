import pygame
import os

pygame.init()

BASE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(os.path.dirname(BASE), "imagens")

def carregar_imagem(nome, largura, altura):
    caminho = os.path.join(IMG, nome)
    imagem = pygame.image.load(caminho).convert_alpha()
    return pygame.transform.scale(imagem, (largura, altura))

LARGURA = 720
ALTURA = 720
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Game 06 - Movimento")

personagem = carregar_imagem("personagem.png", 85, 85)
obstaculo = carregar_imagem("obstaculo1.png", 80, 80)
objetivo = carregar_imagem("objetivo.png", 75, 75)

chao = 650

x = 80
y = chao - 85
vel = 5

obstaculo_x = 390
obstaculo_y = chao - 80

objetivo_x = 620
objetivo_y = chao - 75

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_RIGHT]:
        x += vel

    if teclas[pygame.K_LEFT]:
        x -= vel

    tela.fill((135, 206, 235))

    tela.blit(personagem, (x, y))
    tela.blit(obstaculo, (obstaculo_x, obstaculo_y))
    tela.blit(objetivo, (objetivo_x, objetivo_y))

    pygame.display.flip()

pygame.quit()
