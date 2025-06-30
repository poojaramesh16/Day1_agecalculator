from datetime import datetime

# Ask the user for their name and birth year
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

# Get the current year
current_year = datetime.now().year

# Calculate age
age = current_year - birth_year

# Display the result
print(f"Hello, {name}! You are {age} years old in {current_year}.")
