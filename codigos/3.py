
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
pygame.display.set_caption("Game 03 - Personagem")

# Carregar personagem
personagem = carregar_imagem("personagem.png", 85, 85)

# Posição inicial do personagem
x = 80
y = 600  # mais embaixo

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Cor de fundo
    tela.fill((135, 206, 235))

    # Desenhar personagem
    tela.blit(personagem, (x, y))

    # Atualizar tela
    pygame.display.flip()

# Encerrar
pygame.quit()