from tkinter import Frame, ttk


class EditSourcesPage(Frame):
    def __init__(self, root, controller, loader):
        Frame.__init__(self, root)
        label = ttk.Label(self, text ='Here you can configure data sources.')
        label.grid(row = 0, column = 0, padx = 100, pady = 100)
