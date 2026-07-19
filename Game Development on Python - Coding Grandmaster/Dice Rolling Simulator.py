import random


def roll_dice():
    return random.randint(1, 6)


while True:
    print("\n******** DICE ROLLING SIMULATOR ********")
    choice = input("Press R to roll the dice or Q to quit: ").upper()

    if choice == "R":
        dice_value = roll_dice()
        print("You rolled:", dice_value)

        if dice_value == 6:
            print("Great! You got the highest number.")

        elif dice_value == 1:
            print("You got the lowest number.")

        else:
            print("Roll again and try to get 6!")

    elif choice == "Q":
        print("Thank you for playing!")
        break

    else:
        print("Invalid choice. Please enter R or Q.")