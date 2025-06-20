# Project 7: Store and Retrieve User Information

# Create an empty dictionary to store user info
user_info = {}


# Function to add users
def add_user():
    name = input("Enter name: ")
    age = input("Enter age: ")
    user_info[name] = age
    print(f"User {name} added.\n")


# Function to retrieve user info
def get_user():
    name = input("Enter name to retrieve info: ")
    if name in user_info:
        print(f"Name: {name}, Age: {user_info[name]}\n")
    else:
        print("User not found.\n")


# Main program loop
while True:
    print("1. Add user")
    print("2. Retrieve user info")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_user()
    elif choice == "2":
        get_user()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
