import sympy

print("Input numbers separated by spaces representing each row in your matrix")
print("E.g.: 1 2 3 4")
print("Ensure that each row has the same number of arguments.")
print("Press enter on an empty line to finish adding rows to your matrix.")
matrix = []
inputString = 'none'
while inputString != '':
    inputString = input("Enter your row (Empty for finished): ")
    if (inputString != ''):
        matrix.append([int(x) for x in inputString.split()])

matrix = sympy.Matrix(matrix)

M_rref = matrix.rref()
print("Rref {}".format(M_rref[0]))
