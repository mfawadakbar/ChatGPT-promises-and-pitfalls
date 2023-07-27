Here is the Python code for the requested script:

```python
class Animal:
    def go(self):
        print("The Animal is going!")


class Dog(Animal):
    def go(self):
        print("The Dog is going!")


class Cat(Animal):
    def go(self):
        print("The Cat is going!")


def main():
    # Create instances of each class
    animal = Animal()
    dog = Dog()
    cat = Cat()

    # Call the go() method on each instance
    animal.go()  # The Animal is going!
    dog.go()  # The Dog is going!
    cat.go()  # The Cat is going!


if __name__ == '__main__':
    main()
```

In this script, we define three classes: `Animal`, `Dog`, and `Cat`. Each class has a `go` method that overrides the same method in the parent class (`Animal`). When called, the `go` method of each class will print a specific message.

In the `main` function, we create instances of `Animal`, `Dog`, and `Cat`. We then call the `go` method on each instance, which demonstrates polymorphism. The output will show the appropriate message depending on the class of the instance.

To run the script, save it as a `.py` file (e.g., `task.py`) and execute it using the command `python task.py`. The script does not require any arguments or user input.