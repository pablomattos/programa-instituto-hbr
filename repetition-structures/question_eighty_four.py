# Faça um programa que entre com 8 nomes e imprima quantas letras tem cada
# nome

proceed = True
while proceed:
    try:
        names = input().split()

        if len(names) == 8:
            for name in names:
                print(f"The name {name} has {len(name)} letters ")

        else:
            raise ValueError(f"You entered {len(names)} names and only you can enter 10 names!")
        proceed = False

    except Exception as e:
        print(e)

