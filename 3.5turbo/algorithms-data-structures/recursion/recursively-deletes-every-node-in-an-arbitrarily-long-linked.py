Here is a Python script to recursively delete every node in a linked list:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_linked_list(node):
    if node is None:  # Base case: reached end of the list
        return
    
    delete_linked_list(node.next)  # Recursively delete the next node
    del node  # Delete current node

# Function to create a linked list
def create_linked_list(elements):
    head = Node(elements[0])
    current = head
    for i in range(1, len(elements)):
        new_node = Node(elements[i])
        current.next = new_node
        current = new_node
    return head

# Function to print linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Test the program
if __name__ == "__main__":
    elements = [1, 2, 3, 4, 5]
    linked_list = create_linked_list(elements)

    print("Original Linked List:")
    print_linked_list(linked_list)

    delete_linked_list(linked_list)

    print("Linked List after deletion:")
    print_linked_list(linked_list)
```

This script defines a `Node` class to represent each node in the linked list. The `delete_linked_list` function takes a node as input and recursively deletes every node in the list by deleting the next node first and then the current node. The `create_linked_list` function is used to create a sample linked list, and the `print_linked_list` function is used to display the linked list before and after deletion.

To run the script, save it in a file called "task.py" and execute the command "python task.py". It will print the original linked list and the linked list after deletion.