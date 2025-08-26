
"""
4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.
"""

import datetime

def calcular_dias_vivo(data_nascimento):
    data_atual = datetime.datetime.now()
    dias_vivos = (data_atual - data_nascimento).days
    return dias_vivos

data_nascimento_str = input("Digite sua data de nascimento (DD/MM/AAAA): ")
data_nascimento = datetime.datetime.strptime(data_nascimento_str, "%d/%m/%Y")
dias_vivos = calcular_dias_vivo(data_nascimento)
print(f"Você está vivo há {dias_vivos} dias.")