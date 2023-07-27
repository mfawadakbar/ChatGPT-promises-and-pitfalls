def generate_dictionary(n):
    # Initialize an empty dictionary
    dictionary = {}

    # Iterate from 1 to n
    for i in range(1, n+1):
        # If i is divisible by 2, add it as key in the dictionary
        if i % 2 == 0:
            dictionary[i] = i**2
        # If i is not divisible by 2, add it as key and the square of i as value in the dictionary
        else:
            dictionary[i] = i**3
    
    return dictionary

if __name__ == '__main__':
    # Get user input for n
    n = int(input("Enter an integral number: "))
    
    # Generate the dictionary
    result = generate_dictionary(n)
    
    # Print the dictionary
    print(result)
