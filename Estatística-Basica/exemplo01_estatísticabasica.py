import pandas as pd

# Conjunto de notas de 10 alunos
notas = [7.5, 8.0, 6.0, 9.0, 5.5, 8.5, 7.0, 7.5, 8.0, 6.5]

# Criar uma Série do Pandas a partir do conjunto de notas
notas_series = pd.Series(notas)

# Calcular a média
media = notas_series.mean()

# Calcular a mediana
mediana = notas_series.median()

# Calcular a moda
moda = notas_series.mode().values[0]  # .mode() retorna uma Série, usamos .values[0] para pegar o primeiro valor

# Calcular o desvio padrão
desvio_padrao = notas_series.std()

# Exibir os resultados
print(f"Média: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Desvio Padrão: {desvio_padrao}")

"""Explicação do Código:
Importação do pandas: Importamos a biblioteca pandas, que facilita a manipulação de dados.

Criação da Série notas_series: Transformamos o conjunto de notas em uma Série do pandas, o que permite calcular as medidas descritivas diretamente.

Cálculo de Média, Mediana, Moda e Desvio Padrão: Utilizamos métodos como .mean(), .median(), .mode(), e .std() para encontrar as estatísticas desejadas.

Exibição dos Resultados: Usamos print() para exibir cada medida.

"""