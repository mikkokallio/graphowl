from tkinter import Frame, ttk
from constants import COLOR_DARK, FORM_ROWS
from ui.form import Form


class EditConfigPage(Frame):
    def __init__(self, root, loader):
        Frame.__init__(self, root, bg=COLOR_DARK, border=1)

        label = ttk.Label(master=self, text='Dashboard settings', font=("Arial", 25),
                          background=COLOR_DARK, foreground='white')
        label.grid(row=0, column=0, padx=100, pady=10)

        path = []

        form = Form(self, FORM_ROWS, loader, path)
        form.grid(row=1, column=0)

        self.grid_rowconfigure(0, weight=1, minsize=0.1)
        self.grid_rowconfigure(2, weight=1, minsize=0.1)
