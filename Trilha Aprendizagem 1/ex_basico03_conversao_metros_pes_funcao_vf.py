# -*- coding: utf-8 -*-


# Função para converter metros para pés
def metros_para_pes(metros):
    pes = metros * 3.28084  # 1 metro = 3.28084 pés
    return pes

# Exemplo de uso
metros = 10
pes = metros_para_pes(metros)
print(f"{metros} metros são aproximadamente {pes:.2f} pés")