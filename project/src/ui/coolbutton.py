from tkinter import Frame, Button, PhotoImage
from constants import COLOR_DARK, COLOR_DARKER, COLOR_DARKEST, COLOR_LITE


class CoolButton(Frame):
    """Better looking button"""
    def __init__(self, root, imgfile, imgsize, size, cmd):
        Frame.__init__(self, root, bg=COLOR_DARK, border=1,
                       highlightbackground=COLOR_LITE, highlightthickness=1)
        img = PhotoImage(file=f'src/ui/icons/{imgfile}.png')
        img = img.subsample(imgsize)
        btn = Button(self, image=img, border=0, height=size, width=size,
                     background=COLOR_DARKER,
                     activebackground=COLOR_DARKEST,
                     command = cmd)
        btn.image = img
        btn.pack()
