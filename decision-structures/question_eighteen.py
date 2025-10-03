# Melhore o programa anterior, faça um algoritmo para ler dois números inteiros e
# informar se os números são iguais ou se são diferentes e, se são diferentes mostrar o maior valor

print("Program that checks is the numbers entered are the same number or what is the largest number!")
first_number = int(input("Enter a number: "))
second_number = int(input("Enter other number: "))

if first_number == second_number:
    print(f"The number {first_number} and {second_number} are the same number!")

else:
    if first_number > second_number:
        print(f"The number {first_number} is greater than the number {second_number}")

    else:
        print(f"The number {second_number} is greater than the number {first_number}")