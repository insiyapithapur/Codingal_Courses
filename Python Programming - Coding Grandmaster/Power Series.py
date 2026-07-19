terms = int(input("Enter the number of terms: "))

print("Power Series:")

for i in range(1, terms + 1):
    print(i ** i, end=" ")