# game.py
import pygame
from config import LARGURA, ALTURA, TAMANHO_QUADRADO, VELOCIDADE_JOGO, PRETA, VERMELHA, BRANCA
from draw import desenhar_comida, desenhar_bomba, desenhar_cobra, desenhar_pontuacao
from utils import gerar_comida, gerar_bomba

def selecionar_velocidade(tecla, velocidade_x, velocidade_y):
    if tecla == pygame.K_DOWN:
        if velocidade_y != -TAMANHO_QUADRADO:
            velocidade_x = 0
            velocidade_y = TAMANHO_QUADRADO
    elif tecla == pygame.K_UP:
        if velocidade_y != TAMANHO_QUADRADO:
            velocidade_x = 0
            velocidade_y = -TAMANHO_QUADRADO
    elif tecla == pygame.K_RIGHT:
        if velocidade_x != -TAMANHO_QUADRADO:
            velocidade_x = TAMANHO_QUADRADO
            velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        if velocidade_x != TAMANHO_QUADRADO:
            velocidade_x = -TAMANHO_QUADRADO
            velocidade_y = 0
    return velocidade_x, velocidade_y

def fim_de_jogo(tela, pontuacao):
    fim_jogo = True
    while fim_jogo:
        tela.fill(PRETA)
        fonte = pygame.font.SysFont("Helvetica", 50)
        fonte_menor = pygame.font.SysFont("Helvetica", 40)
        mensagem = fonte.render("Fim de Jogo", True, VERMELHA)
        pontuacao_texto = fonte_menor.render(f"Pontuação: {pontuacao}", True, BRANCA)
        reiniciar = fonte_menor.render("Pressione ENTER para Jogar Novamente", True, BRANCA)
        tela.blit(mensagem, (LARGURA / 2 - mensagem.get_width() / 2, ALTURA / 3))
        tela.blit(pontuacao_texto, (LARGURA / 2 - pontuacao_texto.get_width() / 2, ALTURA / 2))
        tela.blit(reiniciar, (LARGURA / 2 - reiniciar.get_width() / 2, ALTURA / 1.5))
        pygame.display.update()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    fim_jogo = False
                    return True
    return False

def rodar_jogo(tela, relogio):
    fim_jogo = False
    x = LARGURA / 2
    y = ALTURA / 2
    velocidade_x = 0
    velocidade_y = 0
    tamanho_cobra = 1
    pixels = []
    pontuacao = 0
    comida_x, comida_y, cor_comida, pontos_comida = gerar_comida(pixels)
    bomba_x, bomba_y = gerar_bomba(pixels, comida_x, comida_y)

    while not fim_jogo:
        tela.fill(PRETA)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key, velocidade_x, velocidade_y)
        
        x += velocidade_x
        y += velocidade_y

        if x < 0 or x >= LARGURA or y < 0 or y >= ALTURA:
            fim_jogo = True

        desenhar_comida(tela, TAMANHO_QUADRADO, comida_x, comida_y, cor_comida)
        desenhar_bomba(tela, TAMANHO_QUADRADO, bomba_x, bomba_y)
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]
        
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True
        
        desenhar_cobra(tela, TAMANHO_QUADRADO, pixels)
        desenhar_pontuacao(tela, pontuacao)
        pygame.display.update()

        if x == comida_x and y == comida_y:
            tamanho_cobra += 4
            pontuacao += pontos_comida
            comida_x, comida_y, cor_comida, pontos_comida = gerar_comida(pixels)
            bomba_x, bomba_y = gerar_bomba(pixels, comida_x, comida_y)
        
        if x == bomba_x and y == bomba_y:
            fim_jogo = True

        relogio.tick(VELOCIDADE_JOGO)
    return pontuacao
