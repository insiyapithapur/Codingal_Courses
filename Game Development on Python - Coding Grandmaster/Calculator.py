def calculate_sum(numbers):
    return sum(numbers)


def calculate_difference(numbers):
    result = numbers[0]

    for number in numbers[1:]:
        result = result - number

    return result


def calculate_product(numbers):
    result = 1

    for number in numbers:
        result = result * number

    return result


def calculate_average(numbers):
    return sum(numbers) / len(numbers)


while True:
    print("\n******** BASIC CALCULATOR ********")
    print("1. Sum")
    print("2. Difference")
    print("3. Product")
    print("4. Average")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Calculator closed.")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Please try again.")
        continue

    count = int(input("How many numbers do you want to enter? "))

    if count <= 0:
        print("Please enter at least one number.")
        continue

    numbers = []

    for i in range(count):
        number = float(input("Enter number " + str(i + 1) + ": "))
        numbers.append(number)

    if choice == "1":
        print("Sum:", calculate_sum(numbers))

    elif choice == "2":
        print("Difference:", calculate_difference(numbers))

    elif choice == "3":
        print("Product:", calculate_product(numbers))

    elif choice == "4":
        print("Average:", calculate_average(numbers))