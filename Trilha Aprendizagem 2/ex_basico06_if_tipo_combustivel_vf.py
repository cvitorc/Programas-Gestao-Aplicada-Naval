# -*- coding: utf-8 -*-
"""
Essa função verifica o tipo de combustível necessário para a embarcação com base em seu tamanho.
"""

def tipo_combustivel(tamanho_embarcacao):
    if tamanho_embarcacao < 10:
        return "Use gasolina para esta embarcação."
    elif tamanho_embarcacao <= 20:
        return "Use diesel para esta embarcação."
    else:
        return "Use óleo pesado para esta embarcação."

# Exemplo de uso
tamanho = 15
print(tipo_combustivel(tamanho))