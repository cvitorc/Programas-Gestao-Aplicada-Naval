# -*- coding: utf-8 -*-
"""
Essa função verifica se a velocidade de uma embarcação está dentro do limite permitido.
"""

def checar_velocidade(velocidade_embarcacao, limite_velocidade):
    if velocidade_embarcacao > limite_velocidade:
        return "Atenção: A embarcação está acima do limite de velocidade permitido!"
    else:
        return "A embarcação está dentro do limite de velocidade permitido."

# Exemplo de uso
velocidade = 20
limite = 15
print(checar_velocidade(velocidade, limite))