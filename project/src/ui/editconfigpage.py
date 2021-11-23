from tkinter import Frame, Tk, ttk


class EditConfigPage(Frame):
    def __init__(self, root, controller):
        Frame.__init__(self, root)
        label = ttk.Label(self, text ='This page is for editing the configuration of the dashboard.')
        label.grid(row = 0, column = 0, padx = 100, pady = 100)
