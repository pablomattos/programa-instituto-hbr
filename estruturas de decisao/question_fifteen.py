# Faça um algoritmo que leia um número e
# mostre se ele é divisível por 5 OU por 9.

print("Program that checks if the number entered is divisible by five or nine!")
number_entered = int(input("Enter a number: "))

if number_entered % 5 == 0:
    print(f"The number {number_entered} is divisible by 5!")

elif number_entered % 9 == 0:
    print(f"The number {number_entered} is divisible by 9!")

else:
    print(f"The number {number_entered} is not divisible by 5 or 9!")