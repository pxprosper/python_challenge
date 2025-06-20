# Project 6: Sum and Average of a List of Numbers

# Ask the user to input numbers separated by spaces
numbers_input = input("Enter numbers separated by spaces: ")

# Convert the input string into a list of floats
numbers = [float(num) for num in numbers_input.split()]

# Calculate sum and average
total = sum(numbers)
average = total / len(numbers) if numbers else 0

# Print the results
print(f"Sum: {total}")
print(f"Average: {average}")
