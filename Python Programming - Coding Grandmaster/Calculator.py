def addition(num1, num2):
    return num1 + num2


def multiplication(num1, num2):
    return num1 * num2


number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

print("1. Addition")
print("2. Multiplication")

choice = int(input("Enter your choice: "))

if choice == 1:
    result = addition(number1, number2)
    print("Addition:", result)

elif choice == 2:
    result = multiplication(number1, number2)
    print("Multiplication:", result)

else:
    print("Invalid choice")