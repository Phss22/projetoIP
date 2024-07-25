# draw.py
import pygame
from config import BRANCA, VERMELHA, PRETA

def desenhar_comida(tela, tamanho, comida_x, comida_y, cor):
    pygame.draw.rect(tela, cor, [comida_x, comida_y, tamanho, tamanho])

def desenhar_bomba(tela, tamanho, bomba_x, bomba_y):
    pygame.draw.rect(tela, VERMELHA, [bomba_x, bomba_y, tamanho, tamanho])

def desenhar_cobra(tela, tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, BRANCA, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(tela, pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 35)
    texto = fonte.render(f"Pontos: {pontuacao}", True, VERMELHA)
    tela.blit(texto, [10, 10])
