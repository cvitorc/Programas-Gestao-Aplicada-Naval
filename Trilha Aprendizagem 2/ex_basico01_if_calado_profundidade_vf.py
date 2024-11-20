# -*- coding: utf-8 -*-
"""

Essa função verifica se uma embarcação com determinado calado pode navegar em uma profundidade específica.
"""

def verificar_profundidade(calado_embarcacao, profundidade_agua):
    if profundidade_agua > calado_embarcacao:
        return "A embarcação pode navegar nesta profundidade."
    else:
        return "A embarcação não pode navegar nesta profundidade; a água é muito rasa."

# Exemplo de uso
calado = 4.0
profundidade = 5.0
print(verificar_profundidade(calado, profundidade))