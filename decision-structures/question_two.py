#  Faça um algoritmo que leia um número e mostrar se ele é positivo ou negativo.
print("Program that checks if a number is positive or negative: ")
number_entered = int(input("Enter a number: "))

if number_entered > 0:
    print(f"The number {number_entered} is positive.")

elif number_entered < 0:
    print(f"The number {number_entered} is negative.")

else:
    print(f"The number entered is equal to zero")


