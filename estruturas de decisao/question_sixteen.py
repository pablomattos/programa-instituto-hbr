# Faça um algoritmo que leia um número e
# mostre se ele é divisível por 3 E por 7

print("Program that checks if the number entered is divisible by three or seven")
number_entered = int(input("Enter a number: "))

if number_entered % 3 == 0 and number_entered % 7 == 0:
        print(f"The number {number_entered} is divisible by 3 and 7.")

else:
    print(f"The number {number_entered} is not divisible by 3 and 7.")