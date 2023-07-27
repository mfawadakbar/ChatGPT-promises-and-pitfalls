Sure! Here's a Python script that uses the builder pattern to create a hamburger object:

```python
# Hamburger Builder

class Cheese:
    def __str__(self):
        return "Cheese"

class Bun:
    def __str__(self):
        return "Bun"

class Lettuce:
    def __str__(self):
        return "Lettuce"

class Beef:
    def __str__(self):
        return "Beef"

class Chicken:
    def __str__(self):
        return "Chicken"

class Tomato:
    def __str__(self):
        return "Tomato"

class Hamburger:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def __str__(self):
        return ", ".join(map(str, self.ingredients))


class HamburgerBuilder:
    def __init__(self):
        self.hamburger = Hamburger()

    def add_cheese(self):
        self.hamburger.add_ingredient(Cheese())
        return self

    def add_bun(self):
        self.hamburger.add_ingredient(Bun())
        return self

    def add_lettuce(self):
        self.hamburger.add_ingredient(Lettuce())
        return self

    def add_beef(self):
        self.hamburger.add_ingredient(Beef())
        return self

    def add_chicken(self):
        self.hamburger.add_ingredient(Chicken())
        return self

    def add_tomato(self):
        self.hamburger.add_ingredient(Tomato())
        return self

    def get_hamburger(self):
        return self.hamburger

# Usage
builder = HamburgerBuilder()
hamburger = builder.add_bun().add_beef().add_lettuce().add_tomato().add_cheese().get_hamburger()
print("Hamburger Ingredients: ", hamburger)
```

This script defines several ingredient classes (Cheese, Bun, Lettuce, Beef, Chicken, Tomato) and a Hamburger class. The HamburgerBuilder class provides methods for adding different ingredients to the hamburger using the builder pattern. Finally, a Hamburger object is built using the builder and its ingredients are printed.

To run the script, save it in a file named "task.py" and execute it using the command "python task.py".