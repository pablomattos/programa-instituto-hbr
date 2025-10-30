# Escreva um algoritmo para repetir a leitura de uma senha até que ela seja válida.
# Para cada leitura da senha incorreta informada escrever a mensagem "SENHA INVÁLIDA". Quanto
# a senha for informada corretamente deve ser impressa a mensagem "ACESSO PERMITIDO"e o
# algoritmo é encerrado mostrando quantas vezes a senha foi digitada. Considere que a senha
# correta o valor 2014.

password = 2014
password_valid = False
count_of_passwords_entered = 0

while not password_valid:
    try:
        password = int(input("Digite a senha: "))
        count_of_passwords_entered += 1
        if password == 2014:
            print("ACESSO PERMITIDO")
            print(f"A senha foi digitada {count_of_passwords_entered} vezes")
            password_valid = True

        else:
            print("SENHA INVÁLIDA")

    except ValueError:
        print("SENHA INVÁLIDA")
        count_of_passwords_entered += 1