# Faça um programa que pede para o usuário digitar várias profissões e no final
# mostre quantas vezes foi digitado a profissão professor. Para parar o algoritmo, o usuário deverá
# digitar 0. Considere o termo "professor ou Professor ou PROFESSOR".
from tokenize import Number

number_of_names = 0
proceed = True

try:
    while proceed:
        entered_profession = input("Enter a profission (or 0 to stop):")
        if entered_profession == "0":
            proceed =False

        for profession in entered_profession.split():
            if profession.upper() == "PROFESSOR":
                number_of_names += 1

except:
    print("You entered a valid profession")

else:
    print(f"O nome professor foi digitado {number_of_names} vezes")


