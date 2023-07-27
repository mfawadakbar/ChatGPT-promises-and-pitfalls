Sure! Here's a Python script that generates a binary search tree and performs a postorder traversal using the `binarytree` library:

```python
# Import necessary libraries
from binarytree import build

def postorder_traversal(node):
    """
    Perform postorder traversal recursively

    Args:
        node: Binary tree node

    Returns:
        List: Postorder traversal values
    """
    if node is None:
        return []

    # Recursively traverse the left subtree
    left = postorder_traversal(node.left)

    # Recursively traverse the right subtree
    right = postorder_traversal(node.right)

    # Append current node value to the traversal list
    return left + right + [node.value]

# Generate a random binary search tree with 10 nodes
tree = build(height=4)

# Print the binary search tree
print("Binary Search Tree:")
print(tree)

# Perform postorder traversal and print the result
print("\nPostorder Traversal:")
postorder = postorder_traversal(tree)
print(postorder)
```

You need to install the `binarytree` library using the following command before executing the above script:

```
pip install binarytree
```

This script generates a random binary search tree with 10 nodes using the `build()` function from the `binarytree` library. Then, it performs a postorder traversal recursively on the generated tree using the `postorder_traversal()` function. Finally, it prints the generated tree and the postorder traversal result.