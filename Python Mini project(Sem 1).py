from tkinter import *
import tkinter as tk
import random
import time  # Import the time module

word_hints = {
    0: {"word": "python", "hint": "Most widely used programming language"},
    1: {"word": "toxic", "hint": "Yash next movie"},
    2: {"word": "aatmatrisha", "hint": "Annual cultural fest of PESU RR Campus"},
    3: {"word": "patanjali", "hint": "India made ayurvedic brand"},
    4: {"word": "pathology", "hint": "Study of Disease"},
    5: {"word": "london", "hint": "Capital of England"},
    6: {"word": "kanyakumari", "hint": "Southernmost land part of India"},
    7: {"word": "microcontroller", "hint": "Highly integrated chip, contains CPU"},
    8: {"word": "kuvempu", "hint": "Kannada 1st Jnanapeeth awardee"},
    9: {"word": "india", "hint": "Which country has been elected to the Inter-governmental Committee of UNESCO 2003 Convention"},
}



def play_game(selected_word, level):
    guessed_letters = set()
    max_attempts = 6
    time_limit = 60  # Time limit for each level in seconds

    def check_guess():
        nonlocal max_attempts, time_limit
        guess = entry.get().lower()
        entry.delete(0, END)

        if guess in guessed_letters:
            result_label.config(text="You already guessed that letter. Try again.")
            return

        guessed_letters.add(guess)

        if guess not in selected_word["word"]:
            max_attempts -= 1
            result_label.config(text=f"Incorrect guess. Attempts left: {max_attempts}")

        display_word = "".join([letter if letter in guessed_letters else '_' for letter in selected_word["word"]])
        word_label.config(text=f"Current word: {display_word}")

        if set(selected_word["word"]) <= guessed_letters:
            result_label.config(text=f"Congratulations! You guessed the word: {selected_word['word']}")
        elif max_attempts == 0:
            result_label.config(text=f"Sorry, you ran out of attempts. The word was: {selected_word['word']}")
        else:
            result_label.config(text="")

    def update_timer():
        nonlocal time_limit
        timer_label.config(text=f"Time left: {time_limit} seconds")
        if time_limit > 0:
            time_limit -= 1
            game_window.after(1000, update_timer)
        else:
            result_label.config(text=f"Time's up! The word was: {selected_word['word']}")
            game_window.after(1000, game_window.destroy)  # Close the game window after displaying the result

    game_window = Toplevel(root)
    game_window.title(f"Hangman - Level {level}")
    game_window.geometry('300x400')
    game_window.configure(background='light blue')

    word_label = Label(game_window, text=f"Current word: {'_' * len(selected_word['word'])}", pady=10)
    word_label.pack()

    hint_label = Label(game_window, text=f"Hint: {selected_word['hint']}", pady=10)
    hint_label.pack()

    entry = Entry(game_window, width=20)
    entry.pack()

    guess_button = Button(game_window, text="Guess", command=check_guess, bg="orange", fg="white")
    guess_button.pack()

    result_label = Label(game_window, text="", pady=10)
    result_label.pack()

    timer_label = Label(game_window, text=f"Time left: {time_limit} seconds", pady=10)
    timer_label.pack()

    game_window.after(1000, update_timer)  # Start the timer

def new(level):
    selected_word = word_hints.get(level, {"word": "default", "hint": "default"})
    play_game(selected_word, level)

root = tk.Tk()
root.title("Hangman")
root.geometry("500x600")

level_buttons = []

for level in range(10):
    button = Button(root, padx=30, pady=10, text=f"Level {level}", command=lambda l=level: new(l), bg="blue", fg="white")
    button.pack()
    level_buttons.append(button)

root.mainloop()
