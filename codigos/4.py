
import pygame
import os

# Iniciar o pygame
pygame.init()

# Caminho da pasta de imagens
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(os.path.dirname(BASE_DIR), "imagens")

# Função para carregar imagem
def carregar_imagem(nome, largura, altura):
    caminho = os.path.join(PASTA_IMAGENS, nome)
    imagem = pygame.image.load(caminho).convert_alpha()
    imagem = pygame.transform.scale(imagem, (largura, altura))
    return imagem

# Criar a janela
LARGURA = 720
ALTURA = 720
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Game 04 - Obstáculo")

# Carregar imagens
personagem = carregar_imagem("personagem.png", 85, 85)
obstaculo = carregar_imagem("obstaculo1.png", 80, 80)

# Posições
x = 80
y = 600  # mais embaixo

obstaculo_x = 390
obstaculo_y = 620  # alinhado com o chão

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Cor de fundo
    tela.fill((135, 206, 235))

    # Desenhar na tela
    tela.blit(personagem, (x, y))
    tela.blit(obstaculo, (obstaculo_x, obstaculo_y))

    # Atualizar tela
    pygame.display.flip()

# Encerrar
pygame.quit()

