from tkinter import Frame, OptionMenu, StringVar, ttk, constants
from constants import COLOR_DARK


class EditConfigPage(Frame):
    def __init__(self, root, controller, loader):
        Frame.__init__(self, root)
        self._loader = loader
        self._config = self._loader.load()

        self.timespans = ['5 minutes', '15 minutes', '30 minutes', '1 hour', '6 hours', '12 hours', '1 day']
        self.intervals = ['30 seconds', '1 minute', '2 minutes', '5 minutes', '10 minutes', '15 minutes', '30 minutes']
        self.layouts = ['1', '2', '3', '4']

        self.v = StringVar(self, value=self._config['title'])
        self.option = StringVar(self, value=self._config['timespan'])
        self.option.set(self._config['timespan'])
        self.option2 = StringVar(self, value=self._config['interval'])
        self.optionx = StringVar(self, value='2')
        self.optiony = StringVar(self)

        title_label = ttk.Label(master=self, text="Dashboard title", background=COLOR_DARK)
        title_entry = ttk.Entry(master=self, textvariable=self.v)
        #variable.set(timespans[3])
        timespan_label = ttk.Label(master=self, text="Time span")
        timespan_entry = ttk.OptionMenu(self, self.option, *self.timespans)
        interval_label = ttk.Label(master=self, text="Refresh interval")
        interval_entry = ttk.OptionMenu(self, self.option2, *self.intervals)
        x_label = ttk.Label(master=self, text="Layout x")
        x_entry = ttk.OptionMenu(self, self.optionx, *self.layouts)
        y_label = ttk.Label(master=self, text="Layout y")
        y_entry = ttk.OptionMenu(self, self.optiony, *self.layouts)
        button = ttk.Button(master=self, text="Save", command=self.save_config)

        title_label.grid(row=1, column=1, padx = 100, pady = 5)
        title_entry.grid(row=1, column=2, sticky=constants.W, padx = 100, pady = 5)
        timespan_label.grid(row=2, column=1, padx = 100, pady = 5)
        timespan_entry.grid(row=2, column=2, sticky=(constants.E, constants.W), padx = 100, pady = 5)
        interval_label.grid(row=3, column=1, padx = 100, pady = 5)
        interval_entry.grid(row=3, column=2, sticky=(constants.E, constants.W), padx = 100, pady = 5)
        x_label.grid(row=4, column=1, padx = 100, pady = 5)
        x_entry.grid(row=4, column=2, sticky=(constants.E, constants.W), padx = 100, pady = 5)
        y_label.grid(row=5, column=1, padx = 100, pady = 5)
        y_entry.grid(row=5, column=2, sticky=(constants.E, constants.W), padx = 100, pady = 5)
        button.grid(row=6, column=1, columnspan=2, sticky=(constants.E, constants.W), padx = 100, pady = 5)

        #self.grid_columnconfigure(0, weight=1, minsize=0.1)
        #self.grid_columnconfigure(3, weight=1, minsize=0.1)
        self.grid_rowconfigure(0, weight=1, minsize=0.1)
        self.grid_rowconfigure(7, weight=1, minsize=0.1)

    def save_config(self, *args):
        print(f'You selected: {self.v.get()}')
        print(f'You selected: {self.option.get()}')
        print(f'You selected: {self.optionx.get()}')
        print(f'You selected: {self.optiony.get()}')
