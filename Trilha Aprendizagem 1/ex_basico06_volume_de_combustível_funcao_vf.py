# -*- coding: utf-8 -*-
"""

Esse programa calcula o volume de combustível necessário para uma viagem, baseado na distância e no consumo da embarcação.
"""

# Função para calcular o volume de combustível
def volume_combustivel(distancia, consumo_por_milha):
    volume = distancia * consumo_por_milha
    return volume

# Exemplo de uso
distancia = 100  # distância em milhas náuticas
consumo_por_milha = 0.5  # consumo em litros por milha náutica
volume = volume_combustivel(distancia, consumo_por_milha)
print(f"O volume de combustível necessário é: {volume:.2f} litros")