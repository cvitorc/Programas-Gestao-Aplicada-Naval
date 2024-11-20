# -*- coding: utf-8 -*-
"""

Análise de Stakeholders: Programa para categorizar stakeholders com base em interesse e influência, usando gráficos de bolhas para visualizar diferentes perfis de stakeholders.
"""

# Importando as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt

# Dados dos stakeholders
# Neste exemplo, vamos criar dados fictícios para cinco stakeholders
# com nível de interesse e influência em uma escala de 1 a 5
dados = {
    'Stakeholder': ['Cliente', 'Diretoria', 'Equipe', 'Fornecedor', 'Comunidade'],
    'Interesse': [5, 4, 3, 2, 1],     # Interesse no projeto (1 - Baixo, 5 - Alto)
    'Influência': [4, 5, 2, 3, 1]     # Influência sobre o projeto (1 - Baixa, 5 - Alta)
}

# Convertendo os dados para um DataFrame
df = pd.DataFrame(dados)

# Configurando o gráfico de dispersão
plt.figure(figsize=(10, 6))
plt.scatter(df['Interesse'], df['Influência'], color='blue', s=100)  # s controla o tamanho dos pontos

# Adicionando rótulos para cada ponto
for i, stakeholder in enumerate(df['Stakeholder']):
    plt.text(df['Interesse'][i], df['Influência'][i], stakeholder, fontsize=12, ha='right')

# Títulos e rótulos
plt.title("Análise de Stakeholders: Interesse vs Influência")
plt.xlabel("Interesse")
plt.ylabel("Influência")

# Limites dos eixos para maior clareza
plt.xlim(0.5, 5.5)
plt.ylim(0.5, 5.5)

# Exibindo o gráfico
plt.grid(True)  # Adiciona linhas de grade para facilitar a leitura
plt.show()