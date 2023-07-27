# Get user input for a sequence of numbers
numbers = input("Enter a sequence of numbers (separated by spaces): ").split()

# Use list comprehension to square each odd number
squared_odd_numbers = [int(num)**2 for num in numbers if int(num) % 2 != 0]

# Print the squared odd numbers
print("Squared odd numbers:", squared_odd_numbers)
