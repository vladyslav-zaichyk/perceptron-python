import tkinter
from tkinter import colorchooser

import trainer
from perceptron import Perceptron

INPUTS_COUNT = 3
SIGN_THRESHOLD = 255
LEARNING_RATE = 0.1


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

        color_chooser_button = tkinter.Button(self,
                                              text="Pick a color!",
                                              command=lambda: self.choose_color_dialog())
        color_chooser_button.pack(side="bottom", fill="both", expand=True)

    def choose_color_dialog(self):
        color = colorchooser.askcolor(self.box.canvas['bg'])

        # Guessing right color for the text
        guess = self.perceptron.guess(color[0])
        guessed_colour = "black" if guess > 0 else "white"

        self.box.change_text_color(guessed_colour)
        self.box.change_bg_color(color[1])


if __name__ == '__main__':
    root = tkinter.Tk()
    root.title("RGB Perceptron")
    icon = tkinter.PhotoImage(file='icon.png')
    root.wm_iconphoto(False, icon)
    app = MainApp(root)
    app.pack(side="top", fill="both", expand=True)

    # Training before ui starts
    trainer.train2pick_colours(app.perceptron, trainer.color_set)

    root.mainloop()
