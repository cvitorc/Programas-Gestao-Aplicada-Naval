# -*- coding: utf-8 -*-


# Função para converter Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Exemplo de uso
celsius = 25
fahrenheit = celsius_para_fahrenheit(celsius)
print(f"{celsius}°C é igual a {fahrenheit}°F")