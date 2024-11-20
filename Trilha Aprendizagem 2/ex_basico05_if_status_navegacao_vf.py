# -*- coding: utf-8 -*-
"""

Essa função ajuda a decidir se a embarcação pode sair para navegar com base nas condições climáticas.
"""

def status_navegacao(vento_kmh, altura_ondas_m):
    if vento_kmh < 30 and altura_ondas_m < 1.5:
        return "Condições seguras para navegar."
    elif 30 <= vento_kmh <= 60 and altura_ondas_m <= 2.5:
        return "Cuidado: Condições moderadas. Navegue com cautela."
    else:
        return "Perigo! Condições de navegação inseguras."

# Exemplo de uso
vento = 50
altura_ondas = 2
print(status_navegacao(vento, altura_ondas))