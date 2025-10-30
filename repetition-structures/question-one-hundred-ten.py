list_of_numbers = []
number = 0

while number < 20:
    number += 1
    list_of_numbers.append(number)

for n in list_of_numbers:

    divisors = []
    for divider in list_of_numbers: 
        if n % divider == 0:
            divisors.append(str(divider))

    print(f"{n}: {' '.join(divisors)}")
