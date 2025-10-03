##Questão 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

first_note = 0
second_note = 0
third_note = 0
fourth_note = 0
grade_average = 0

print("Programa que calcula a média de quatro notas de um aluno")
first_note = float(input("Digite a primeira nota: "))
second_note = float(input("Digite a segunda nota: "))
third_note = float(input("Digite a terceira nota: "))
fourth_note = float(input("Digite a quarta nota: "))

grade_average = ( first_note + second_note + third_note + fourth_note )/ 4

print("A média das notas é: ", grade_average )


