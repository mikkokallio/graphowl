from tkinter import Frame
from constants import COLOR_DARK, FORM_ROWS
from ui.form import Form


class EditConfigPage(Frame):
    def __init__(self, root, controller, loader):
        Frame.__init__(self, root, bg=COLOR_DARK, border=1)
        
        path = []
        
        form = Form(self, FORM_ROWS, loader, path)
        form.grid(row=1, column=0)

        self.grid_rowconfigure(0, weight=1, minsize=0.1)
        self.grid_rowconfigure(2, weight=1, minsize=0.1)
