from tkinter import Frame, ttk
from constants import COLOR_DARK, GRAPH_ROWS
from ui.form import Form


class EditGraphsPage(Frame):
    def __init__(self, root, controller, loader):
        Frame.__init__(self, root, bg=COLOR_DARK, border=1)
        label = ttk.Label(self,text = 'And here you can configure the graphs to be shown in the dashboard.')
        label.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        path = ['graphs', 0]
        
        form = Form(self, GRAPH_ROWS, loader, path)
        form.grid(row=1, column=1)

        self.grid_rowconfigure(0, weight=1, minsize=0.1)
        self.grid_rowconfigure(2, weight=1, minsize=0.1)
