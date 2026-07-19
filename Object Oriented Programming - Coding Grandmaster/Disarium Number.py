def is_disarium(number):
    digits = str(number)
    total = 0

    for position in range(len(digits)):
        digit = int(digits[position])
        total = total + digit ** (position + 1)

    return total == number


number = int(input("Enter a number: "))

if is_disarium(number):
    print(number, "is a Disarium number.")
else:
    print(number, "is not a Disarium number.")