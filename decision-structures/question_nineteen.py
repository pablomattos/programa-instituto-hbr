# Faça um algoritmo que leia 3 valores e mostra o menor valor digitado e o maior
# valor digitado.

print("Program that checks wich the smallest and largest number ")

first_number = int(input("Enter a number: "))
second_number = int(input("Enter a number: "))
third_number = int(input("Enter a number: "))

if first_number > second_number and first_number > third_number:
    print(f"The number {first_number} is the largest number.")

if second_number > first_number and second_number > third_number:
    print(f"The number {second_number} is the largest number.")

if third_number > second_number and third_number > first_number:
    print(f"The number {third_number} is the largest number.")

if first_number < second_number and first_number < third_number:
    print(f"The number {first_number} is the smallest number.")

if second_number < first_number and second_number < third_number:
    print(f"The number {second_number} is the smallest number.")

if third_number < second_number and third_number < first_number:
    print(f"The number {third_number} is the smallest number.")