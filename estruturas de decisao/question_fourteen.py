# . Faça um algoritmo que leia um número,
# mostre na tela se ele é divisível por 11.

print("Program that checks if a number entered is divisible by eleven or not")
number_entered = int(input("Enter a number: "))

if number_entered % 11 == 0:
    print(f"The number {number_entered} is divisible by 11!")

else:
    print(f"The number {number_entered} is not divisible by 11!")