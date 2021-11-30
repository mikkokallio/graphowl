from tkinter import Frame, Tk, ttk, constants


class EditConfigPage(Frame):
    def __init__(self, root, controller):
        Frame.__init__(self, root)
        title_label = ttk.Label(master=self, text="Dashboard title")
        title_entry = ttk.Entry(master=self)
        timespan_label = ttk.Label(master=self, text="Time span")
        timespan_entry = ttk.Entry(master=self)
        interval_label = ttk.Label(master=self, text="Interval")
        interval_entry = ttk.Entry(master=self)
        x_label = ttk.Label(master=self, text="Layout x")
        x_entry = ttk.Entry(master=self)
        y_label = ttk.Label(master=self, text="Layout y")
        y_entry = ttk.Entry(master=self)
        button = ttk.Button(master=self, text="Save")

        title_label.grid(row=0, column=0, padx = 100, pady = 5)
        title_entry.grid(row=0, column=1, sticky=constants.W, padx = 100, pady = 5)
        timespan_label.grid(row=1, column=0, padx = 100, pady = 5)
        timespan_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx = 100, pady = 5)
        interval_label.grid(row=2, column=0, padx = 100, pady = 5)
        interval_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx = 100, pady = 5)
        x_label.grid(row=3, column=0, padx = 100, pady = 5)
        x_entry.grid(row=3, column=1, sticky=(constants.E, constants.W), padx = 100, pady = 5)
        y_label.grid(row=4, column=0, padx = 100, pady = 5)
        y_entry.grid(row=4, column=1, sticky=(constants.E, constants.W), padx = 100, pady = 5)
        button.grid(row=5, column=0, columnspan=2, sticky=(constants.E, constants.W), padx = 100, pady = 5)

        #self.grid_columnconfigure(1, weight=1, minsize=1)
