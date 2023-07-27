Sure! Here's a simple implementation of a stack object that can be imported and used in other Python projects:

```python
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)
```

To use the stack object in another Python project, you can import it like this:

```python
from stack import Stack

# Example usage
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())    # Output: 3
print(stack.pop())     # Output: 3
print(stack.is_empty())   # Output: False
print(stack.size())    # Output: 2
```

You can save the code in a file named `stack.py` and then use it in other Python projects by importing it as shown above.