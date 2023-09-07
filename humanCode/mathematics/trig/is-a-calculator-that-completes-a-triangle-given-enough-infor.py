from trianglesolver import solve


a = input("Input side a (enter for none): ")
if (a == ''):
    a = None
else:
    a = int(a)

b = input("Input side b (enter for none): ")
if (b == ''):
    b = None
else:
    b = int(b)

c = input("Input side c (enter for none): ")
if (c == ''):
    c = None
else:
    c = int(c)

A = input("Input angle A in radians (enter for none): ")
if (A == ''):
    A = None
else:
    A = int(A)

B = input("Input angle B in radians (enter for none): ")
if (B == ''):
    B = None
else:
    B = int(B)

C = input("Input angle C in radians (enter for none): ")
if (C == ''):
    C = None
else:
    C = int(C)

a, b, c, A, B, C = solve(a=a, b=b, c=c, A=A, B=B, C=C)

print("Side a: " + str(a))
print("Side b: " + str(b))
print("Side c: " + str(c))
print("Angle A: " + str(A))
print("Angle B: " + str(B))
print("Angle C: " + str(C))
