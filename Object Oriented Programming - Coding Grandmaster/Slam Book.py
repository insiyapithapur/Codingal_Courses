# Function to create a Slam Book
def create_slam_book():
    number_of_friends = int(input("Enter the number of friends: "))
    slam_book = []

    for i in range(number_of_friends):
        print("\nEnter details for Friend", i + 1)

        name = input("Enter name: ")
        nickname = input("Enter nickname: ")
        birthday = input("Enter date of birth: ")
        hobby = input("Enter favourite hobby: ")
        favourite_food = input("Enter favourite food: ")
        message = input("Write something about your friend: ")

        friend_details = {
            "Name": name,
            "Nickname": nickname,
            "Birthday": birthday,
            "Hobby": hobby,
            "Favourite Food": favourite_food,
            "Message": message
        }

        slam_book.append(friend_details)

    return slam_book


# Function to display Slam Book
def display_slam_book(slam_book):
    print("\n*************** MY SLAM BOOK ***************")

    for friend_number, friend in enumerate(slam_book, start=1):
        print("\nFriend", friend_number)
        print("--------------------------------------------")

        for key, value in friend.items():
            print(key, ":", value)


# Main program
my_slam_book = create_slam_book()
display_slam_book(my_slam_book)