import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()


from tkinter import *
from tkinter import messagebox
app = Tk()

C = Canvas(app, bg="blue", height=1080, width=1920)
filename = PhotoImage(file = "TRUMPG.GIF")
background_label = Label((app), image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

from winsound import *

play = lambda: PlaySound('BINGA.wav', SND_FILENAME)
button = Button(app, text = 'Bing', command = play)

button.pack()

from winsound import *

play = lambda: PlaySound('BONGA.wav', SND_FILENAME)
button = Button(app, text = 'Bong', command = play)

button.pack()

C.pack()
root = tk.Tk()
app = Application(master=root)
app.mainloop()
