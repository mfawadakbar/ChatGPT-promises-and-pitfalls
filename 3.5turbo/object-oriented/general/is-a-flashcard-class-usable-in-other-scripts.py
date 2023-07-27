Sure! Here's a Python script that defines a `Flashcard` class which can be used in other scripts as a flashcard:

```python
import random

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __str__(self):
        return f"Question: {self.question}\nAnswer: {self.answer}"

    def ask_question(self):
        user_input = input(f"{self.question}: ")
        if user_input.lower() == self.answer.lower():
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {self.answer}")

    @staticmethod
    def quiz_flashcards(flashcards):
        random.shuffle(flashcards)
        for flashcard in flashcards:
            flashcard.ask_question()

# Example usage
flashcards = [
    Flashcard("What is the capital of France?", "Paris"),
    Flashcard("What is the largest planet in our solar system?", "Jupiter"),
    Flashcard("What is the symbol for the element gold?", "Au")
]

Flashcard.quiz_flashcards(flashcards)
```

You can add more flashcards to the `flashcards` list as needed. The `quiz_flashcards` method shuffles the flashcards and then asks the user the questions one by one, giving feedback on whether their answer is correct or not.

To run this script, save it in a file named `task.py`, then run the command `python task.py` in your terminal.