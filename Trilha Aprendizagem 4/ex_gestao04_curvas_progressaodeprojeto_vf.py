# -*- coding: utf-8 -*-
"""

A Curva S é uma ferramenta de monitoramento de progresso que permite visualizar o avanço do projeto ao longo do tempo. Ela mostra o valor planejado (PV), o valor agregado (EV) e o custo real (AC) em cada ponto do cronograma, permitindo comparar o progresso atual com o planejado.
"""

# Importando as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt

# Simulando dados do projeto (em unidades de tempo e valores)
# Suponha um projeto com duração de 12 meses
meses = list(range(1, 13))

# Valores planejados, agregados e custos reais (em milhares de reais)
# Dados fictícios simulando o crescimento dos valores ao longo do tempo
valor_planejado = [10, 20, 35, 50, 70, 90, 110, 130, 150, 170, 190, 200]  # PV
valor_agregado = [8, 18, 30, 45, 65, 85, 100, 125, 140, 160, 185, 195]    # EV
custo_real = [9, 19, 33, 48, 67, 92, 108, 128, 145, 165, 190, 200]        # AC

# Configurando o DataFrame para organizar os dados
df = pd.DataFrame({
    'Meses': meses,
    'Valor Planejado (PV)': valor_planejado,
    'Valor Agregado (EV)': valor_agregado,
    'Custo Real (AC)': custo_real
})

# Configurando o gráfico
plt.figure(figsize=(10, 6))

# Plotando as três curvas
plt.plot(df['Meses'], df['Valor Planejado (PV)'], label='Valor Planejado (PV)', linestyle='--', color='blue', marker='o')
plt.plot(df['Meses'], df['Valor Agregado (EV)'], label='Valor Agregado (EV)', linestyle='-', color='green', marker='o')
plt.plot(df['Meses'], df['Custo Real (AC)'], label='Custo Real (AC)', linestyle='-', color='red', marker='o')

# Títulos e rótulos
plt.title("Curva S de Progresso do Projeto")
plt.xlabel("Meses")
plt.ylabel("Valor Acumulado (em milhares de reais)")
plt.legend()

# Exibindo a grade para facilitar a leitura
plt.grid(True, linestyle='--', alpha=0.7)

# Exibindo o gráfico
plt.show()

"""Explicação do Código
Dados Simulados:
meses: Período do projeto, com 12 meses.
valor_planejado: Progresso planejado acumulado para cada mês (PV).
valor_agregado: Progresso real do trabalho realizado até o momento (EV).
custo_real: Custo acumulado ao longo do tempo (AC).
Configuração do Gráfico:
Linha Azul Tracejada representa o Valor Planejado (PV).
Linha Verde Contínua representa o Valor Agregado (EV).
Linha Vermelha Contínua representa o Custo Real (AC).
Marcadores em cada ponto facilitam a visualização dos dados mensais.
Interpretação da Curva S:
Quando o EV está abaixo do PV, o projeto está atrasado.
Se o AC está acima do EV, o projeto está acima do orçamento.
Quando o EV se aproxima do PV e o AC está próximo do EV, o projeto está no prazo e orçamento.
Análise
Esse gráfico ajuda a comparar o andamento planejado com o real. É possível identificar desvios e tomar medidas corretivas para trazer o projeto de volta ao cronograma e orçamento planejados.
"""