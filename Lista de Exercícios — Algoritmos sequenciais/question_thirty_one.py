## Questão 31. Entre com uma data e mostre a data no formato: DD/MM/ANO

day = 0
month = 0
year = 0

print("Programa que formata (DD/MM/ANO) a data a partir dos valores de dia, mês e ano digitados")
day = int(input("Digite o dia: "))
formatted_day = f"{day:02d}"

month = int(input("Digite o mês: "))
formatted_month = f"{month:02d}"

year = int(input("Digite o ano:"))

print("Data formatada: ", formatted_day,"/",formatted_month,"/",year)