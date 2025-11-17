valid_number = False
while not valid_number:
    number_of_people_entered = input("Digite o número de pessoas que farão o pedido: ")
    if number_of_people_entered.isdigit() and int(number_of_people_entered) > 0:
        number_of_people = int(number_of_people_entered)
        valid_number = True
    else:
        print("Número inválido, digite um número inteiro positivo.")

total_value = 0
current_person = 0
orders_by_person = []

while current_person < number_of_people:
    value_person = 0
    continue_request = True
    while continue_request:
        order_code = input("Digite o código do pedido (101, 201, 202, 301, 302, 500): ")

        match order_code:
            case "101":
                price = 3
            case "201":
                price = 5
            case "202":
                price = 6
            case "301":
                price = 4
            case "302":
                price = 5
            case "500":
                price = 2
            case _:
                price = None

        if price is not None:
            valid_quantity = False
            while not valid_quantity:
                quantity_entered = input("Digite a quantidade do item: ")
                if quantity_entered.isdigit() and int(quantity_entered) > 0:
                    quantity = int(quantity_entered)
                    valid_quantity = True
                else:
                    print("Quantidade inválida, digite um número inteiro positivo.")

            value_person += price * quantity

            add_item = input("Deseja adicionar mais um item no seu pedido? (S para sim, N para não): ").strip().upper()
            if add_item != "S":
                continue_request = False
        else:
            print("Código inválido, digite um dos códigos da tabela.")

    orders_by_person.append(value_person)
    total_value += value_person
    current_person += 1

print("\nResumo dos pedidos:")
i = 1
for value in orders_by_person:
    print(f"Pessoa {i}: R$ {value:.2f}")
    i += 1


print(f"\nValor final total a ser pago por todos os pedidos: R$ {total_value:.2f}")
