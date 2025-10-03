# Escreva um programa em Python 3 que leia um número inteiro que representa um código de DDD
# para discagem interurbana. Em seguida, informe à qual cidade o DDD pertence, considerando a
# tabela abaixo:
from zoneinfo import reset_tzpath

# 51 Porto Alegre
# 61 Salvador
# 11 São Paulo
# 21 Rio de Janeiro
# 31 Belo Horizonte
# 54 Caxias do Sul
# 55 Santa Maria
# 53 Pelotas

#"Program that checks if the ddd code is valid or not"

code_entered = int(input())

match code_entered:
    case 51:
        print("Porto Alegre")

    case 61:
        print("Salvador")

    case 11:
        print("São Paulo")

    case 21:
        print("Rio de Janeiro")

    case 31:
        print("Belo Horizonte")

    case 54:
        print("Caxias do Sul")

    case 55:
        print("Santa Maria")

    case 53:
        print("Pelotas")

    case _:
        print("DDD não cadastrado")




