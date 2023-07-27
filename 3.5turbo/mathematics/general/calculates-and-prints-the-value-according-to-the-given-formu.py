import math

def calculate_value():
    # Ask the user for input values
    C = float(input("Enter the value of C: "))
    D = float(input("Enter the value of D: "))
    H = float(input("Enter the value of H: "))

    # Calculate the value according to the formula
    Q = math.sqrt((2 * C * D) / H)

    # Print the result
    print("The calculated value is:", Q)

if __name__ == "__main__":
    calculate_value()
