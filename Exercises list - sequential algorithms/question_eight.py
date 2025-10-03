import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Questão 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

hour_value = 0
number_of_hours_worked = 0
salary_of_the_month = 0

print("Programa que calcula o salário do mês a partir do valor da hora e número de horas trabalhadas")
hour_value = float(input("Digite o valor da hora trabalhada: "))
number_of_hours_worked = float(input("Digite o número de dias trabalhados: "))

salary_of_the_month = hour_value * number_of_hours_worked
formatted_salary_of_the_month = locale.currency(salary_of_the_month, grouping=True)

print("O valor do salário do mês é:  ", formatted_salary_of_the_month)