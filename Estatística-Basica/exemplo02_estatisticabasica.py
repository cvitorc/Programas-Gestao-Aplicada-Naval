import pandas as pd

# Dados de exemplo: idades e tempo médio de sono (em horas)
dados = {
    'Idades': [20, 22, 25, 30, 35, 40, 45, 50, 55, 60],
    'Sono (horas)': [7.5, 8.0, 6.5, 7.0, 6.0, 5.5, 5.0, 6.5, 5.5, 5.0]
}

# Criar um DataFrame com os dados
df = pd.DataFrame(dados)

# Calcular a média de horas de sono
media_sono = df['Sono (horas)'].mean()

# Calcular a variância do tempo médio de sono
variancia_sono = df['Sono (horas)'].var()

# Calcular o desvio padrão do tempo médio de sono
desvio_padrao_sono = df['Sono (horas)'].std()

# Exibir os resultados
print(f"Média de Sono: {media_sono} horas")
print(f"Variância: {variancia_sono}")
print(f"Desvio Padrão: {desvio_padrao_sono}")

"""Explicação do Código

Importação do pandas: Para manipulação de dados.

Criação do DataFrame df: Contém as idades e o tempo médio de sono.

Cálculos de Média, Variância e Desvio Padrão:

Média: .mean() calcula a média de horas de sono.

Variância: .var() mede a dispersão dos dados em relação à média.

Desvio Padrão: .std() indica a dispersão média dos dados em relação à média.

"""