import tkinter
import numpy
from tkinter import colorchooser
from tkinter import messagebox

import trainer
from util.color_util import hex2rgb
from util.color_util import rand_hex_color
from perceptron import Perceptron

INPUTS_COUNT = 3
SIGN_THRESHOLD = 255
LEARNING_RATE = 0.01

WEIGHTS_FILE = "weights.data"


class DisplayBox(tkinter.Frame):
    """Box element with text inside"""

    def __init__(self, parent, *args, **kwargs):
        tkinter.Frame.__init__(self, parent, *args, **kwargs)
        self.canvas = tkinter.Canvas(self, height=300, width=300, bg="white")
        self.text = self.canvas.create_text(150, 150,
                                            fill="black",
                                            text="Hello there!",
                                            justify="center",
                                            font="Times 20 bold")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.current_text_color = 'black'

    def change_bg_color(self, color):
        self.canvas.configure(bg=color)

    def change_text_color(self, color):
        self.canvas.itemconfig(self.text, fill=color)


class MainApp(tkinter.Frame):
    """Main Application class"""

    def __init__(self, parent, *args, **kwargs):
        tkinter.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.box = DisplayBox(self)
        self.box.pack(side="top", fill="both", expand=True)
        # Perceptron initialization
        self.perceptron = Perceptron(SIGN_THRESHOLD, INPUTS_COUNT, LEARNING_RATE)
        print(self.perceptron.weights)

        # Load perceptron weights, if exist
        try:
            with open(WEIGHTS_FILE, 'r') as weights_file:
                self.perceptron.weights = numpy.fromfile(weights_file)
        except IOError:
            print("Weights not found, they will be generated randomly")
            self.perceptron.weights = numpy.random.rand(INPUTS_COUNT)

        print(self.perceptron.weights)
        color_chooser_button = tkinter.Button(self,
                                              text="Pick a color!",
                                              command=lambda: self.choose_color_dialog())
        training_panel = tkinter.Frame(self)
        error_button = tkinter.Button(training_panel,
                                      text="Wrong guess",
                                      command=lambda: self.wrong_guess())
        random_color_button = tkinter.Button(training_panel,
                                             text="Random color",
                                             command=lambda: self.set_random_bg_color())

        error_button.pack(side="left", fill="both", expand=True)
        random_color_button.pack(side="right", fill="both", expand=True)

        training_panel.pack(side="bottom", fill="both", expand=True)
        color_chooser_button.pack(side="bottom", fill="both", expand=True)

    def set_random_bg_color(self):
        self.perform_guess(rand_hex_color())

    def wrong_guess(self):
        bg_color = self.box.canvas['bg']
        text_color = self.box.current_text_color
        current_guess = -1 if text_color == 'white' else 1
        # Target is the opposite of current guess
        target = current_guess * -1
        self.perceptron.learn(trainer.hex2rgb(bg_color), target)
        self.box.change_text_color("black" if target > 0 else "white")

    def choose_color_dialog(self):
        # Check, if color dialog actually returns a color (if you press cancel - it will not)
        current_bg_color = self.box.canvas['bg']
        target_bg_color = colorchooser.askcolor(self.box.canvas['bg'])
        bg_color = current_bg_color if target_bg_color is None else target_bg_color[1]

        self.perform_guess(bg_color)

    def perform_guess(self, bg_color):
        guessed_text_color = self.__guess_text_color(bg_color)
        self.__change_colors(bg_color, guessed_text_color)

    def __guess_text_color(self, bg_color):
        guess = self.perceptron.guess(hex2rgb(bg_color))
        return "black" if guess > 0 else "white"

    def __change_colors(self, bg_color, text_color):
        self.box.current_text_color = text_color
        self.box.change_text_color(text_color)
        self.box.change_bg_color(bg_color)


def on_closing(perceptron):
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        # Write current perceptron weights to a file
        with open(WEIGHTS_FILE, "w") as weights_file:
            print(perceptron.weights)
            perceptron.weights.tofile(weights_file)
        root.destroy()


if __name__ == '__main__':
    root = tkinter.Tk()

    root.title("RGB Perceptron")
    icon = tkinter.PhotoImage(file='icon.png')
    root.wm_iconphoto(False, icon)
    app = MainApp(root)

    app.pack(side="top", fill="both", expand=True)

    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(app.perceptron))
    root.mainloop()
