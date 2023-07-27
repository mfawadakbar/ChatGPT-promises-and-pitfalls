```python
import random

def generate_maze(rows, columns):
    # Initialize a grid of zeros
    maze = [[0] * columns for _ in range(rows)]
    
    # Recursive function to create the maze
    def create_maze(row, col):
        # Calculate the directions to move in
        directions = [(0, -2), (2, 0), (0, 2), (-2, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            new_row = row + dx
            new_col = col + dy
            
            # Check if the new position is valid
            if 0 <= new_row < rows and 0 <= new_col < columns and maze[new_row][new_col] == 0:
                # Carve a path through wall
                maze[new_row][new_col] = 1
                maze[row + dx // 2][col + dy // 2] = 1
                
                # Recursive call for the new position
                create_maze(new_row, new_col)
    
    # Start the maze generation from a random position
    start_row = random.randint(0, rows-1) // 2 * 2 + 1
    start_col = random.randint(0, columns-1) // 2 * 2 + 1
    create_maze(start_row, start_col)
    
    return maze

# Example usage
maze = generate_maze(10, 10)
for row in maze:
    print(row)
```