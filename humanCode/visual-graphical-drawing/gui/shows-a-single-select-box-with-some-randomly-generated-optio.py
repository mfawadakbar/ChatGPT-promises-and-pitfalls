# This program will create a random populated text box

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Random Selectionbox")
root.geometry("600x400")

ttk.Label(root, text = "This box is filled with random items.",
          background = 'white', foreground = 'grey',
          font = ('Times New Roman', 15)).grid(row = 0, column = 1)

ttk.Label(root, text = "Select the item :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)

box = tk.StringVar()
item_chosen = ttk.Combobox(root, width = 30, textvariable=box)

# Create a randomized number. The random number will then pick that amount of items from a random list.
