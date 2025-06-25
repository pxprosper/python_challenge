# Project 9: Handle invalid number input

def get_integer():
    while True:
        try:
            number = int(input("Enter an integer: "))
            print(f"You entered: {number}")
            break
        except ValueError:
            print("❌ Error: That was not a valid integer.")
        finally:
            print("✅ Program ended.\n")


# Call the function
get_integer()

