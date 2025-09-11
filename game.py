import random
import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Number Guessing Game")

# Generate random number
n = random.randint(1, 100)
guesses = 0

def check_guess():
    global guesses
    try:
        guess = int(entry.get())
        guesses += 1
        if guess > n:
            result_label.config(text="Lower number please!")
        elif guess < n:
            result_label.config(text="Higher number please!")
        else:
            messagebox.showinfo("Congratulations!", f"You guessed the number {n} in {guesses} attempts!")
            root.quit()  # Close the game window
    except ValueError:
        result_label.config(text="Please enter a valid number!")

# UI Elements
instruction_label = tk.Label(root, text="Guess a number between 1 and 100:")
instruction_label.pack()

entry = tk.Entry(root)
entry.pack()

guess_button = tk.Button(root, text="Check", command=check_guess)
guess_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()