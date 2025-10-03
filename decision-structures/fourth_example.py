name = input("Enter your name: ")
print("Hello %s!!!" %name)

minute = int(input("Enter how many minutes were spoken in the month: "))

if minute < 200:
    account = minute * 0.2

else:
    if minute <= 400:
        account = minute * 0.18

    else:
        account = minute * 0.15

print("The total account is R$%.2f" %account)