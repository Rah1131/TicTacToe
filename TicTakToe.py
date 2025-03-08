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
            messagebox.showinfo("Game Over", f"Player {1 if winner == 'X' else 2} Wins!")
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
            button.config(text="X", background="#FF5A79", foreground="white", font=('Arial', 40, 'bold'))  # Light pink for X
            player = 2
        else:
            button.config(text="O", background="#B22234", foreground="white", font=('Arial', 40, 'bold'))  # Dark red for O
            player = 1
        bc[bn - 1] = 1
        checkwinner()

# Initialize GUI
root = Tk()
root.title("Tic-Tac-Toe")
root.geometry("500x500")
root.configure(bg="white")  # Set background color

# Configure the grid to expand dynamically
for i in range(3):
    root.rowconfigure(i, weight=1)
    root.columnconfigure(i, weight=1)

# Create buttons with theme colors
buttons = []
for i in range(3):
    for j in range(3):
        btn = Button(root, text=" ", font=('Arial', 40, 'bold'), width=5, height=2,
                     bg="#FFB6C1", activebackground="#FF5A79", relief="flat",
                     command=lambda b=len(buttons) + 1: buttonpressed(b))
        btn.grid(row=i, column=j, sticky="nsew", padx=5, pady=5)  # Padding for spacing
        buttons.append(btn)

root.mainloop()
