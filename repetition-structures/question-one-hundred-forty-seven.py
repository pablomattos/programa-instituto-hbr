final_price = 0
installment_value = 0

valid_car_value = False
while not valid_car_value:
    car_value_entered = input("Preço do carro: ")

    try:
        car_value = float(car_value_entered)
        if car_value > 0:
            valid_car_value = True
        else:
            print("Digite um valor positivo.")
    except ValueError:
        print("Valor inválido, digite um valor numérico válido.")

valid_payment_method = False
while not valid_payment_method:
    payment_method = input("Digite V para pagamento à vista ou P para pagamento parcelado: ").upper()
    if payment_method != "V" and payment_method != "P":
        print("Código inválido, digite V para pagamento à vista ou P para pagamento a prazo.")
    else:
        valid_payment_method = True

if payment_method == "V":
    final_price = car_value * 0.8
    print(30 * "-")
    print(f"Preço final do carro (à vista com desconto 20%): R$ {final_price:.2f}")
    print(30 * "-")
else:

    valid_installments = False
    posible_installments = [6, 12, 18, 24, 36, 48, 60]
    while not valid_installments:
        try:
            number_of_installments = int(input(f"Quantidade de parcelas {posible_installments}: "))
            if number_of_installments in posible_installments:
                valid_installments = True
            else:
                print("Número de parcelas inválido, escolha conforme a lista.")
        except ValueError:
            print("Digite um número inteiro válido para as parcelas.")

    match number_of_installments:
        case 6:
            final_price = car_value * 1.03
        case 12:
            final_price = car_value * 1.06
        case 18:
            final_price = car_value * 1.09
        case 24:
            final_price = car_value * 1.12
        case 36:
            final_price = car_value * 1.15
        case 48:
            final_price = car_value * 1.24
        case 60:
            final_price = car_value * 1.30

    installment_value = final_price / number_of_installments

    print(60 * "-")
    print(f"Preço final do carro: R$ {final_price:.2f}")
    print(60 * "-")
    print(f"Quantidade de parcelas: {number_of_installments}")
    print(60 * "-")
    print(f"Valor da parcela: R$ {installment_value:.2f}")
    print(60 * "-")
