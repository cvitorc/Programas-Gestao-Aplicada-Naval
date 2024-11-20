import pandas as pd

# Criar um DataFrame simples
data = {
    "Nome": ["Carlos", "Ana", "João", "Maria"],
    "Idade": [25, 30, 35, 40],
    "Cidade": ["Rio", "São Paulo", "Belo Horizonte", "Salvador"]
}

df = pd.DataFrame(data)

# Exibir o DataFrame
print("DataFrame Criado:")
print(df)

# Calcular estatísticas básicas
print("\nEstatísticas Básicas:")
print(df.describe(include="all"))

# Filtrar pessoas com idade maior que 30
print("\nPessoas com idade maior que 30:")
print(df[df["Idade"] > 30])
