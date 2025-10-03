#  Faça um algoritmo para ler 4 números inteiros e informar se a soma dos dois
# primeiros números é igual a soma dos outros valores. Se a soma for igual, mostrar os 4 valores e
# suas respectivas somas, caso contrário indicar se as somas dos valores são pares ou ímpares.

print("Program that checks if the sum of the first two numbers is equal the sum of the last numbers")

first_number = int(input("Enter a number: "))
second_number = int(input("Enter other number: "))
third_number = int(input("Enter other number: "))
fourth_number = int(input("Enter other number: "))

sum_of_the_first_two_numbers = first_number + second_number
sum_of_the_last_numbers = third_number + fourth_number

if sum_of_the_first_two_numbers == sum_of_the_last_numbers:
    print(f"First number entered: {first_number}")
    print(f"Second number entered: {second_number}")
    print(f"Third number entered: {third_number}")
    print(f"Fourth number entered: {fourth_number}")
    print(f"{first_number} + {second_number} = {sum_of_the_first_two_numbers}")
    print(f"{third_number} + {fourth_number} = {sum_of_the_last_numbers}")

else:
    if sum_of_the_first_two_numbers % 2 == 0:
        print(f"The sum of the first two numbers is {sum_of_the_first_two_numbers} that is even")

    else:
        print(f"The sum of the first two numbers is {sum_of_the_first_two_numbers} that is odd")

    if sum_of_the_last_numbers % 2 == 0:
        print(f"The sum of the last numbers is {sum_of_the_last_numbers} that is even")

    else:
        print(f"The sum of the last numbers is {sum_of_the_last_numbers} that is odd")

