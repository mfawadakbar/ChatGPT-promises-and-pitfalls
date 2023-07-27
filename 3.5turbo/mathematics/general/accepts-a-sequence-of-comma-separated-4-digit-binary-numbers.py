# Function to process the binary numbers
def process_binary_numbers(numbers):
    # Split the input sequence into individual binary numbers
    binary_list = numbers.split(",")
    
    # Convert each binary number to decimal and store in a list
    decimal_list = [int(binary, 2) for binary in binary_list]
    
    # Perform any operations on the decimal numbers here
    # For example, let's calculate the sum of the decimal numbers
    total_sum = sum(decimal_list)
    
    # Return the sum and the list of decimal numbers
    return total_sum, decimal_list


# Get input sequence from the user
input_sequence = input("Enter the sequence of comma-separated 4-digit binary numbers: ")

# Process the binary numbers
result_sum, result_list = process_binary_numbers(input_sequence)

# Print the sum and the list of decimal numbers
print("Sum of decimal numbers:", result_sum)
print("Decimal numbers:", result_list)
