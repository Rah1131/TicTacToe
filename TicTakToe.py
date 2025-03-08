from tkinter import *
from tkinter import messagebox

# Function to check for a winner
def checkwinner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)  # Diagonals
    ]

    for combo in winning_combinations:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != " ":
            winner = buttons[combo[0]]["text"]
            messagebox.showinfo("Game Over", f"Player {1 if winner == 'X' else 2} Wins!!")
            root.quit()

# Player turn tracking
player = 1
bc = [0] * 9  # Track button clicks

# Function to handle button click
def buttonpressed(bn):
    global player
    button = buttons[bn - 1]

    if bc[bn - 1] == 0:
        if player == 1:
            button.config(text="X", background="yellow")  # Set "X" with light yellow background
            player = 2
        else:
            button.config(text="O", background="light green")  # Set "O" with light green background
            player = 1
        bc[bn - 1] = 1
        checkwinner()

# Initialize GUI
root = Tk()
root.title("Tic-Tac-Toe")

# Configure the grid to expand dynamically
for i in range(3):
    root.rowconfigure(i, weight=2)
    root.columnconfigure(i, weight=2)

# Create buttons
buttons = []
for i in range(3):
    for j in range(3):
        btn = Button(root, text=" ", font=('Arial', 30), width=4, height=2,
                     command=lambda b=len(buttons) + 1: buttonpressed(b))
        btn.grid(row=i, column=j, sticky="nsew")  # Expand buttons to fill the grid
        buttons.append(btn)

root.mainloop()