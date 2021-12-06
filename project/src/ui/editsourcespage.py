from tkinter import Frame, ttk
from constants import COLOR_DARK, SOURCE_ROWS
from ui.carousel import Carousel


class EditSourcesPage(Frame):
    def __init__(self, root, loader):
        Frame.__init__(self, root, bg=COLOR_DARK, border=1)

        label = ttk.Label(master=self, text='Data sources configuration', font=("Arial", 25),
                          background=COLOR_DARK, foreground='white')
        label.grid(row=0, column=1, padx=100, pady=10)

        carousel = Carousel(self, loader, SOURCE_ROWS, 'sources')
        carousel.grid(row=1, column=1)

        self.grid_rowconfigure(0, weight=1, minsize=0.1)
        self.grid_rowconfigure(2, weight=1, minsize=0.1)
