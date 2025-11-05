total_value_of_cash_purchases = 0
total_value_of_purchases_made_in_credit = 0
total_value_of_purchases = 0
purchases_made_in_credit_list = []

for transaction in range(1, 16):

    valid_transaction_code = False
    try:
        while not valid_transaction_code:
            transaction_code = input("Informe o código da transação: ").upper()
            if transaction_code != "V" and transaction_code != "P":
                print("Código inválido, digite V para transação à vista ou P para transação à prazo: ")
            else:
                valid_transaction_code = True

    except ValueError:
        print("Valor inválido, digite V para transação à vista ou P para transação à prazo: ")

    valid_transaction_value = False
    while not valid_transaction_value:
        transaction_value_entered = input("Valor da transação: ")
        try:
            transaction_value = float(transaction_value_entered)
            valid_transaction_value = True
        except ValueError:
            print("Valor inválido, digite um valor válido: ")

    if transaction_code == "V":
        total_value_of_cash_purchases += transaction_value

    if transaction_code == "P":
        total_value_of_purchases_made_in_credit += transaction_value
        purchases_made_in_credit_list.append(transaction_value)

    total_value_of_purchases += transaction_value

if purchases_made_in_credit_list:
    value_of_the_first_installment = purchases_made_in_credit_list[0] / 3
else:
    value_of_the_first_installment = 0

print(f"Valor total das compras à vista: {total_value_of_cash_purchases}")
print(f"Valor total das compras à prazo: {total_value_of_purchases_made_in_credit}")
print(f"Valor total das compras: {total_value_of_purchases}")
print(f"Valor da primeira prestação das compras à prazo: {value_of_the_first_installment}")
