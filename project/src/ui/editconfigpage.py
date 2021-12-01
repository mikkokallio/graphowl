from tkinter import Frame, Button, OptionMenu, StringVar, ttk, constants
from constants import COLOR_DARK, COLOR_BRITE, NEON_ELECTRIC


class EditConfigPage(Frame):
    def __init__(self, root, controller, loader):
        Frame.__init__(self, root, bg=COLOR_DARK, border=1)
        self._loader = loader
        self._config = self._loader.load()

        self.timespans = ['none', '5 minutes', '15 minutes', '30 minutes', '1 hour', '6 hours', '12 hours', '1 day']
        self.intervals = ['none', '30 seconds', '1 minute', '2 minutes', '5 minutes', '10 minutes', '15 minutes', '30 minutes']
        self.layouts = [1, 2, 3, 4]

        self._title = StringVar(self, value=self._config['title'])
        self._timespan = StringVar(self, value=self._config['timespan'])
        self._interval = StringVar(self, value=self._config['interval'])
        self._layoutx = StringVar(self, value=self._config['layout']['x'])
        self._layouty = StringVar(self, value=self._config['layout']['y'])

        title_label = ttk.Label(master=self, text="Dashboard title", background=COLOR_DARK, foreground=COLOR_BRITE)
        title_entry = ttk.Entry(master=self, textvariable=self._title)
        timespan_label = ttk.Label(master=self, text="Time span", background=COLOR_DARK, foreground=COLOR_BRITE)
        timespan_entry = OptionMenu(self, self._timespan, *self.timespans)
        interval_label = ttk.Label(master=self, text="Refresh interval", background=COLOR_DARK, foreground=COLOR_BRITE)
        interval_entry = OptionMenu(self, self._interval, *self.intervals)
        x_label = ttk.Label(master=self, text="Layout x", background=COLOR_DARK, foreground=COLOR_BRITE)
        x_entry = OptionMenu(self, self._layoutx, *self.layouts)
        y_label = ttk.Label(master=self, text="Layout y", background=COLOR_DARK, foreground=COLOR_BRITE)
        y_entry = OptionMenu(self, self._layouty, *self.layouts)
        button = Button(master=self, text="Save", background=COLOR_BRITE, activebackground=NEON_ELECTRIC, command=self.save_config)

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
        self._config['title'] = self._title.get()
        self._config['timespan'] = self._timespan.get()
        self._config['interval'] = self._interval.get()
        self._config['layout']['x'] = int(self._layoutx.get())
        self._config['layout']['y'] = int(self._layouty.get())
        self._loader.save(self._config)
