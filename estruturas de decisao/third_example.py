name = input("Enter your name: ")
print("Hello %s!!!" %name)

numberOne = int(input("Enter the first number: "))
numberTwo = int(input("Enter the second number: "))

sum_of_numbers = numberOne + numberTwo

print("The result is: ", sum_of_numbers)

if numberOne > numberTwo:
    print("The first number is the biggest")

if numberTwo > numberOne:
    print("The first number is the biggest")

if numberTwo == numberOne:
    print("The numbers are the same")