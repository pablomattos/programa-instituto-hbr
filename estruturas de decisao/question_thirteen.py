# Questão 13. Faça um algoritmo que leia um número,
# mostre na tela se ele é ou não divisível por 5

print("Program that checks if a number divisible by five or not ")
number_entered = int(input("Enter a number: "))

if number_entered % 5 == 0:
    print(f"The number {number_entered} is divisible by 5")

else:
    print(f"The number {number_entered} is not divisible by 5")