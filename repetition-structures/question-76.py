# Faça um programa que pede para o usuário digitar várias profissões e no final
# mostre quantas vezes foi digitado a profissão professor. Para parar o algoritmo, o usuário deverá
# digitar 0. Considere o termo "professor ou Professor ou PROFESSOR".
number_of_names = 0
proceed = True

try:
    while proceed:
        entered_profession = input("Digite uma profissão (ou 0 para parar):")
        if entered_profession == "0":
            proceed = False

        for profession in entered_profession.split():
            if profession.upper() == "PROFESSOR":
                number_of_names += 1

except:
    print("Você digitou uma profissão inválida!")

else:
    print(f"O nome professor foi digitado {number_of_names} vezes")


