Here's an example of a Python script that randomly generates a small graph and determines if it is Hamiltonian:

```python
# Import necessary libraries
import networkx as nx
import random

# Function to check if a graph is Hamiltonian
def is_hamiltonian(graph):
    # Get all possible Hamiltonian cycles in the graph
    hamiltonian_cycles = list(nx.hamiltonian_cycles(graph))
    if len(hamiltonian_cycles) > 0:  # If there exists a Hamiltonian cycle
        return True
    else:
        return False

# Generate a small random graph
num_nodes = random.randint(3, 6)  # Random number of nodes between 3 and 6
graph = nx.gnm_random_graph(num_nodes, random.randint(num_nodes, num_nodes*(num_nodes-1)//2))

# Check if the graph is Hamiltonian
is_ham = is_hamiltonian(graph)

# Print the graph and the result
print("Generated Graph: ")
print(nx.adjacency_matrix(graph))
print("Is Hamiltonian: ", is_ham)
```

Note that this script uses the `networkx` library to generate and analyze the graph. You can install it by running `pip install networkx`. The `is_hamiltonian()` function checks if the graph has any Hamiltonian cycles using the `nx.hamiltonian_cycles()` function.

Hope this helps! Let me know if you have any questions.