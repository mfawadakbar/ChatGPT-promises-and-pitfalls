Sure! Here's a python script for a calculator that calculates the area and volume of a cube, sphere, or cone:

```python
import math

def cube():
    side_length = float(input("Enter the side length of the cube: "))
    area = 6 * side_length ** 2
    volume = side_length ** 3
    print("Area of the cube:", area)
    print("Volume of the cube:", volume)
    

def sphere():
    radius = float(input("Enter the radius of the sphere: "))
    area = 4 * math.pi * radius ** 2
    volume = (4/3) * math.pi * radius ** 3
    print("Area of the sphere:", area)
    print("Volume of the sphere:", volume)
    

def cone():
    radius = float(input("Enter the radius of the cone: "))
    height = float(input("Enter the height of the cone: "))
    slant_height = math.sqrt(radius ** 2 + height ** 2)
    area = math.pi * radius * (radius + slant_height)
    volume = (1/3) * math.pi * radius ** 2 * height
    print("Area of the cone:", area)
    print("Volume of the cone:", volume)


def calculator():
    print("Calculator Options:")
    print("1. Cube")
    print("2. Sphere")
    print("3. Cone")
    choice = int(input("Choose an option (1-3): "))

    if choice == 1:
        cube()
    elif choice == 2:
        sphere()
    elif choice == 3:
        cone()
    else:
        print("Invalid choice.")


calculator()
```
To run this script, save it in a file with the name `task.py`. Open the terminal or command prompt, navigate to the directory where the script is saved, and run the command `python task.py`.