# -*- coding: utf-8 -*-
"""
Esse programa monitora as profundidades ao longo de uma rota e alerta se algum ponto é muito raso para a embarcação.
"""

# Lista de profundidades em metros ao longo da rota
profundidades = [12, 15, 7, 10, 5, 18, 6]
calado_embarcacao = 8  # calado da embarcação em metros

# Verificando se a profundidade é suficiente ao longo da rota
for profundidade in profundidades:
    if profundidade < calado_embarcacao:
        print(f"Atenção! Profundidade de {profundidade} metros é insuficiente para navegação segura.")
    else:
        print(f"Profundidade de {profundidade} metros é adequada.")