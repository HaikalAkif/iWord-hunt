# import
import tkinter as tk
from tkinter import *
from pydub import AudioSegment
from pydub.playback import play
from PIL import ImageTk, Image
from music import MusicUtil


class MainWindow():

    def __init__(self, music_player, window):
        self.music_player = music_player

        self.window = window
        self.window.geometry('600x400')
        self.window.title("Game menu")

        #Set Dimensions
        self.canvas = tk.Canvas(self.window, width=600, height=400)
        self.canvas.pack()

        # Create Background image
        bg_image = tk.PhotoImage(file="eid.png")
        self.canvas.create_image(0, 0, anchor="nw", image=bg_image)

        frame = tk.Frame()
        frame.pack()

        # Create a label for the title
        self.title_label = tk.Label(window, text="iWord Hunt!", font=("Inter", 24))
        self.title_label.pack(pady=30)

        # Create a button to start the game
        self.start_button = tk.Button(window, text="Start Game", command=self.start_game, font=("Inter", 16))
        self.start_button.pack(pady=10)

        # Create a option button
        self.option_button = tk.Button(window, text="Option", command= self.option_page , font=("Inter", 16))
        self.option_button.pack(pady=10)

        # Create a button to exit the game
        self.exit_button = tk.Button(window, text="Exit", command=window.destroy, font=("Inter", 16))
        self.exit_button.pack(pady=10)


    # Define function to start the game
    def start_game(self):
        #  Create the game window
        self.game_window = tk.Toplevel(self.window)
        self.game_window.title("My Game")
    
        # Create the game content
        self.game_label = tk.Label(self.game_window, text="iWord Hunt!", font=("Inter", 24), bg="blue", width=400, height=300)
        self.game_label.pack(pady=20)
    
        # Hide the main menu window
        self.window.withdraw()

    def option_page(self):
        # Create option window
        game_option = tk.Toplevel(self.window)
        game_option.title("Game Option")

        # Create option content
        game_option_label = tk.Label(game_option, text="Game Option", font=("Inter", 24), bg="green", fg="black", width=400, height=300)
        print("1.Language 2.Volume")

    # Hide the main menu window
    def exit_program(self):   
        self.window.withdraw()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":

    window = tk.Tk()
    music_util = MusicUtil("sdhr.mp3")

    w = MainWindow(music_util, window)
    w.run()