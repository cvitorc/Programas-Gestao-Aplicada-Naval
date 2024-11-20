# -*- coding: utf-8 -*-
"""
O convés de um barco é muitas vezes retangular. Esse programa calcula a área de um convés retangular, onde o usuário fornece o comprimento e a largura.
"""

# Função para calcular a área de um retângulo
def area_retangulo(comprimento, largura):
    area = comprimento * largura
    return area

# Exemplo de uso
comprimento = 20  # em metros
largura = 5       # em metros
area = area_retangulo(comprimento, largura)
print(f"A área do convés é: {area} metros quadrados")