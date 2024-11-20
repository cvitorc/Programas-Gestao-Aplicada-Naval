# -*- coding: utf-8 -*-
"""

A velocidade dos barcos é geralmente medida em nós, mas pode ser útil converter para quilômetros por hora.
"""

# Função para converter nós para km/h
def nos_para_kmh(nos):
    kmh = nos * 1.852  # 1 nó = 1.852 km/h
    return kmh

# Exemplo de uso
nos = 15
kmh = nos_para_kmh(nos)
print(f"{nos} nós são aproximadamente {kmh:.2f} km/h")