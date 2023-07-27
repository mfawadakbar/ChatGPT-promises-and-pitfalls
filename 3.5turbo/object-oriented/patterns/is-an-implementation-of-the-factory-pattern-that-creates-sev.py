Sure, here's an implementation of the factory pattern that creates different types of animals with a `bark()` method:

```python
# Animal base class
class Animal:
    def bark(self):
        pass

# Dog subclass
class Dog(Animal):
    def bark(self):
        print("Woof!")

# Cat subclass
class Cat(Animal):
    def bark(self):
        print("Meow!")

# Factory class
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Invalid animal type")

# Main function
def main():
    animal_type = input("Enter animal type (dog/cat): ")
    animal = AnimalFactory.create_animal(animal_type)
    animal.bark()

# Run the main function
if __name__ == "__main__":
    main()
```

To run the above code, create a file named `task.py` and copy the code into it. Then, run the following command in the terminal:

```
python task.py
```

The script will prompt you to enter the animal type (dog or cat). After entering the animal type, it will create the corresponding animal object using the factory and call the `bark()` method to print the animal's sound to the screen.