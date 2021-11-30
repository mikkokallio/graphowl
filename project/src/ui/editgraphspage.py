from tkinter import Frame, ttk


class EditGraphsPage(Frame):
    def __init__(self, root, controller):
        Frame.__init__(self, root)
        label = ttk.Label(self,text = 'And here you can configure the graphs to be shown in the dashboard.')
        label.grid(row = 0, column = 0, padx = 100, pady = 100)
