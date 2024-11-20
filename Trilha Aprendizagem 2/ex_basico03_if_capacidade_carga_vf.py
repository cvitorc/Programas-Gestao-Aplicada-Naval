# -*- coding: utf-8 -*-
"""

Essa função classifica uma embarcação como pequena, média ou grande com base em sua capacidade de carga.
"""

def classificar_embarcacao(capacidade_carga):
    if capacidade_carga < 50:
        return "Esta é uma embarcação pequena."
    elif capacidade_carga <= 150:
        return "Esta é uma embarcação média."
    else:
        return "Esta é uma embarcação grande."

# Exemplo de uso
capacidade = 100
print(classificar_embarcacao(capacidade))