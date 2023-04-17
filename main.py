# import
import tkinter as tk
from tkinter import ttk

# Define the function to start the game
def start_game():
    print("Starting game...")

def option_page():
    print("1.Language 2.Volume")

# Create the main window
window = tk.Tk()
window.geometry('600x400')
window.title("Game Menu")

#background
# canvas = tk.Canvas(window, width=1200, height=900)
# canvas.pack()
# bg_image = tk.PhotoImage(file = "eid.png")
# canvas.create_image(0, 0, anchor = "nw", image=bg_image)

# Create a label for the title
title_label = tk.Label(window, text="iWord Hunt!", font=("Inter", 24))
title_label.pack(pady=30)

# Create a button to start the game
start_button = tk.Button(window, text="Start Game", command=start_game, font=("Inter", 16))
start_button.pack(pady=10)

# Create a option button
option_button = tk.Button(window, text="Option", command= option_page , font=("Inter", 16))
option_button.pack(pady=10)

# Create a button to exit the game
exit_button = tk.Button(window, text="Exit", command=window.destroy, font=("Inter", 16))
exit_button.pack(pady=10)

# Start the main event loop
window.mainloop()
