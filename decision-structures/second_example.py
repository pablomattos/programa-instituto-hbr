GASOLINE = 4.97
ALCOHOL = 3.48
value = 0.0

name = input("Enter your name: ")
print(f"Hello {name}!!!")
fuel = input("Enter G - Gasoline and A - Alcohol: ")
amount = float(input("Enter the quantity in liters: "))

if fuel.upper() == 'G':
    value = amount * GASOLINE
    print(f"Total value {value:.2f}")

elif fuel.upper() == 'A':
    value = amount * ALCOHOL
    print(f"Total value {value:.2f}")

else:
    print("Invalid option, run again and enter a valid option!")

