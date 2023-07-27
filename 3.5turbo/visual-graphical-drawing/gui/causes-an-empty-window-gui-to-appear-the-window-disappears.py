Sure! Here's a Python script that uses the tkinter library to create a simple empty window GUI that disappears when clicked:

```python
import tkinter as tk

def on_click(event):
    root.destroy()  # Close the window when clicked

root = tk.Tk()
root.title("Empty Window")
root.geometry("400x300")

# Bind the click event to the window
root.bind("<Button-1>", on_click)

root.mainloop()
```