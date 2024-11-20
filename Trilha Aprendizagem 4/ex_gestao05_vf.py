# -*- coding: utf-8 -*-
"""

Programa que calcula índices como CPI (Índice de Performance de Custo) e SPI (Índice de Performance de Prazo), criando gráficos para ilustrar o desempenho do projeto. Dados no arquivo excel.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo Excel com os dados do projeto
arquivo_excel = "dados_projeto_TI.xlsx"

# Carregar os dados do Excel
df = pd.read_excel(arquivo_excel)

# Cálculos de EVA
df['CPI'] = df['EV'] / df['AC']  # Índice de Performance de Custo
df['SPI'] = df['EV'] / df['PV']  # Índice de Performance de Prazo

# Gráfico de CPI e SPI
plt.figure(figsize=(10, 5))
plt.plot(df['Periodo'], df['CPI'], marker='o', label='Índice de Performance de Custo (CPI)')
plt.plot(df['Periodo'], df['SPI'], marker='o', label='Índice de Performance de Prazo (SPI)')
plt.axhline(y=1, color='r', linestyle='--', label='Linha de Base (1.0)')
plt.title('Índices de Performance CPI e SPI')
plt.xlabel('Período')
plt.ylabel('Índice')
plt.legend()
plt.grid(True)

# Salvando o gráfico como imagem
plt.savefig("CPI_SPI.png", format="png", dpi=300)

plt.show()