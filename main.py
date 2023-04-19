# import
import tkinter as tk
from tkinter import *
from pydub import AudioSegment
from pydub.playback import play
from PIL import ImageTk, Image

# Define the function to start the game
def start_game():
    # Create the game window
    game_window = tk.Toplevel(window)
    game_window.title("My Game")
    
    # Create the game content
    game_label = tk.Label(game_window, text="iWord Hunt!", font=("Inter", 24), bg="blue", width=400, height=300)
    game_label.pack(pady=20)
    
    # Hide the main menu window
    window.withdraw()

def option_page():
    # Create option window
    game_option = tk.Toplevel(window)
    game_option.title("Game Option")

    # Create option content
    game_label = tk.Label(game_option, text="Game Option", font=("Inter", 24), bg="green", fg="black", width=400, height=300)
    print("1.Language 2.Volume")

    # Hide the main menu window
    window.withdraw()


# # Set the dimensions of the window
# canvas = tk.Canvas(window, width=600, height=400)
# canvas.pack()

# #  Load the background image
# bg_image = tk.PhotoImage(file = "eid.png")

# # Create the background image
# canvas.create_image(0, 0, anchor="nw", image=bg_image)
# x jadi

# Create the main window
window = tk.Tk()
window.geometry('600x400')
window.title("Game Menu")



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





# Load and play song
# def play_song():
#     play(song)
#     window.after(len(song), play_song)
# song = AudioSegment.from_mp3("sdhr.mp3")
# play_song() xjadi