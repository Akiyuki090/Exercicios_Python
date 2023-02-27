import pygame
import random


# Configurações do jogo
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
CELL_SIZE = 10

# Inicializa o Pygame
pygame.init()

# Cria a janela do jogo
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Jogo da Cobrinha')

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Função para desenhar a cobra na tela


def draw_snake(snake):
    for pos in snake:
        pygame.draw.rect(screen, GREEN, (pos[0], pos[1], CELL_SIZE, CELL_SIZE))

# Função principal do jogo


def game():
    # Posição inicial da cobra
    snake = [[SCREEN_WIDTH/2, SCREEN_HEIGHT/2]]

    # Direção inicial da cobra
    direction = 'RIGHT'

    # Loop principal do jogo
    while True:
        # Verifica os eventos do teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    direction = 'RIGHT'
                elif event.key == pygame.K_UP:
                    direction = 'UP'
                elif event.key == pygame.K_DOWN:
                    direction = 'DOWN'

        # Move a cobra
        if direction == 'LEFT':
            snake[0][0] -= CELL_SIZE
        elif direction == 'RIGHT':
            snake[0][0] += CELL_SIZE
        elif direction == 'UP':
            snake[0][1] -= CELL_SIZE
        elif direction == 'DOWN':
            snake[0][1] += CELL_SIZE

        # Desenha a cobra na tela
        screen.fill(BLACK)
        draw_snake(snake)
        pygame.display.update()


# Inicia o jogo
game()
