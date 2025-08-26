"""
4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.
"""
def calcular_dias_vivo(anos, meses, dias):
    dias_por_ano = 365
    dias_por_mes = 30
    total_dias = (anos * dias_por_ano) + (meses * dias_por_mes) + dias
    return total_dias

anos = int(input("Digite a quantidade de anos: "))
meses = int(input("Digite a quantidade de meses: "))
dias = int(input("Digite a quantidade de dias: "))
dias_vivos = calcular_dias_vivo(anos, meses, dias)
print(f"Você está vivo há {dias_vivos} dias.")
