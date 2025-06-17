# Project 2: Greet the user and calculate birth year

# Get user input
name = input("What is your name? ")
age = int(input("How old are you? "))

# Calculate birth year (assuming the current year is 2025)
current_year = 2025
birth_year = current_year - age

# Print greeting and birth year
print(f"Hello, {name}!")
print(f"You were born in {birth_year}.")
