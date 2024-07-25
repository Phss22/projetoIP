# utils.py
import random
from config import TAMANHO_QUADRADO, LARGURA, ALTURA, VERDE, AZUL, AMARELO, VERMELHA

def gerar_comida(pixels):
    tipos_comida = [
        {"cor": VERDE, "pontos": 1},
        {"cor": AZUL, "pontos": 2},
        {"cor": AMARELO, "pontos": 3}
    ]
    tipo_comida = random.choice(tipos_comida)
    comida_x = round(random.randrange(0, LARGURA - TAMANHO_QUADRADO) / 10.0) * 10.0
    comida_y = round(random.randrange(0, ALTURA - TAMANHO_QUADRADO) / 10.0) * 10.0
    while [comida_x, comida_y] in pixels:
        comida_x = round(random.randrange(0, LARGURA - TAMANHO_QUADRADO) / 10.0) * 10.0
        comida_y = round(random.randrange(0, ALTURA - TAMANHO_QUADRADO) / 10.0) * 10.0
    return comida_x, comida_y, tipo_comida["cor"], tipo_comida["pontos"]

def gerar_bomba(pixels, comida_x, comida_y):
    bomba_x = round(random.randrange(0, LARGURA - TAMANHO_QUADRADO) / 10.0) * 10.0
    bomba_y = round(random.randrange(0, ALTURA - TAMANHO_QUADRADO) / 10.0) * 10.0
    while ([bomba_x, bomba_y] in pixels) or ([bomba_x, bomba_y] == [comida_x, comida_y]):
        bomba_x = round(random.randrange(0, LARGURA - TAMANHO_QUADRADO) / 10.0) * 10.0
        bomba_y = round(random.randrange(0, ALTURA - TAMANHO_QUADRADO) / 10.0) * 10.0
    return bomba_x, bomba_y
