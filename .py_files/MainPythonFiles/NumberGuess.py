from tkinter import *
import random

# User gets a total of 10 attempts
attempts = 10

# Answer is randomly generated between 1 and 99
answer = random.randint(1, 99)

def check_answer(entry_window,btn_check):
    global attempts
    global text

    # attempts is decreased by 1 to reflect users remaining attempts.
    attempts -= 1

    # Getting users input and converting it to integer data type.
    guess = int(entry_window.get())

    # Comparing guess to answer
    if answer == guess:
        text.set("You win!!")
        btn_check.pack_forget()
    # Ensuring the user still has attempts - if not remove option for more attempts.
    elif attempts == 0:
        text.set("You are out of attempts goodbye!")
        btn_check.pack_forget()
    # If guess is less than the answer - update user with remaining attempts and tell them to enter a higher number.
    elif guess < answer:
        text.set("Incorrect! - You have " + str(attempts) + " remaining attempts - Go higher!")
        # Clearing the input box for next attempt.
        entry_window.delete(0, END)
    # If guess is higher than the answer - update user with remaining attempts and tell them to enter a lower number.
    elif guess > answer:
        text.set("Incorrect! - You have " + str(attempts) + " remaining - Go lower!")
        # Clearing the input box for next attempt.
        entry_window.delete(0, END)
    return

def RunGuessingGame():
    root = Tk()
    # Using custom icon.
    root.title("Guess The Number")
    # Selecting size we want the window to be.
    root.geometry("325x150")
    # Label to instruct the user on what to do.
    label = Label(root, text="Guess the number between 1 and 99")
    label.pack()
    # User input box.
    entry_window = Entry(root, width=40, borderwidth=4)
    entry_window.pack()
    # Check button to find out if the entered amount is correct.
    btn_check = Button(root, text="Check", command=check_answer)
    btn_check.pack()
    # Quit button so that the user can leave the game
    btn_quit = Button(root, text="Quit", command=root.destroy)
    btn_quit.pack()

    # Creating a text variable so we can update it as the game progresses.
    text = StringVar()
    text.set("You have 10 attempts! Good luck")
    guess_attempts = Label(root, textvariable=text)
    guess_attempts.pack()

# loop for the program - Nothing after this point will run until the window is closed.
    root.mainloop()

if __name__ == "__Main__":
    RunGuessingGame()